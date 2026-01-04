"""Random effects panel data estimation."""

from typing import Optional, List, Dict, Any
import numpy as np
import pandas as pd
from linearmodels.panel import RandomEffects as LMRandomEffects
from scipy import stats
import warnings


class RandomEffects:
    """Random effects panel data estimator with GLS estimation.
    
    Estimates panel data models using generalized least squares (GLS)
    under the assumption that unobserved heterogeneity is uncorrelated
    with regressors. More efficient than fixed effects if assumption holds.
    
    Specification: Y_it = X_it'β + α_i + ε_it
    Where α_i ~ N(0, σ²_α) (random effect, uncorrelated with X_it)
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        covariates: List[str],
        entity: str,
        time: str,
        cluster_se: bool = True
    ):
        """Initialize random effects model.
        
        Args:
            data: Panel data DataFrame
            outcome: Name of outcome variable
            covariates: List of covariate variable names
            entity: Name of entity (unit) identifier variable
            time: Name of time period variable
            cluster_se: If True, cluster standard errors at entity level
        """
        self.data = data.copy()  # Preserve original data
        self.outcome = outcome
        self.covariates = covariates
        self.entity = entity
        self.time = time
        self.cluster_se = cluster_se
        self.results = None
        self.hausman_results = None
        
        # Validate required columns
        required_cols = [outcome, entity, time] + covariates
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Set up panel index
        self.data = self.data.set_index([entity, time])
        self.data = self.data.sort_index()
    
    def estimate(self) -> Dict[str, Any]:
        """Estimate random effects model using GLS.
        
        Returns:
            Dictionary containing:
                - coefficients: Estimated coefficients
                - std_errors: Standard errors
                - pvalues: P-values
                - rsquared: Overall R-squared
                - rsquared_within: Within R-squared
                - rsquared_between: Between R-squared
                - nobs: Number of observations
                - nentities: Number of entities
                - ntime: Number of time periods
        """
        # Prepare data
        y = self.data[self.outcome]
        X = self.data[self.covariates]
        
        # Drop missing values
        model_data = pd.concat([y, X], axis=1).dropna()
        y = model_data[self.outcome]
        X = model_data[self.covariates]
        
        # Estimate with linearmodels RandomEffects
        model = LMRandomEffects(dependent=y, exog=X)
        
        if self.cluster_se:
            self.results = model.fit(cov_type='clustered', cluster_entity=True)
        else:
            self.results = model.fit()
        
        # Store parameter names for Hausman test
        self.param_names = list(self.results.params.index)
        
        # Extract results (match FixedEffects pattern - return arrays)
        return {
            'coefficients': self.results.params.values,
            'std_errors': self.results.std_errors.values,
            'pvalues': self.results.pvalues.values,
            'rsquared': float(self.results.rsquared),
            'rsquared_within': float(self.results.rsquared_within),
            'rsquared_between': float(self.results.rsquared_between),
            'nobs': int(self.results.nobs),
            'nentities': int(self.results.entity_info.total),
            'ntime': int(self.results.time_info.total),
            'param_names': self.param_names  # Store names for Hausman test
        }
    
    def test_hausman(self, fe_results: Any) -> Dict[str, float]:
        """Test Hausman specification test (FE vs RE).
        
        Tests H0: Random effects is appropriate (unobserved heterogeneity
        is uncorrelated with regressors). If p < 0.05, reject H0 and use
        fixed effects instead.
        
        Args:
            fe_results: Results from FixedEffects.estimate() method.
                       Should be a dictionary with 'coefficients' key.
        
        Returns:
            Dictionary containing:
                - hausman_statistic: Hausman test statistic
                - pvalue: P-value
                - degrees_of_freedom: Degrees of freedom
                - null_hypothesis: "Random effects is appropriate"
                - interpretation: Text interpretation
        """
        if self.results is None:
            self.estimate()
        
        # Get coefficients from RE and FE
        re_coefs = self.results.params
        
        # FE coefficients come as array, need to map to names
        # FixedEffects returns arrays, so we need to use the param_names we stored
        # or assume same order as covariates
        fe_coefs_array = fe_results['coefficients']
        fe_std_errors_array = fe_results['std_errors']
        
        # Get FE parameter names (if available) or use covariates
        if 'param_names' in fe_results:
            fe_param_names = fe_results['param_names']
        else:
            # FixedEffects doesn't return param_names, so use covariates in order
            fe_param_names = self.covariates[:len(fe_coefs_array)]
        
        # Create Series for FE coefficients and std errors
        fe_coefs = pd.Series(fe_coefs_array, index=fe_param_names)
        fe_std_errors = pd.Series(fe_std_errors_array, index=fe_param_names)
        
        # Align coefficients (only common covariates)
        common_vars = re_coefs.index.intersection(fe_coefs.index)
        if len(common_vars) == 0:
            raise ValueError("No common covariates between RE and FE models")
        
        re_coefs_aligned = re_coefs.loc[common_vars]
        fe_coefs_aligned = fe_coefs.loc[common_vars]
        fe_std_errors_aligned = fe_std_errors.loc[common_vars]
        
        # Get variance-covariance matrices
        re_cov = self.results.cov.loc[common_vars, common_vars]
        
        # FE covariance: use diagonal approximation from std errors
        fe_cov = np.diag(fe_std_errors_aligned.values**2)
        
        # Difference in coefficients
        diff = (fe_coefs_aligned - re_coefs_aligned).values
        
        # Variance of difference: Var(β_FE - β_RE) = Var(β_FE) - Var(β_RE)
        # (since FE and RE are independent under H0)
        var_diff = fe_cov - re_cov.values
        
        # Handle potential negative variances (can happen with approximation)
        # Use absolute value or ensure positive definite
        try:
            var_diff_inv = np.linalg.inv(var_diff)
        except np.linalg.LinAlgError:
            # If singular, use pseudo-inverse
            var_diff_inv = np.linalg.pinv(var_diff)
        
        # Hausman statistic: (β_FE - β_RE)' * Var(β_FE - β_RE)^{-1} * (β_FE - β_RE) ~ χ²(k)
        hausman_stat = float(diff.T @ var_diff_inv @ diff)
        df = len(common_vars)
        pvalue = 1 - stats.chi2.cdf(hausman_stat, df)
        
        interpretation = (
            "Random effects is appropriate (p >= 0.05)" if pvalue >= 0.05
            else "Fixed effects is preferred (p < 0.05, reject RE)"
        )
        
        self.hausman_results = {
            'hausman_statistic': hausman_stat,
            'pvalue': pvalue,
            'degrees_of_freedom': df,
            'null_hypothesis': 'Random effects is appropriate',
            'interpretation': interpretation
        }
        
        return self.hausman_results
    
    def summary(self) -> str:
        """Generate regression summary table.
        
        Returns:
            Formatted summary string
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return str(self.results.summary)
    
    def get_residuals(self) -> pd.Series:
        """Get regression residuals.
        
        Returns:
            Series of residuals (indexed by entity and time)
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return self.results.resids

