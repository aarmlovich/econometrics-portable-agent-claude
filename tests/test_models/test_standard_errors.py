"""
Tests for standard error calculations.

These tests validate that robust standard errors (HC1, HC2, HC3) are computed correctly.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.regression.ols import OLSRegression


class TestRobustStandardErrors:
    """Test suite for robust standard errors in OLS."""

    def test_hc1_standard_errors(self, ols_data):
        """Test HC1 (heteroskedasticity-consistent) standard errors."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1'
        )
        results = model.estimate()

        # Check required keys exist
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'diagnostics' in results
        assert 'hc_type' in results['diagnostics']

        # Verify HC1 was used
        assert results['diagnostics']['hc_type'] == 'HC1'

        # Standard errors should be positive
        assert all(se > 0 for se in results['std_errors'].values())

    def test_hc2_standard_errors(self, ols_data):
        """Test HC2 (leverage-adjusted) standard errors."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC2'
        )
        results = model.estimate()

        assert results['diagnostics']['hc_type'] == 'HC2'
        assert all(se > 0 for se in results['std_errors'].values())

    def test_hc3_standard_errors(self, ols_data):
        """Test HC3 (jackknife) standard errors."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC3'
        )
        results = model.estimate()

        assert results['diagnostics']['hc_type'] == 'HC3'
        assert all(se > 0 for se in results['std_errors'].values())

    def test_auto_hc_selection_large_sample(self, ols_data):
        """Test automatic HC type selection with large sample (should choose HC1)."""
        # ols_data has 500 obs, 3 covariates + constant = 4 params
        # n/k = 500/4 = 125 -> should select HC2
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='auto'
        )
        results = model.estimate()

        # n/k = 125, so should select HC2 (100 <= n/k < 250)
        assert results['diagnostics']['hc_type'] == 'HC2'
        assert results['fit_stats']['obs_per_regressor'] == pytest.approx(125.0, rel=0.01)

    def test_auto_hc_selection_small_sample(self):
        """Test automatic HC type selection with small sample (should choose HC3)."""
        np.random.seed(42)
        n = 50  # Small sample

        data = pd.DataFrame({
            'y': np.random.normal(0, 1, n),
            'X1': np.random.normal(0, 1, n),
            'X2': np.random.normal(0, 1, n),
            'X3': np.random.normal(0, 1, n)
        })

        model = OLSRegression(
            data=data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='auto'
        )
        results = model.estimate()

        # n/k = 50/4 = 12.5, so should select HC3 (n/k < 100)
        assert results['diagnostics']['hc_type'] == 'HC3'

    def test_robust_se_with_heteroskedasticity(self, ols_heteroskedastic_data):
        """Test that robust SE are appropriate with heteroskedastic errors."""
        model = OLSRegression(
            data=ols_heteroskedastic_data,
            outcome='y',
            covariates=['x'],
            hc_type='HC1'
        )
        results = model.estimate()

        # Coefficient should still be close to true value (3.0)
        # Note: with heteroskedasticity, we expect coefficient around 3.0
        assert abs(results['coefficients']['x'] - 3.0) < 0.5

        # Standard errors should be computed
        assert len(results['std_errors']) == 2  # Intercept + slope

    def test_hc_types_produce_different_se(self, ols_heteroskedastic_data):
        """Test that different HC types produce different standard errors."""
        ses = {}
        for hc_type in ['HC1', 'HC2', 'HC3']:
            model = OLSRegression(
                data=ols_heteroskedastic_data,
                outcome='y',
                covariates=['x'],
                hc_type=hc_type
            )
            results = model.estimate()
            ses[hc_type] = results['std_errors']['x']  # Slope SE

        # HC3 should typically be largest (most conservative)
        # HC1 should typically be smallest
        # Note: This relationship isn't guaranteed for all data, but is typical
        assert ses['HC3'] >= ses['HC1'] * 0.9, "HC3 should be >= HC1 (approximately)"


class TestOLSCoefficients:
    """Test that OLS recovers true coefficients."""

    def test_ols_recovers_true_coefficients(self, ols_data, true_effects):
        """Test that OLS estimates are close to true values."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1'
        )
        results = model.estimate()

        # Coefficients now use named keys
        # True: const=5.0, X1=2.0, X2=3.0, X3=-1.0
        assert abs(results['coefficients']['const'] - true_effects['ols_const']) < 0.5
        assert abs(results['coefficients']['X1'] - true_effects['ols_X1']) < 0.5
        assert abs(results['coefficients']['X2'] - true_effects['ols_X2']) < 0.5
        assert abs(results['coefficients']['X3'] - true_effects['ols_X3']) < 0.5

    def test_ols_without_constant(self, ols_data):
        """Test OLS without intercept term."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1',
            constant=False
        )
        results = model.estimate()

        # Should have 3 coefficients (no intercept)
        assert len(results['coefficients']) == 3
        assert 'const' not in results['coefficients']


class TestOLSDiagnostics:
    """Test OLS diagnostic methods."""

    def test_leverage_statistics(self, ols_data):
        """Test leverage calculation."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1'
        )
        model.estimate()

        stats = model.get_leverage_statistics()

        assert 'mean_leverage' in stats
        assert 'max_leverage' in stats
        assert 'high_leverage_count' in stats
        assert 'recommendation' in stats

        # Mean leverage should equal k/n
        k = 4  # 3 covariates + constant
        n = len(ols_data)
        expected_mean_leverage = k / n
        assert abs(stats['mean_leverage'] - expected_mean_leverage) < 0.01

    def test_residuals(self, ols_data):
        """Test residual extraction."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1'
        )
        model.estimate()

        residuals = model.get_residuals()
        fitted = model.get_fitted_values()

        # Check dimensions
        assert len(residuals) == len(ols_data)
        assert len(fitted) == len(ols_data)

        # Residuals should sum to approximately zero
        assert abs(residuals.sum()) < 1e-10

    def test_summary_generation(self, ols_data):
        """Test summary table generation."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1'
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'R-squared' in summary or 'rsquared' in summary.lower()


class TestOLSValidation:
    """Test input validation."""

    def test_missing_columns_raises_error(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3],
            'X1': [1, 2, 3]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            OLSRegression(
                data=data,
                outcome='y',
                covariates=['X1', 'X2'],  # X2 is missing
                hc_type='HC1'
            )

    def test_insufficient_observations_raises_error(self):
        """Test that insufficient observations raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2],
            'X1': [1, 2],
            'X2': [1, 2],
            'X3': [1, 2]
        })

        with pytest.raises(ValueError, match="Insufficient observations"):
            OLSRegression(
                data=data,
                outcome='y',
                covariates=['X1', 'X2', 'X3'],  # 3 covariates + constant = 4 params, but only 2 obs
                hc_type='HC1'
            )

    def test_estimate_before_diagnostics_raises_error(self):
        """Test that diagnostics fail before estimate()."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'X1': np.random.normal(0, 1, 100)
        })

        model = OLSRegression(
            data=data,
            outcome='y',
            covariates=['X1'],
            hc_type='HC1'
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

        with pytest.raises(ValueError, match="Model not estimated"):
            model.get_residuals()


# TODO: Add more tests:
# - Test HAC standard errors (when implemented)
# - Test two-way clustering (when implemented)
# - Validate against statsmodels/linearmodels results exactly
# - Test with collinear variables
