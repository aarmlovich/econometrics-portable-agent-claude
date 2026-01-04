"""Instrumental variables estimation with diagnostics."""

from typing import Optional, List, Dict, Literal, Any
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
from scipy import stats
import warnings

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class InstrumentalVariables(BaseEconometricModel):
    """Instrumental variables (IV) estimator with first-stage diagnostics.
    
    Estimates treatment effects using 2SLS (two-stage least squares)
    with comprehensive diagnostics including first-stage statistics,
    weak instrument tests, and overidentification tests.
    
    Specification:
    First stage:  X_i = π_0 + π_1 Z_i + u_i
    Second stage: Y_i = α + βX̂_i + ε_i
    
    Where Z_i are instruments and X_i is the endogenous treatment.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        treatment: str,
        instruments: List[str],
        covariates: Optional[List[str]] = None,
        hc_type: Literal['HC1', 'HC2', 'HC3'] = 'HC1'
    ):
        """Initialize instrumental variables model.

        Args:
            data: DataFrame containing outcome, treatment, instruments, and covariates
            outcome: Name of outcome variable
            treatment: Name of endogenous treatment variable
            instruments: List of instrument variable names
            covariates: Optional list of covariate variable names
            hc_type: Type of heteroskedasticity-consistent standard errors
        """
        super().__init__(data=data, outcome=outcome)
        self.treatment = treatment
        self.instruments = instruments
        self.covariates = covariates if covariates else []
        self.hc_type = hc_type
        self.first_stage_results = None
        self.reduced_form_results = None
        self._first_stage_cache = None  # Cache first-stage results

        # Validate required columns
        required_cols = [outcome, treatment] + instruments + self.covariates
        self._validate_columns(required_cols)

        if len(instruments) < 1:
            raise ValueError("At least one instrument is required")
    
    def estimate_first_stage(self) -> Dict[str, Any]:
        """Estimate first-stage regression.

        First stage: Treatment = f(Instruments, Covariates)

        Returns:
            Dictionary containing:
                - coefficients: First-stage coefficients
                - std_errors: Standard errors
                - pvalues: P-values
                - rsquared: R-squared
                - f_statistic: F-statistic for instruments
                - f_pvalue: F-statistic p-value
                - nobs: Number of observations
        """
        # Return cached result if available
        if self._first_stage_cache is not None:
            return self._first_stage_cache

        # Prepare data
        y_first = self.data[self.treatment].dropna()
        X_first = self.data[self.instruments + self.covariates].dropna()

        # Align indices
        common_idx = y_first.index.intersection(X_first.index)
        y_first = y_first.loc[common_idx]
        X_first = X_first.loc[common_idx]

        # Add constant
        X_first = add_constant(X_first)

        # Estimate first stage
        model_first = OLS(y_first, X_first)
        self.first_stage_results = model_first.fit(cov_type=self.hc_type)

        # Calculate F-statistic for instruments (joint significance)
        n = self.first_stage_results.nobs
        k_instruments = len(self.instruments)
        k_total = len(self.first_stage_results.params) - 1  # Excluding constant
        k_exog = k_total

        # R-squared from first stage
        rsquared = self.first_stage_results.rsquared

        # F-statistic for instruments (Wald test)
        instrument_params = self.first_stage_results.params[self.instruments]
        instrument_cov = self.first_stage_results.cov_params().loc[
            self.instruments, self.instruments
        ]

        # Wald test statistic: β' * (Var(β))^{-1} * β ~ χ²(k_instruments)
        try:
            wald_stat = float(instrument_params.T @ np.linalg.inv(instrument_cov) @ instrument_params)
            f_statistic = wald_stat / k_instruments
            f_pvalue = 1 - stats.f.cdf(f_statistic, k_instruments, n - k_exog - 1)
        except (np.linalg.LinAlgError, ValueError):
            # Fallback: use R-squared formula
            if rsquared < 1.0:
                f_statistic = (rsquared / (1 - rsquared)) * ((n - k_exog - 1) / k_instruments)
            else:
                f_statistic = np.inf
            f_pvalue = 1 - stats.f.cdf(f_statistic, k_instruments, n - k_exog - 1) if np.isfinite(f_statistic) else 0.0

        # Cache result
        self._first_stage_cache = {
            'coefficients': self.first_stage_results.params.to_dict(),
            'std_errors': self.first_stage_results.bse.to_dict(),
            'pvalues': self.first_stage_results.pvalues.to_dict(),
            'rsquared': float(rsquared),
            'f_statistic': float(f_statistic),
            'f_pvalue': float(f_pvalue),
            'nobs': int(n)
        }
        return self._first_stage_cache
    
    def estimate(self) -> EstimationResult:
        """Estimate 2SLS (two-stage least squares).

        Returns:
            EstimationResult with:
                - coefficients: {treatment: IV estimate}
                - std_errors: {treatment: standard error}
                - pvalues: {treatment: p-value}
                - ci_lower/ci_upper: Confidence intervals
                - nobs: Number of observations
                - fit_stats: rsquared, first_stage_f, first_stage_rsquared
                - diagnostics: hc_type, n_instruments, is_overidentified
        """
        # Estimate first stage if not already done
        first_stage = self.estimate_first_stage()

        # Get first-stage fitted values (predicted treatment)
        y_first = self.data[self.treatment].dropna()
        X_first = self.data[self.instruments + self.covariates].dropna()
        common_idx = y_first.index.intersection(X_first.index)
        X_first_aligned = add_constant(X_first.loc[common_idx])
        treatment_predicted = self.first_stage_results.fittedvalues

        # Prepare second stage
        y_second = self.data[self.outcome].loc[common_idx].dropna()
        X_second = pd.concat([
            treatment_predicted,
            X_first_aligned[self.covariates] if self.covariates else pd.DataFrame(index=common_idx)
        ], axis=1)
        X_second.columns = [self.treatment] + self.covariates if self.covariates else [self.treatment]
        X_second = add_constant(X_second)

        # Align indices
        common_idx_second = y_second.index.intersection(X_second.index)
        y_second = y_second.loc[common_idx_second]
        X_second = X_second.loc[common_idx_second]

        # Estimate second stage
        model_second = OLS(y_second, X_second)
        self.results = model_second.fit(cov_type=self.hc_type)
        self._estimated = True

        # Extract IV coefficient (treatment effect)
        iv_coef = self.results.params[self.treatment]
        iv_se = self.results.bse[self.treatment]
        iv_pval = self.results.pvalues[self.treatment]
        iv_tval = self.results.tvalues[self.treatment]

        # Confidence interval
        ci = self.results.conf_int().loc[self.treatment]

        # Get first-stage F-statistic
        first_stage_f = first_stage['f_statistic']

        # Warn if weak instruments
        if first_stage_f < 10:
            warnings.warn(
                f"Weak instruments detected: F-statistic = {first_stage_f:.2f} < 10. "
                "Consider using LIML or alternative instruments.",
                UserWarning
            )

        return create_estimation_result(
            coefficients={self.treatment: float(iv_coef)},
            std_errors={self.treatment: float(iv_se)},
            pvalues={self.treatment: float(iv_pval)},
            tvalues={self.treatment: float(iv_tval)},
            ci_lower={self.treatment: float(ci[0])},
            ci_upper={self.treatment: float(ci[1])},
            nobs=int(self.results.nobs),
            model_type='iv',
            fit_stats={
                'rsquared': float(self.results.rsquared),
                'first_stage_f': float(first_stage_f),
                'first_stage_rsquared': float(first_stage['rsquared']),
            },
            diagnostics={
                'hc_type': self.hc_type,
                'n_instruments': len(self.instruments),
                'is_overidentified': len(self.instruments) > 1,
            }
        )
    
    def test_weak_instruments(self) -> Dict[str, float]:
        """Test for weak instruments.
        
        Uses first-stage F-statistic. Rule of thumb: F > 10 suggests
        strong instruments, F < 10 suggests weak instruments.
        
        Returns:
            Dictionary containing:
                - f_statistic: First-stage F-statistic
                - f_pvalue: F-statistic p-value
                - is_weak: Boolean (True if F < 10)
                - interpretation: Text interpretation
        """
        if self.first_stage_results is None:
            first_stage = self.estimate_first_stage()
        else:
            first_stage = self.estimate_first_stage()
        
        f_stat = first_stage['f_statistic']
        f_pval = first_stage['f_pvalue']
        is_weak = f_stat < 10
        
        interpretation = (
            "Strong instruments (F > 10)" if not is_weak
            else "Weak instruments (F < 10) - consider LIML or alternative instruments"
        )
        
        return {
            'f_statistic': float(f_stat),
            'f_pvalue': float(f_pval),
            'is_weak': bool(is_weak),
            'interpretation': interpretation
        }
    
    def test_overidentification(self) -> Optional[Dict[str, float]]:
        """Test for overidentification (Sargan test).
        
        Only applicable when number of instruments > number of endogenous variables.
        Tests H0: Instruments are valid (uncorrelated with error term).
        
        Returns:
            Dictionary containing test results, or None if exactly identified
        """
        if len(self.instruments) <= 1:  # Exactly identified
            return None
        
        if self.results is None:
            self.estimate()
        
        # Sargan test: n * R² from regression of residuals on all instruments
        # Get residuals from second stage
        residuals = self.results.resid
        
        # Regress residuals on instruments and covariates
        X_overid = self.data[self.instruments + self.covariates].loc[residuals.index].dropna()
        common_idx = residuals.index.intersection(X_overid.index)
        residuals_aligned = residuals.loc[common_idx]
        X_overid_aligned = add_constant(X_overid.loc[common_idx])
        
        # Regress residuals on instruments (including covariates as controls)
        model_overid = OLS(residuals_aligned, X_overid_aligned)
        results_overid = model_overid.fit()
        
        # Sargan statistic: n * R² ~ χ²(k_instruments - 1)
        n = len(residuals_aligned)
        rsquared_overid = results_overid.rsquared
        sargan_stat = n * rsquared_overid
        df_overid = len(self.instruments) - 1  # Degrees of freedom
        sargan_pvalue = 1 - stats.chi2.cdf(sargan_stat, df_overid)
        
        return {
            'sargan_statistic': float(sargan_stat),
            'pvalue': float(sargan_pvalue),
            'degrees_of_freedom': int(df_overid),
            'null_hypothesis': 'Instruments are valid (uncorrelated with error)',
            'interpretation': (
                'p > 0.05 suggests instruments are valid' if sargan_pvalue > 0.05
                else 'p < 0.05 suggests some instruments may be invalid'
            )
        }
    
    def estimate_reduced_form(self) -> Dict[str, float]:
        """Estimate reduced-form regression.
        
        Reduced form: Outcome = f(Instruments, Covariates)
        Shows effect of instruments on outcome directly.
        
        Returns:
            Dictionary containing reduced-form estimates for each instrument
        """
        # Prepare data
        y_rf = self.data[self.outcome].dropna()
        X_rf = self.data[self.instruments + self.covariates].dropna()
        
        # Align indices
        common_idx = y_rf.index.intersection(X_rf.index)
        y_rf = y_rf.loc[common_idx]
        X_rf = X_rf.loc[common_idx]
        
        # Add constant
        X_rf = add_constant(X_rf)
        
        # Estimate reduced form
        model_rf = OLS(y_rf, X_rf)
        self.reduced_form_results = model_rf.fit(cov_type=self.hc_type)
        
        # Extract instrument coefficients
        reduced_form_coefs = {}
        for inst in self.instruments:
            reduced_form_coefs[inst] = {
                'coefficient': float(self.reduced_form_results.params[inst]),
                'std_error': float(self.reduced_form_results.bse[inst]),
                'pvalue': float(self.reduced_form_results.pvalues[inst])
            }
        
        return {
            'instrument_coefficients': reduced_form_coefs,
            'nobs': int(self.reduced_form_results.nobs),
            'rsquared': float(self.reduced_form_results.rsquared)
        }
    
    def summary(self) -> str:
        """Generate summary of IV estimation results.

        Returns:
            Formatted summary string
        """
        self._check_estimated()
        
        summary_lines = []
        summary_lines.append("=" * 80)
        summary_lines.append("Instrumental Variables (2SLS) Estimation Results")
        summary_lines.append("=" * 80)
        summary_lines.append("")
        
        # Second stage results
        summary_lines.append("Second Stage Results:")
        summary_lines.append(str(self.results.summary()))
        summary_lines.append("")
        
        # First stage results
        first_stage = self.estimate_first_stage()
        summary_lines.append("First Stage Results:")
        summary_lines.append(f"  F-statistic: {first_stage['f_statistic']:.4f}")
        summary_lines.append(f"  F-statistic p-value: {first_stage['f_pvalue']:.4f}")
        summary_lines.append(f"  R-squared: {first_stage['rsquared']:.4f}")
        
        # Weak instrument test
        weak_test = self.test_weak_instruments()
        summary_lines.append("")
        summary_lines.append("Weak Instrument Test:")
        summary_lines.append(f"  {weak_test['interpretation']}")
        
        # Overidentification test
        overid_test = self.test_overidentification()
        if overid_test is not None:
            summary_lines.append("")
            summary_lines.append("Overidentification Test (Sargan):")
            summary_lines.append(f"  Test statistic: {overid_test['sargan_statistic']:.4f}")
            summary_lines.append(f"  P-value: {overid_test['pvalue']:.4f}")
            summary_lines.append(f"  {overid_test['interpretation']}")
        
        return "\n".join(summary_lines)

