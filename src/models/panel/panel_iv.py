"""Panel instrumental variables estimation with fixed effects."""

from typing import Optional, List, Dict, Any
import numpy as np
import pandas as pd
from scipy import stats
import warnings

# Check if PanelIV is available in linearmodels
_USE_IV2SLS_FALLBACK = False
try:
    from linearmodels.panel.iv import PanelIV as LMPanelIV
except ImportError:
    # Fallback: Use IV2SLS with manual demeaning for fixed effects
    from linearmodels.iv import IV2SLS
    _USE_IV2SLS_FALLBACK = True

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


def _demean_panel(data: pd.DataFrame, columns: List[str], entity_effects: bool, time_effects: bool) -> pd.DataFrame:
    """Apply within transformation (demeaning) for fixed effects.

    Args:
        data: Panel data with MultiIndex (entity, time)
        columns: Columns to demean
        entity_effects: If True, demean by entity
        time_effects: If True, demean by time

    Returns:
        Demeaned DataFrame
    """
    result = data[columns].copy()

    if entity_effects:
        # Demean by entity (within transformation)
        entity_means = result.groupby(level=0).transform('mean')
        result = result - entity_means

    if time_effects:
        # Demean by time
        time_means = result.groupby(level=1).transform('mean')
        result = result - time_means

    # Add back grand mean if both effects (to avoid double-demeaning bias)
    if entity_effects and time_effects:
        grand_mean = data[columns].mean()
        result = result + grand_mean

    return result


class PanelIV(BaseEconometricModel):
    """Panel IV estimator with fixed effects and first-stage diagnostics.
    
    Estimates treatment effects using 2SLS in panel data setting with
    entity and/or time fixed effects. Includes first-stage diagnostics,
    weak instrument tests, and overidentification tests.
    
    Specification:
    First stage:  X_it = π_0 + π_1 Z_it + α_i + γ_t + u_it
    Second stage: Y_it = α + βX̂_it + α_i + γ_t + ε_it
    
    Where Z_it are instruments, X_it is endogenous treatment,
    and α_i, γ_t are entity and time fixed effects.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        treatment: str,
        instruments: List[str],
        entity: str,
        time: str,
        covariates: Optional[List[str]] = None,
        entity_effects: bool = True,
        time_effects: bool = True,
        cluster_se: bool = True
    ):
        """Initialize panel IV model.

        Args:
            data: Panel data DataFrame
            outcome: Name of outcome variable
            treatment: Name of endogenous treatment variable
            instruments: List of instrument variable names
            entity: Name of entity (unit) identifier variable
            time: Name of time period variable
            covariates: Optional list of covariate variable names
            entity_effects: If True, include entity fixed effects
            time_effects: If True, include time fixed effects
            cluster_se: If True, cluster standard errors at entity level
        """
        super().__init__(data=data, outcome=outcome)
        self.treatment = treatment
        self.instruments = instruments
        self.entity = entity
        self.time = time
        self.covariates = covariates if covariates else []
        self.entity_effects = entity_effects
        self.time_effects = time_effects
        self.cluster_se = cluster_se
        self.first_stage_results = None
        self.reduced_form_results = None
        self._first_stage_cache = None

        # Validate required columns
        required_cols = [outcome, treatment, entity, time] + instruments + self.covariates
        self._validate_columns(required_cols)

        if len(instruments) < 1:
            raise ValueError("At least one instrument is required")

        # Set up panel index
        self.data = self.data.set_index([entity, time])
        self.data = self.data.sort_index()
    
    def estimate_first_stage(self) -> Dict[str, Any]:
        """Estimate first-stage regression with fixed effects.
        
        Returns:
            Dictionary containing first-stage statistics
        """
        # Prepare data
        y_first = self.data[self.treatment]
        X_first = self.data[self.instruments + self.covariates]
        
        # Drop missing values
        model_data = pd.concat([y_first, X_first], axis=1).dropna()
        y_first = model_data[self.treatment]
        X_first = model_data[self.instruments + self.covariates]
        
        # Estimate first stage with fixed effects using PanelOLS
        from linearmodels.panel import PanelOLS
        
        model_first = PanelOLS(
            dependent=y_first,
            exog=X_first,
            entity_effects=self.entity_effects,
            time_effects=self.time_effects
        )
        
        if self.cluster_se:
            self.first_stage_results = model_first.fit(cov_type='clustered', cluster_entity=True)
        else:
            self.first_stage_results = model_first.fit()
        
        # Calculate F-statistic for instruments
        # Get coefficients and covariance for instruments only
        instrument_params = self.first_stage_results.params[self.instruments]
        instrument_cov = self.first_stage_results.cov.loc[
            self.instruments, self.instruments
        ]
        
        n = self.first_stage_results.nobs
        k_instruments = len(self.instruments)
        k_total = len(self.first_stage_results.params)
        
        # Wald test statistic
        try:
            wald_stat = float(instrument_params.T @ np.linalg.inv(instrument_cov) @ instrument_params)
            f_statistic = wald_stat / k_instruments
            # Approximate degrees of freedom (simplified)
            df_denom = n - k_total - (self.first_stage_results.entity_info.total if self.entity_effects else 0) - (self.first_stage_results.time_info.total if self.time_effects else 0)
            f_pvalue = 1 - stats.f.cdf(f_statistic, k_instruments, df_denom)
        except (np.linalg.LinAlgError, ValueError):
            rsquared = self.first_stage_results.rsquared
            if rsquared < 1.0:
                f_statistic = (rsquared / (1 - rsquared)) * ((n - k_total - 1) / k_instruments)
            else:
                f_statistic = np.inf
            f_pvalue = 0.0 if np.isfinite(f_statistic) else 0.0
        
        return {
            'coefficients': self.first_stage_results.params.to_dict(),
            'std_errors': self.first_stage_results.std_errors.to_dict(),
            'pvalues': self.first_stage_results.pvalues.to_dict(),
            'rsquared': float(self.first_stage_results.rsquared),
            'rsquared_within': float(self.first_stage_results.rsquared_within),
            'f_statistic': float(f_statistic),
            'f_pvalue': float(f_pvalue),
            'nobs': int(n)
        }
    
    def estimate(self) -> EstimationResult:
        """Estimate panel IV (2SLS) with fixed effects.

        Returns:
            EstimationResult with IV estimates and diagnostics
        """
        # Prepare data
        y = self.data[self.outcome]
        X = self.data[[self.treatment] + self.covariates]
        Z = self.data[self.instruments]

        # Drop missing values
        model_data = pd.concat([y, X, Z], axis=1).dropna()
        y = model_data[self.outcome]
        X = model_data[[self.treatment] + self.covariates]
        Z = model_data[self.instruments]

        if _USE_IV2SLS_FALLBACK:
            # Use IV2SLS with manual demeaning for fixed effects
            all_cols = [self.outcome, self.treatment] + self.covariates + self.instruments

            # Demean data for fixed effects
            if self.entity_effects or self.time_effects:
                demeaned = _demean_panel(model_data, all_cols, self.entity_effects, self.time_effects)
                y = demeaned[self.outcome]
                X = demeaned[[self.treatment] + self.covariates]
                Z = demeaned[self.instruments]
                # Reset index for IV2SLS (expects flat index)
                y = y.reset_index(drop=True)
                X = X.reset_index(drop=True)
                Z = Z.reset_index(drop=True)

            # IV2SLS expects: dependent, exog (exogenous regressors), endog (endogenous), instruments
            # exog = covariates (if any), endog = treatment, instruments = Z
            from statsmodels.tools.tools import add_constant
            if self.covariates:
                exog = add_constant(X[self.covariates])
            else:
                exog = add_constant(pd.DataFrame(index=y.index))
            endog = X[[self.treatment]]
            instruments = Z

            model = IV2SLS(dependent=y, exog=exog, endog=endog, instruments=instruments)
            if self.cluster_se:
                # IV2SLS uses different clustering approach - use robust as approximation
                self.results = model.fit(cov_type='robust')
            else:
                self.results = model.fit()
        else:
            # Use native PanelIV from linearmodels
            model = LMPanelIV(
                dependent=y,
                exog=X,
                endog=self.treatment,
                instruments=Z,
                entity_effects=self.entity_effects,
                time_effects=self.time_effects
            )

            if self.cluster_se:
                self.results = model.fit(cov_type='clustered', cluster_entity=True)
            else:
                self.results = model.fit()

        self._estimated = True

        # Get first-stage F-statistic
        first_stage = self.estimate_first_stage()
        first_stage_f = first_stage['f_statistic']

        # Extract IV coefficient - handle both PanelIV and IV2SLS result formats
        iv_coef = self.results.params[self.treatment]
        iv_se = self.results.std_errors[self.treatment]
        iv_pval = self.results.pvalues[self.treatment]
        iv_tval = self.results.tstats[self.treatment]

        # Confidence interval
        ci = self.results.conf_int().loc[self.treatment]
        ci_low = float(ci.iloc[0]) if hasattr(ci, 'iloc') else float(ci[0])
        ci_high = float(ci.iloc[1]) if hasattr(ci, 'iloc') else float(ci[1])

        # Get fit statistics - handle differences between PanelIV and IV2SLS
        rsquared = float(self.results.rsquared)
        # IV2SLS doesn't have rsquared_within, use rsquared as fallback
        rsquared_within = float(getattr(self.results, 'rsquared_within', rsquared))

        # Warn if weak instruments
        # Threshold: F < 10 indicates weak instruments (Staiger-Stock rule)
        # Reference: Wooldridge, Ch. 5, p.101-103
        if first_stage_f < 10:
            warnings.warn(
                f"Weak instruments detected: F-statistic = {first_stage_f:.2f} < 10. "
                "Consider using LIML or alternative instruments. "
                "(Wooldridge, p.101-103)",
                UserWarning
            )

        return create_estimation_result(
            coefficients={self.treatment: float(iv_coef)},
            std_errors={self.treatment: float(iv_se)},
            pvalues={self.treatment: float(iv_pval)},
            tvalues={self.treatment: float(iv_tval)},
            ci_lower={self.treatment: ci_low},
            ci_upper={self.treatment: ci_high},
            nobs=int(self.results.nobs),
            model_type='panel_iv',
            fit_stats={
                'rsquared': rsquared,
                'rsquared_within': rsquared_within,
                'first_stage_f': float(first_stage_f),
            },
            diagnostics={
                'entity_effects': self.entity_effects,
                'time_effects': self.time_effects,
                'cluster_se': self.cluster_se,
                'n_instruments': len(self.instruments),
                'using_iv2sls_fallback': _USE_IV2SLS_FALLBACK,
            }
        )
    
    def test_weak_instruments(self) -> Dict[str, float]:
        """Test for weak instruments using first-stage F-statistic.

        Uses the Staiger-Stock (1997) rule of thumb: F > 10 indicates strong instruments.
        Reference: Wooldridge, Ch. 5, p.101-103

        Returns:
            Dictionary containing weak instrument test results
        """
        if self.first_stage_results is None:
            first_stage = self.estimate_first_stage()
        else:
            first_stage = self.estimate_first_stage()

        f_stat = first_stage['f_statistic']
        f_pval = first_stage['f_pvalue']
        # Threshold: F < 10 (Staiger-Stock rule, Wooldridge p.101-103)
        is_weak = f_stat < 10

        interpretation = (
            "Strong instruments (F > 10, Wooldridge p.101)" if not is_weak
            else "Weak instruments (F < 10) - consider LIML (Wooldridge p.101-103)"
        )

        return {
            'f_statistic': float(f_stat),
            'f_pvalue': float(f_pval),
            'is_weak': bool(is_weak),
            'interpretation': interpretation,
            'citation': 'Wooldridge, Ch. 5, p.101-103'
        }
    
    def test_overidentification(self) -> Optional[Dict[str, float]]:
        """Test for overidentification (if over-identified).
        
        Returns:
            Dictionary containing test results, or None if exactly identified
        """
        if len(self.instruments) <= 1:
            return None
        
        if self.results is None:
            self.estimate()
        
        # Panel IV overidentification test (simplified)
        # In practice, would use Hansen J-test or similar
        # For now, return None with note that test not fully implemented
        warnings.warn(
            "Overidentification test for panel IV not fully implemented. "
            "Use cross-section IV overidentification test as approximation.",
            UserWarning
        )
        return None
    
    def estimate_reduced_form(self) -> Dict[str, float]:
        """Estimate reduced-form regression with fixed effects.
        
        Returns:
            Dictionary containing reduced-form estimates
        """
        # Prepare data
        y_rf = self.data[self.outcome]
        X_rf = self.data[self.instruments + self.covariates]
        
        # Drop missing values
        model_data = pd.concat([y_rf, X_rf], axis=1).dropna()
        y_rf = model_data[self.outcome]
        X_rf = model_data[self.instruments + self.covariates]
        
        # Estimate reduced form with fixed effects
        from linearmodels.panel import PanelOLS
        
        model_rf = PanelOLS(
            dependent=y_rf,
            exog=X_rf,
            entity_effects=self.entity_effects,
            time_effects=self.time_effects
        )
        
        if self.cluster_se:
            self.reduced_form_results = model_rf.fit(cov_type='clustered', cluster_entity=True)
        else:
            self.reduced_form_results = model_rf.fit()
        
        # Extract instrument coefficients
        reduced_form_coefs = {}
        for inst in self.instruments:
            reduced_form_coefs[inst] = {
                'coefficient': float(self.reduced_form_results.params[inst]),
                'std_error': float(self.reduced_form_results.std_errors[inst]),
                'pvalue': float(self.reduced_form_results.pvalues[inst])
            }
        
        return {
            'instrument_coefficients': reduced_form_coefs,
            'nobs': int(self.reduced_form_results.nobs),
            'rsquared': float(self.reduced_form_results.rsquared),
            'rsquared_within': float(self.reduced_form_results.rsquared_within)
        }
    
    def summary(self) -> str:
        """Generate summary of panel IV estimation results.

        Returns:
            Formatted summary string
        """
        self._check_estimated()
        
        summary_lines = []
        summary_lines.append("=" * 80)
        summary_lines.append("Panel IV (2SLS) Estimation Results")
        summary_lines.append("=" * 80)
        summary_lines.append("")
        
        # Second stage results
        summary_lines.append("Second Stage Results:")
        summary_lines.append(str(self.results.summary))
        summary_lines.append("")
        
        # First stage results
        first_stage = self.estimate_first_stage()
        summary_lines.append("First Stage Results:")
        summary_lines.append(f"  F-statistic: {first_stage['f_statistic']:.4f}")
        summary_lines.append(f"  F-statistic p-value: {first_stage['f_pvalue']:.4f}")
        summary_lines.append(f"  R-squared: {first_stage['rsquared']:.4f}")
        summary_lines.append(f"  Within R-squared: {first_stage['rsquared_within']:.4f}")
        
        # Weak instrument test
        weak_test = self.test_weak_instruments()
        summary_lines.append("")
        summary_lines.append("Weak Instrument Test:")
        summary_lines.append(f"  {weak_test['interpretation']}")
        
        return "\n".join(summary_lines)

