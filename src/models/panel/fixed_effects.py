"""Fixed effects panel data estimation."""

from typing import Optional, List, Dict
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm


class FixedEffects:
    """Fixed effects panel data estimator with clustered standard errors.
    
    Estimates panel data models with entity and/or time fixed effects.
    Standard errors are clustered at the entity level by default.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        covariates: List[str],
        entity: str,
        time: str,
        entity_effects: bool = True,
        time_effects: bool = True,
        cluster_se: bool = True
    ):
        """Initialize fixed effects model.
        
        Args:
            data: Panel data DataFrame
            outcome: Name of outcome variable
            covariates: List of covariate variable names
            entity: Name of entity (unit) identifier variable
            time: Name of time period variable
            entity_effects: If True, include entity fixed effects
            time_effects: If True, include time fixed effects
            cluster_se: If True, cluster standard errors at entity level
        """
        self.data = data.copy()  # Preserve original data
        self.outcome = outcome
        self.covariates = covariates
        self.entity = entity
        self.time = time
        self.entity_effects = entity_effects
        self.time_effects = time_effects
        self.cluster_se = cluster_se
        self.results = None
        
        # Validate required columns
        required_cols = [outcome, entity, time] + covariates
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Set up panel index
        self.data = self.data.set_index([entity, time])
    
    def estimate(self) -> Dict[str, np.ndarray]:
        """Estimate fixed effects model.
        
        Estimates: Y_it = X_it'β + α_i + γ_t + ε_it
        Where α_i are entity fixed effects and γ_t are time fixed effects.
        
        Returns:
            Dictionary containing:
                - coefficients: Estimated coefficients
                - std_errors: Standard errors
                - pvalues: P-values
                - rsquared: R-squared
                - rsquared_within: Within R-squared
                - nobs: Number of observations
        """
        # Prepare data
        y = self.data[self.outcome]
        X = self.data[self.covariates]
        
        # Drop missing values
        model_data = pd.concat([y, X], axis=1).dropna()
        y = model_data[self.outcome]
        X = model_data[self.covariates]
        
        # Estimate with linearmodels PanelOLS
        # Note: linearmodels handles fixed effects efficiently
        model = PanelOLS(
            dependent=y,
            exog=X,
            entity_effects=self.entity_effects,
            time_effects=self.time_effects
        )
        
        if self.cluster_se:
            self.results = model.fit(cov_type='clustered', cluster_entity=True)
        else:
            self.results = model.fit()
        
        # Extract results
        return {
            'coefficients': self.results.params.values,
            'std_errors': self.results.std_errors.values,
            'pvalues': self.results.pvalues.values,
            'rsquared': float(self.results.rsquared),
            'rsquared_within': float(self.results.rsquared_within),
            'nobs': int(self.results.nobs),
            'nentities': int(self.results.entity_info.total),
            'ntime': int(self.results.time_info.total)
        }
    
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

