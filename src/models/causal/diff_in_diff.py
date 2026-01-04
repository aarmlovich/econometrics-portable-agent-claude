"""Difference-in-differences estimation with diagnostics."""

from typing import Optional, Dict, List
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
import statsmodels.api as sm


class DifferenceInDifferences:
    """Difference-in-differences estimator with parallel trends testing.
    
    Estimates treatment effects using the difference-in-differences
    identification strategy. Includes parallel trends testing and
    basic diagnostics.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        treatment: str,
        time: str,
        unit: str,
        treatment_period: Optional[int] = None
    ):
        """Initialize difference-in-differences model.
        
        Args:
            data: Panel data DataFrame
            outcome: Name of outcome variable
            treatment: Name of treatment indicator (1 if treated, 0 if control)
            time: Name of time period variable
            unit: Name of unit identifier variable
            treatment_period: Time period when treatment starts.
                             If None, inferred from treatment indicator.
        """
        self.data = data.copy()  # Preserve original data
        self.outcome = outcome
        self.treatment = treatment
        self.time = time
        self.unit = unit
        self.treatment_period = treatment_period
        self.results = None
        
        # Validate required columns
        required_cols = [outcome, treatment, time, unit]
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Create post-treatment indicator
        if treatment_period is None:
            # Infer from treatment variable
            treated_units = data[data[treatment] == 1][unit].unique()
            treated_data = data[data[unit].isin(treated_units)]
            self.treatment_period = treated_data[time].min()
        
        self.data['post'] = (self.data[time] >= self.treatment_period).astype(int)
        self.data['treat_post'] = self.data[treatment] * self.data['post']
    
    def estimate(self) -> Dict[str, float]:
        """Estimate difference-in-differences coefficient.
        
        Uses two-way fixed effects specification:
        Y_it = α + β(Treat_i × Post_t) + γ_i + δ_t + ε_it
        
        Returns:
            Dictionary containing:
                - did_coefficient: DiD estimate (β)
                - std_error: Standard error
                - pvalue: P-value
                - ci_lower: Lower 95% confidence interval
                - ci_upper: Upper 95% confidence interval
                - nobs: Number of observations
        """
        # Prepare data
        model_data = self.data[[self.outcome, 'treat_post', self.unit, self.time]].dropna()
        
        # Create dummy variables for fixed effects
        unit_dummies = pd.get_dummies(model_data[self.unit], prefix='unit', drop_first=True)
        time_dummies = pd.get_dummies(model_data[self.time], prefix='time', drop_first=True)
        
        # Combine variables
        X = pd.concat([
            model_data[['treat_post']],
            unit_dummies,
            time_dummies
        ], axis=1)
        y = model_data[self.outcome]
        
        # Estimate with clustered standard errors at unit level
        model = OLS(y, X)
        self.results = model.fit(cov_type='cluster', cov_kwds={'groups': model_data[self.unit]})
        
        # Extract DiD coefficient
        did_coef = self.results.params['treat_post']
        did_se = self.results.bse['treat_post']
        did_pval = self.results.pvalues['treat_post']
        
        # Confidence interval
        ci = self.results.conf_int().loc['treat_post']
        
        return {
            'did_coefficient': float(did_coef),
            'std_error': float(did_se),
            'pvalue': float(did_pval),
            'ci_lower': float(ci[0]),
            'ci_upper': float(ci[1]),
            'nobs': int(self.results.nobs)
        }
    
    def test_parallel_trends(
        self,
        periods_before: int = 3
    ) -> Dict[str, float]:
        """Test for parallel trends in pre-treatment periods.
        
        Tests whether treated and control groups have similar trends
        before treatment. This is a key identifying assumption for DiD.
        
        Args:
            periods_before: Number of pre-treatment periods to use in test
            
        Returns:
            Dictionary with test results:
                - pvalue: P-value for test of differential pre-trends
                - test_statistic: Test statistic value
                - null_hypothesis: "No differential pre-trends"
        """
        if self.results is None:
            raise ValueError("Must estimate model first. Call estimate().")
        
        # Get pre-treatment data
        pre_data = self.data[self.data[self.time] < self.treatment_period].copy()
        
        if len(pre_data) < periods_before:
            raise ValueError(
                f"Insufficient pre-treatment periods: "
                f"need {periods_before}, have {len(pre_data[self.time].unique())}"
            )
        
        # Get pre-treatment periods
        pre_periods = sorted(pre_data[self.time].unique())[-periods_before:]
        pre_data = pre_data[pre_data[self.time].isin(pre_periods)]
        
        # Estimate interaction between treatment and time in pre-period
        pre_data['time_trend'] = pre_data[self.time] - pre_data[self.time].min()
        pre_data['treat_trend'] = pre_data[self.treatment] * pre_data['time_trend']
        
        # Simple regression test
        y_pre = pre_data[self.outcome]
        X_pre = add_constant(pre_data[['treat_trend', self.treatment, 'time_trend']])
        
        test_model = OLS(y_pre, X_pre)
        test_results = test_model.fit(cov_type='cluster', 
                                     cov_kwds={'groups': pre_data[self.unit]})
        
        treat_trend_pval = test_results.pvalues['treat_trend']
        treat_trend_stat = test_results.tvalues['treat_trend']
        
        return {
            'pvalue': float(treat_trend_pval),
            'test_statistic': float(treat_trend_stat),
            'null_hypothesis': 'No differential pre-trends',
            'interpretation': (
                'p > 0.05 suggests parallel trends' 
                if treat_trend_pval > 0.05 
                else 'p < 0.05 suggests non-parallel trends (violation of assumption)'
            )
        }
    
    def summary(self) -> str:
        """Generate summary of DiD estimation results.
        
        Returns:
            Formatted summary string
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return str(self.results.summary())

