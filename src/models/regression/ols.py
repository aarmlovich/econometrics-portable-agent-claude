"""Ordinary Least Squares (OLS) regression with robust standard errors."""

from typing import Optional, List, Tuple, Dict, Literal
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
import statsmodels.api as sm


class OLSRegression:
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
        self.data = data.copy()  # Preserve original data
        self.outcome = outcome
        self.covariates = covariates
        self.hc_type = hc_type
        self.constant = constant
        self.model = None
        self.results = None
        self._X_used = None  # Store X matrix for leverage calculations
        
        # Validate data
        required_cols = [outcome] + covariates
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        
        # Check for sufficient observations
        if len(data) < len(covariates) + (1 if constant else 0) + 1:
            raise ValueError(
                "Insufficient observations for number of parameters"
            )
    
    def _select_hc_type(self, n: int, k: int) -> str:
        """Automatically select HC type based on observations per regressor.
        
        Selection rule (based on Long and Ervin 2000, MacKinnon and White 1985):
        - n/k ≥ 250: HC1 (standard practice)
        - 100 ≤ n/k < 250: HC2 (leverage-adjusted)
        - n/k < 100: HC3 (jackknife, preferred for small samples)
        
        Args:
            n: Number of observations
            k: Number of regressors (including constant if present)
            
        Returns:
            Selected HC type: 'HC1', 'HC2', or 'HC3'
        """
        obs_per_regressor = n / k
        
        if obs_per_regressor >= 250:
            return 'HC1'
        elif obs_per_regressor >= 100:
            return 'HC2'
        else:
            return 'HC3'
    
    def estimate(self) -> Dict[str, np.ndarray]:
        """Estimate OLS regression.
        
        Returns:
            Dictionary containing:
                - coefficients: Estimated coefficients
                - std_errors: Standard errors
                - pvalues: P-values
                - tvalues: T-statistics
                - rsquared: R-squared
                - rsquared_adj: Adjusted R-squared
                - nobs: Number of observations
                - hc_type: Type of HC standard errors used
                - obs_per_regressor: Observations per regressor ratio
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
        
        # Estimate model
        self.model = OLS(y, X)
        
        # Fit with appropriate covariance type
        if hc_type_to_use in ['HC1', 'HC2', 'HC3']:
            self.results = self.model.fit(cov_type=hc_type_to_use)
        else:
            # Homoskedastic (no robust SE) - should not happen with valid hc_type
            self.results = self.model.fit()
        
        # Calculate observations per regressor
        n_obs = int(self.results.nobs)
        k_params = len(self.results.params)
        obs_per_regressor = n_obs / k_params
        
        # Extract results
        return {
            'coefficients': self.results.params.values,
            'std_errors': self.results.bse.values,
            'pvalues': self.results.pvalues.values,
            'tvalues': self.results.tvalues.values,
            'rsquared': self.results.rsquared,
            'rsquared_adj': self.results.rsquared_adj,
            'nobs': n_obs,
            'hc_type': hc_type_to_use,
            'obs_per_regressor': obs_per_regressor
        }
    
    def summary(self) -> str:
        """Generate regression summary table.
        
        Returns:
            Formatted summary string
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return str(self.results.summary())
    
    def get_residuals(self) -> pd.Series:
        """Get regression residuals.
        
        Returns:
            Series of residuals
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return self.results.resid
    
    def get_fitted_values(self) -> pd.Series:
        """Get fitted values.
        
        Returns:
            Series of fitted values
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        return self.results.fittedvalues
    
    def get_leverage(self) -> np.ndarray:
        """Get leverage values (hat matrix diagonal elements).
        
        Leverage measures how much influence each observation has on the
        regression fit. Mean leverage = k/n (regressors/observations).
        High leverage: > 2*(k/n) or close to 1.
        
        Returns:
            Array of leverage values (h_ii)
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        if self._X_used is None:
            raise ValueError("X matrix not available for leverage calculation.")
        
        # Calculate hat matrix: H = X(X'X)^{-1}X'
        X = self._X_used
        XtX_inv = np.linalg.inv(X.T @ X)
        H = X @ XtX_inv @ X.T
        leverage = np.diag(H)
        
        return leverage
    
    def get_leverage_statistics(self) -> Dict[str, float]:
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
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
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
            recommendation = "HC2 (moderate sample: 100 ≤ n/k < 250)"
        else:
            recommendation = "HC1 (large sample: n/k ≥ 250)"
        
        return {
            'mean_leverage': float(mean_leverage),
            'max_leverage': float(max_leverage),
            'high_leverage_threshold': float(threshold),
            'high_leverage_count': int(high_leverage_count),
            'high_leverage_pct': float(high_leverage_pct),
            'obs_per_regressor': float(obs_per_regressor),
            'recommendation': recommendation
        }

