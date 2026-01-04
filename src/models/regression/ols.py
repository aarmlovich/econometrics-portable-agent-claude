"""Ordinary Least Squares (OLS) regression with robust standard errors."""

from typing import Optional, List, Dict, Literal, Any
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
import matplotlib.pyplot as plt

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class OLSRegression(BaseEconometricModel):
    """OLS regression with robust standard errors and diagnostics.

    This class provides OLS estimation with heteroskedasticity-robust
    standard errors by default. Supports HC1, HC2, and HC3 (jackknife)
    standard errors with automatic selection based on observations per regressor.

    References:
    - MacKinnon and White (1985): HC3 preferred for small samples
    - Long and Ervin (2000): HC variants converge with ≥250 obs/regressor
    """

    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        covariates: List[str],
        hc_type: Literal['HC1', 'HC2', 'HC3', 'auto'] = 'HC1',
        constant: bool = True
    ):
        """Initialize OLS regression model.

        Args:
            data: DataFrame containing outcome and covariate variables
            outcome: Name of outcome variable
            covariates: List of covariate variable names
            hc_type: Type of heteroskedasticity-consistent standard errors.
                     Options: 'HC1' (default, Stata standard), 'HC2' (leverage-adjusted),
                     'HC3' (jackknife, preferred for small samples), 'auto' (select based on n/k ratio)
            constant: If True, include intercept term
        """
        super().__init__(data=data, outcome=outcome)
        self.covariates = covariates
        self.hc_type = hc_type
        self.constant = constant
        self.model = None
        self._X_used = None  # Store X matrix for leverage calculations
        self._hc_type_used = None  # Store the actual HC type used

        # Validate data
        required_cols = [outcome] + covariates
        self._validate_columns(required_cols)

        # Check for sufficient observations
        if len(data) < len(covariates) + (1 if constant else 0) + 1:
            raise ValueError(
                "Insufficient observations for number of parameters"
            )

    def _select_hc_type(self, n: int, k: int) -> str:
        """Automatically select HC type based on observations per regressor.

        Selection rule (based on Long and Ervin 2000, MacKinnon and White 1985):
        - n/k >= 250: HC1 (standard practice)
        - 100 <= n/k < 250: HC2 (leverage-adjusted)
        - n/k < 100: HC3 (jackknife, preferred for small samples)

        Reference: Wooldridge, Ch. 4, Section 4.2.3, p.57-58 discusses
        heteroskedasticity-robust inference and HC variants.

        Args:
            n: Number of observations
            k: Number of regressors (including constant if present)

        Returns:
            Selected HC type: 'HC1', 'HC2', or 'HC3'
        """
        obs_per_regressor = n / k

        # Threshold: n/k < 100 suggests HC3 for better small-sample properties
        # Reference: Wooldridge, Ch. 4, p.57-58
        if obs_per_regressor >= 250:
            return 'HC1'
        elif obs_per_regressor >= 100:
            return 'HC2'
        else:
            return 'HC3'

    def estimate(self) -> EstimationResult:
        """Estimate OLS regression.

        Returns:
            EstimationResult with:
                - coefficients: Named coefficient estimates
                - std_errors: Named standard errors
                - pvalues: Named p-values
                - tvalues: Named t-statistics
                - ci_lower/ci_upper: Named confidence intervals
                - nobs: Number of observations
                - fit_stats: rsquared, rsquared_adj, obs_per_regressor
                - diagnostics: hc_type used
        """
        # Prepare data
        y = self.data[self.outcome].dropna()
        X = self.data[self.covariates].dropna()

        # Align indices (drop missing in both)
        common_idx = y.index.intersection(X.index)
        y = y.loc[common_idx]
        X = X.loc[common_idx]

        # Add constant if requested
        if self.constant:
            X = add_constant(X)

        # Store X for leverage calculations
        self._X_used = X.values if isinstance(X, pd.DataFrame) else X

        # Determine HC type (auto-select if requested)
        hc_type_to_use = self.hc_type
        if hc_type_to_use == 'auto':
            n = len(y)
            k = X.shape[1]
            hc_type_to_use = self._select_hc_type(n, k)
        self._hc_type_used = hc_type_to_use

        # Estimate model
        self.model = OLS(y, X)

        # Fit with appropriate covariance type
        if hc_type_to_use in ['HC1', 'HC2', 'HC3']:
            self.results = self.model.fit(cov_type=hc_type_to_use)
        else:
            self.results = self.model.fit()

        self._estimated = True

        # Calculate observations per regressor
        n_obs = int(self.results.nobs)
        k_params = len(self.results.params)
        obs_per_regressor = n_obs / k_params

        # Get parameter names
        param_names = list(self.results.params.index)

        # Build confidence intervals
        conf_int = self.results.conf_int()

        # Create standardized result
        return create_estimation_result(
            coefficients={name: float(self.results.params[name]) for name in param_names},
            std_errors={name: float(self.results.bse[name]) for name in param_names},
            pvalues={name: float(self.results.pvalues[name]) for name in param_names},
            tvalues={name: float(self.results.tvalues[name]) for name in param_names},
            ci_lower={name: float(conf_int.loc[name, 0]) for name in param_names},
            ci_upper={name: float(conf_int.loc[name, 1]) for name in param_names},
            nobs=n_obs,
            model_type='ols',
            fit_stats={
                'rsquared': float(self.results.rsquared),
                'rsquared_adj': float(self.results.rsquared_adj),
                'obs_per_regressor': float(obs_per_regressor),
            },
            diagnostics={
                'hc_type': hc_type_to_use,
            }
        )

    def summary(self) -> str:
        """Generate regression summary table.

        Returns:
            Formatted summary string
        """
        self._check_estimated()
        return str(self.results.summary())

    def get_residuals(self) -> pd.Series:
        """Get regression residuals.

        Returns:
            Series of residuals
        """
        self._check_estimated()
        return self.results.resid

    def get_fitted_values(self) -> pd.Series:
        """Get fitted values.

        Returns:
            Series of fitted values
        """
        self._check_estimated()
        return self.results.fittedvalues

    def get_leverage(self) -> np.ndarray:
        """Get leverage values (hat matrix diagonal elements).

        Leverage measures how much influence each observation has on the
        regression fit. Mean leverage = k/n (regressors/observations).
        High leverage: > 2*(k/n) or close to 1.

        Returns:
            Array of leverage values (h_ii)
        """
        self._check_estimated()

        if self._X_used is None:
            raise ValueError("X matrix not available for leverage calculation.")

        # Calculate hat matrix: H = X(X'X)^{-1}X'
        X = self._X_used
        XtX_inv = np.linalg.inv(X.T @ X)
        H = X @ XtX_inv @ X.T
        leverage = np.diag(H)

        return leverage

    def get_leverage_statistics(self) -> Dict[str, Any]:
        """Get leverage statistics for diagnostics.

        Returns:
            Dictionary with:
                - mean_leverage: Mean leverage (should equal k/n)
                - max_leverage: Maximum leverage
                - high_leverage_count: Number of observations with leverage > 2*(k/n)
                - high_leverage_pct: Percentage with high leverage
                - obs_per_regressor: Observations per regressor ratio
                - recommendation: Recommended HC type based on leverage
        """
        self._check_estimated()

        leverage = self.get_leverage()
        n = len(leverage)
        k = len(self.results.params)

        mean_leverage = np.mean(leverage)
        max_leverage = np.max(leverage)
        threshold = 2 * (k / n)
        high_leverage_count = np.sum(leverage > threshold)
        high_leverage_pct = (high_leverage_count / n) * 100
        obs_per_regressor = n / k

        # Recommendation based on leverage
        if max_leverage > 0.9:
            recommendation = "HC3 (very high leverage detected)"
        elif max_leverage > threshold or high_leverage_pct > 5:
            recommendation = "HC2 or HC3 (high leverage present)"
        elif obs_per_regressor < 100:
            recommendation = "HC3 (small sample: n/k < 100)"
        elif obs_per_regressor < 250:
            recommendation = "HC2 (moderate sample: 100 <= n/k < 250)"
        else:
            recommendation = "HC1 (large sample: n/k >= 250)"

        return {
            'mean_leverage': float(mean_leverage),
            'max_leverage': float(max_leverage),
            'high_leverage_threshold': float(threshold),
            'high_leverage_count': int(high_leverage_count),
            'high_leverage_pct': float(high_leverage_pct),
            'obs_per_regressor': float(obs_per_regressor),
            'recommendation': recommendation
        }

    def plot_residuals(
        self,
        ax: Optional[List[plt.Axes]] = None,
        figsize: tuple = (12, 5)
    ) -> plt.Figure:
        """Plot residual diagnostics.

        Creates two plots:
        1. Residuals vs Fitted Values (check for heteroskedasticity and patterns)
        2. Normal Q-Q Plot (check for normality of residuals)

        Args:
            ax: Optional list of 2 matplotlib axes to plot on
            figsize: Figure size in inches

        Returns:
            Matplotlib figure with two subplots
        """
        from src.visualization.plots import plot_residuals
        return plot_residuals(self, ax=ax, figsize=figsize)
