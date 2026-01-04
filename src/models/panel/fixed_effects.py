"""Fixed effects panel data estimation."""

from typing import Optional, List, Dict, Any
import numpy as np
import pandas as pd
from linearmodels.panel import PanelOLS
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class FixedEffects(BaseEconometricModel):
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
        super().__init__(data=data, outcome=outcome)
        self.covariates = covariates
        self.entity = entity
        self.time = time
        self.entity_effects = entity_effects
        self.time_effects = time_effects
        self.cluster_se = cluster_se

        # Validate required columns
        required_cols = [outcome, entity, time] + covariates
        self._validate_columns(required_cols)

        # Set up panel index
        self.data = self.data.set_index([entity, time])
    
    def estimate(self) -> EstimationResult:
        """Estimate fixed effects model.

        Estimates: Y_it = X_it'β + α_i + γ_t + ε_it
        Where α_i are entity fixed effects and γ_t are time fixed effects.

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

        # Estimate with linearmodels PanelOLS
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

        self._estimated = True

        # Get parameter names
        param_names = list(self.results.params.index)

        # Build confidence intervals
        conf_int = self.results.conf_int()

        return create_estimation_result(
            coefficients={name: float(self.results.params[name]) for name in param_names},
            std_errors={name: float(self.results.std_errors[name]) for name in param_names},
            pvalues={name: float(self.results.pvalues[name]) for name in param_names},
            tvalues={name: float(self.results.tstats[name]) for name in param_names},
            ci_lower={name: float(conf_int.loc[name, 'lower']) for name in param_names},
            ci_upper={name: float(conf_int.loc[name, 'upper']) for name in param_names},
            nobs=int(self.results.nobs),
            model_type='fe',
            fit_stats={
                'rsquared': float(self.results.rsquared),
                'rsquared_within': float(self.results.rsquared_within),
                'nentities': int(self.results.entity_info.total),
                'ntime': int(self.results.time_info.total),
            },
            diagnostics={
                'entity_effects': self.entity_effects,
                'time_effects': self.time_effects,
                'cluster_se': self.cluster_se,
            }
        )
    
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

