"""Difference-in-differences estimation with diagnostics."""

from typing import Optional, Dict, List, Any
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class DifferenceInDifferences(BaseEconometricModel):
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
        super().__init__(data=data, outcome=outcome)
        self.treatment = treatment
        self.time = time
        self.unit = unit
        self.treatment_period = treatment_period

        # Validate required columns
        required_cols = [outcome, treatment, time, unit]
        self._validate_columns(required_cols)
        
        # Create post-treatment indicator
        if treatment_period is None:
            # Infer from treatment variable
            treated_units = data[data[treatment] == 1][unit].unique()
            treated_data = data[data[unit].isin(treated_units)]
            self.treatment_period = treated_data[time].min()
        
        self.data['post'] = (self.data[time] >= self.treatment_period).astype(int)
        self.data['treat_post'] = self.data[treatment] * self.data['post']

    def _detect_staggered_treatment(self) -> Dict[str, Any]:
        """Detect if treatment is staggered across units.

        Staggered treatment occurs when different units are treated at different times.
        Two-way fixed effects (TWFE) DiD can be biased with staggered treatment due to
        using already-treated units as controls (Goodman-Bacon 2021).

        Returns:
            Dictionary with:
                - is_staggered: bool, whether treatment is staggered
                - n_treatment_times: int, number of distinct treatment times
                - treatment_times: list of treatment periods
                - warning_message: str, warning message if staggered
        """
        # Get treated units
        treated_units = self.data[self.data[self.treatment] == 1][self.unit].unique()

        if len(treated_units) == 0:
            return {
                'is_staggered': False,
                'n_treatment_times': 0,
                'treatment_times': [],
                'warning_message': ''
            }

        # For each treated unit, find when they first got treated
        treatment_times = []
        for unit in treated_units:
            unit_data = self.data[self.data[self.unit] == unit].sort_values(self.time)
            # Find first period where treatment = 1
            treated_periods = unit_data[unit_data[self.treatment] == 1][self.time]
            if len(treated_periods) > 0:
                treatment_times.append(treated_periods.min())

        unique_treatment_times = sorted(set(treatment_times))
        is_staggered = len(unique_treatment_times) > 1

        warning_msg = ""
        if is_staggered:
            warning_msg = (
                f"\n{'='*70}\n"
                f"WARNING: Staggered Treatment Detected\n"
                f"{'='*70}\n"
                f"Your data has {len(unique_treatment_times)} different treatment times: "
                f"{unique_treatment_times}\n\n"
                f"Two-Way Fixed Effects (TWFE) DiD can be BIASED with staggered treatment.\n\n"
                f"Issues:\n"
                f"  1. TWFE uses already-treated units as controls (forbidden comparisons)\n"
                f"  2. Treatment effects can be weighted by variance, not just sample size\n"
                f"  3. Heterogeneous treatment effects can lead to NEGATIVE weights\n\n"
                f"References:\n"
                f"  - Goodman-Bacon (2021): 'Difference-in-differences with variation in \n"
                f"    treatment timing', Journal of Econometrics\n"
                f"  - Callaway & Sant'Anna (2021): 'Difference-in-Differences with multiple\n"
                f"    time periods', Journal of Econometrics\n"
                f"  - Sun & Abraham (2021): 'Estimating dynamic treatment effects in event\n"
                f"    studies with heterogeneous treatment effects'\n\n"
                f"Recommended alternatives:\n"
                f"  - Callaway & Sant'Anna (2021) estimator: Controls for staggered adoption\n"
                f"  - Sun & Abraham (2021): Interaction-weighted estimator\n"
                f"  - Stacked DiD: Create separate datasets for each treatment cohort\n"
                f"  - Imputation estimators (Borusyak et al. 2024)\n"
                f"{'='*70}\n"
            )

        return {
            'is_staggered': is_staggered,
            'n_treatment_times': len(unique_treatment_times),
            'treatment_times': unique_treatment_times,
            'warning_message': warning_msg
        }

    def estimate(self) -> EstimationResult:
        """Estimate difference-in-differences coefficient.

        Uses two-way fixed effects specification:
        Y_it = α + β(Treat_i × Post_t) + γ_i + δ_t + ε_it

        Returns:
            EstimationResult with:
                - coefficients: {'treat_post': DiD estimate (β)}
                - std_errors: {'treat_post': standard error}
                - pvalues: {'treat_post': p-value}
                - ci_lower/ci_upper: Confidence intervals
                - nobs: Number of observations
                - fit_stats: rsquared
                - diagnostics: n_units, n_periods, treatment_period
        """
        # Check for staggered treatment and emit warning if detected
        staggered_info = self._detect_staggered_treatment()
        if staggered_info['is_staggered']:
            warnings.warn(staggered_info['warning_message'], UserWarning, stacklevel=2)

        # Prepare data
        model_data = self.data[[self.outcome, 'treat_post', self.unit, self.time]].dropna()

        # Create dummy variables for fixed effects (ensure numeric dtype)
        unit_dummies = pd.get_dummies(model_data[self.unit], prefix='unit', drop_first=True, dtype=float)
        time_dummies = pd.get_dummies(model_data[self.time], prefix='time', drop_first=True, dtype=float)

        # Combine variables - ensure treat_post is float
        treat_post_df = model_data[['treat_post']].astype(float)
        X = pd.concat([
            treat_post_df,
            unit_dummies,
            time_dummies
        ], axis=1)

        # Add constant for proper inference
        X = add_constant(X)

        y = model_data[self.outcome].astype(float)

        # Estimate with clustered standard errors at unit level
        model = OLS(y, X)
        self.results = model.fit(cov_type='cluster', cov_kwds={'groups': model_data[self.unit]})
        self._estimated = True

        # Extract DiD coefficient (only report treat_post, not fixed effects)
        did_coef = self.results.params['treat_post']
        did_se = self.results.bse['treat_post']
        did_pval = self.results.pvalues['treat_post']
        did_tval = self.results.tvalues['treat_post']

        # Confidence interval
        ci = self.results.conf_int().loc['treat_post']

        return create_estimation_result(
            coefficients={'treat_post': float(did_coef)},
            std_errors={'treat_post': float(did_se)},
            pvalues={'treat_post': float(did_pval)},
            tvalues={'treat_post': float(did_tval)},
            ci_lower={'treat_post': float(ci[0])},
            ci_upper={'treat_post': float(ci[1])},
            nobs=int(self.results.nobs),
            model_type='did',
            fit_stats={
                'rsquared': float(self.results.rsquared),
            },
            diagnostics={
                'n_units': int(model_data[self.unit].nunique()),
                'n_periods': int(model_data[self.time].nunique()),
                'treatment_period': self.treatment_period,
            }
        )
    
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

    def run_event_study(self, leads: int = 2, lags: int = 3) -> Dict[str, Any]:
        """Run event study to examine dynamic treatment effects.

        An event study estimates treatment effects for multiple periods before and after
        treatment, allowing visualization of pre-trends and dynamic treatment effects.
        This is crucial for validating parallel trends and understanding treatment dynamics.

        Args:
            leads: Number of periods before treatment to include (default: 2)
            lags: Number of periods after treatment to include (default: 3)

        Returns:
            Dictionary with:
                - coefficients: Dict mapping relative period to coefficient
                - std_errors: Dict mapping relative period to standard error
                - ci_lower: Dict mapping relative period to lower CI bound
                - ci_upper: Dict mapping relative period to upper CI bound
                - pvalues: Dict mapping relative period to p-value
                - omitted_period: The period omitted as reference (typically -1)

        Example:
            results = model.run_event_study(leads=2, lags=3)
            # Results include periods: -2, -1 (omitted), 0, 1, 2, 3
            # where 0 is the treatment period
        """
        if self.results is None:
            raise ValueError("Must estimate model first. Call estimate().")

        # Create relative time variable (periods relative to treatment)
        event_data = self.data.copy()
        event_data['rel_time'] = event_data[self.time] - self.treatment_period

        # Get valid relative time periods
        unique_rel_times = sorted(event_data['rel_time'].unique())
        min_rel = max(-leads, min(unique_rel_times))
        max_rel = min(lags, max(unique_rel_times))

        # Filter to valid range
        event_data = event_data[
            (event_data['rel_time'] >= min_rel) &
            (event_data['rel_time'] <= max_rel)
        ].copy()

        # Create event time dummies, omitting period -1 as reference
        event_dummies = []
        event_periods = []
        omitted_period = -1

        for t in range(min_rel, max_rel + 1):
            if t == omitted_period:
                continue
            dummy_name = f'event_t{t}'
            # Only create dummy for treated units
            event_data[dummy_name] = (
                (event_data['rel_time'] == t) &
                (event_data[self.treatment] == 1)
            ).astype(float)
            event_dummies.append(dummy_name)
            event_periods.append(t)

        # Add unit and time fixed effects
        unit_dummies = pd.get_dummies(event_data[self.unit], prefix='unit',
                                     drop_first=True, dtype=float)
        time_dummies = pd.get_dummies(event_data[self.time], prefix='time',
                                     drop_first=True, dtype=float)

        # Prepare regression
        X = pd.concat([
            event_data[event_dummies],
            unit_dummies,
            time_dummies
        ], axis=1)
        X = add_constant(X)
        y = event_data[self.outcome].astype(float)

        # Estimate with clustered standard errors
        model = OLS(y, X)
        results = model.fit(cov_type='cluster', cov_kwds={'groups': event_data[self.unit]})

        # Extract coefficients for event time dummies
        coefficients = {}
        std_errors = {}
        ci_lower = {}
        ci_upper = {}
        pvalues = {}

        # Add reference period (omitted, so coefficient = 0)
        coefficients[omitted_period] = 0.0
        std_errors[omitted_period] = 0.0
        ci_lower[omitted_period] = 0.0
        ci_upper[omitted_period] = 0.0
        pvalues[omitted_period] = 1.0

        # Extract estimates for each event period
        for t, dummy in zip(event_periods, event_dummies):
            coefficients[t] = float(results.params[dummy])
            std_errors[t] = float(results.bse[dummy])
            ci = results.conf_int().loc[dummy]
            ci_lower[t] = float(ci[0])
            ci_upper[t] = float(ci[1])
            pvalues[t] = float(results.pvalues[dummy])

        return {
            'coefficients': coefficients,
            'std_errors': std_errors,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'pvalues': pvalues,
            'omitted_period': omitted_period,
            'nobs': int(results.nobs),
            'rsquared': float(results.rsquared)
        }

    def summary(self) -> str:
        """Generate summary of DiD estimation results.

        Returns:
            Formatted summary string
        """
        self._check_estimated()
        return str(self.results.summary())

    def plot_parallel_trends(
        self,
        ax: Optional[plt.Axes] = None,
        figsize: tuple = (10, 6)
    ) -> plt.Figure:
        """Plot parallel trends for visual inspection.

        Shows mean outcome over time for treated and control groups.

        Args:
            ax: Optional matplotlib axes to plot on
            figsize: Figure size in inches (width, height)

        Returns:
            Matplotlib figure
        """
        from src.visualization.plots import plot_parallel_trends
        return plot_parallel_trends(self, ax=ax, figsize=figsize)

    def plot_event_study(
        self,
        leads: int = 2,
        lags: int = 3,
        ax: Optional[plt.Axes] = None,
        figsize: tuple = (10, 6)
    ) -> plt.Figure:
        """Plot event study with dynamic treatment effects.

        Estimates and plots treatment effects for each time period relative to treatment.

        Args:
            leads: Number of periods before treatment to include
            lags: Number of periods after treatment to include
            ax: Optional matplotlib axes to plot on
            figsize: Figure size in inches

        Returns:
            Matplotlib figure
        """
        # Run event study to get coefficients
        event_results = self.run_event_study(leads=leads, lags=lags)

        # Extract what we need for plotting
        coefficients = event_results['coefficients']
        ci_lower = event_results['ci_lower']
        ci_upper = event_results['ci_upper']

        # Plot
        from src.visualization.plots import plot_event_study
        return plot_event_study(coefficients, ci_lower, ci_upper, ax=ax, figsize=figsize)

