"""Random effects panel data estimation."""

from typing import Optional, List, Dict, Any
import numpy as np
import pandas as pd
from linearmodels.panel import RandomEffects as LMRandomEffects
from scipy import stats
import warnings

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class RandomEffects(BaseEconometricModel):
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
        super().__init__(data=data, outcome=outcome)
        self.covariates = covariates
        self.entity = entity
        self.time = time
        self.cluster_se = cluster_se
        self.hausman_results = None

        # Validate required columns
        required_cols = [outcome, entity, time] + covariates
        self._validate_columns(required_cols)

        # Set up panel index
        self.data = self.data.set_index([entity, time])
        self.data = self.data.sort_index()
    
    def estimate(self) -> EstimationResult:
        """Estimate random effects model using GLS.

        Returns:
            EstimationResult with named coefficients and fit statistics
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

        self._estimated = True

        # Store parameter names for Hausman test
        self.param_names = list(self.results.params.index)

        # Build confidence intervals
        conf_int = self.results.conf_int()

        return create_estimation_result(
            coefficients={name: float(self.results.params[name]) for name in self.param_names},
            std_errors={name: float(self.results.std_errors[name]) for name in self.param_names},
            pvalues={name: float(self.results.pvalues[name]) for name in self.param_names},
            tvalues={name: float(self.results.tstats[name]) for name in self.param_names},
            ci_lower={name: float(conf_int.loc[name, 'lower']) for name in self.param_names},
            ci_upper={name: float(conf_int.loc[name, 'upper']) for name in self.param_names},
            nobs=int(self.results.nobs),
            model_type='re',
            fit_stats={
                'rsquared': float(self.results.rsquared),
                'rsquared_within': float(self.results.rsquared_within),
                'rsquared_between': float(self.results.rsquared_between),
                'nentities': int(self.results.entity_info.total),
                'ntime': int(self.results.time_info.total),
            },
            diagnostics={
                'cluster_se': self.cluster_se,
            }
        )
    
    def test_hausman(self, fe_results: Any) -> Dict[str, float]:
        """Test Hausman specification test (FE vs RE).

        Tests H0: Random effects is appropriate (unobserved heterogeneity
        is uncorrelated with regressors). If p < 0.05, reject H0 and use
        fixed effects instead.

        Reference: Wooldridge, Ch. 10, Section 10.7.3, p.291-300

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
                - citation: Wooldridge reference
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

        # Handle potential non-positive definite variance difference matrix
        # Use eigenvalue decomposition to ensure positive semi-definite
        try:
            # Try direct inverse first
            var_diff_inv = np.linalg.inv(var_diff)
            hausman_stat = float(diff.T @ var_diff_inv @ diff)

            # Hausman statistic should be non-negative (it's a quadratic form)
            # Negative values can occur due to numerical issues or when
            # FE variance < RE variance (which shouldn't happen asymptotically)
            if hausman_stat < 0:
                # Use absolute eigenvalues approach
                eigenvalues, eigenvectors = np.linalg.eigh(var_diff)
                # Replace negative eigenvalues with their absolute values
                eigenvalues_pos = np.abs(eigenvalues)
                eigenvalues_pos = np.maximum(eigenvalues_pos, 1e-10)  # Avoid division by zero
                var_diff_inv = eigenvectors @ np.diag(1 / eigenvalues_pos) @ eigenvectors.T
                hausman_stat = float(diff.T @ var_diff_inv @ diff)
                hausman_stat = abs(hausman_stat)  # Ensure non-negative
        except np.linalg.LinAlgError:
            # If singular, use pseudo-inverse with absolute eigenvalues
            eigenvalues, eigenvectors = np.linalg.eigh(var_diff)
            eigenvalues_pos = np.abs(eigenvalues)
            eigenvalues_pos = np.maximum(eigenvalues_pos, 1e-10)
            var_diff_inv = eigenvectors @ np.diag(1 / eigenvalues_pos) @ eigenvectors.T
            hausman_stat = float(abs(diff.T @ var_diff_inv @ diff))
        df = len(common_vars)
        pvalue = 1 - stats.chi2.cdf(hausman_stat, df)

        # Threshold: p < 0.05 rejects H0 (RE consistent)
        # Reference: Wooldridge, Ch. 10, Section 10.7.3, p.291-300
        interpretation = (
            "Random effects is appropriate (p >= 0.05, Wooldridge p.291)" if pvalue >= 0.05
            else "Fixed effects is preferred (p < 0.05, reject RE, Wooldridge p.291)"
        )

        self.hausman_results = {
            'hausman_statistic': hausman_stat,
            'pvalue': pvalue,
            'degrees_of_freedom': df,
            'null_hypothesis': 'Random effects is appropriate',
            'interpretation': interpretation,
            'citation': 'Wooldridge, Ch. 10, Section 10.7.3, p.291-300'
        }

        return self.hausman_results
    
    def summary(self) -> str:
        """Generate regression summary table.

        Returns:
            Formatted summary string
        """
        self._check_estimated()
        return str(self.results.summary)

    def get_residuals(self) -> pd.Series:
        """Get regression residuals.

        Returns:
            Series of residuals (indexed by entity and time)
        """
        self._check_estimated()
        return self.results.resids

