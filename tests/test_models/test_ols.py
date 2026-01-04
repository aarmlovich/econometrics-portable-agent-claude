"""
Tests for OLS regression implementation.

These tests validate that OLS estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.regression.ols import OLSRegression


class TestOLSRegression:
    """Test suite for OLS estimation."""

    def test_ols_basic_estimation(self, ols_data, true_effects):
        """Test that OLS correctly estimates coefficients."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1',
            constant=True
        )
        results = model.estimate()

        # Check required keys exist (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'nobs' in results

        # Check that all coefficients are present
        assert 'const' in results['coefficients']
        assert 'X1' in results['coefficients']
        assert 'X2' in results['coefficients']
        assert 'X3' in results['coefficients']

        # True coefficients: const=5, X1=2, X2=3, X3=-1
        assert abs(results['coefficients']['const'] - true_effects['ols_const']) < 0.5
        assert abs(results['coefficients']['X1'] - true_effects['ols_X1']) < 0.5
        assert abs(results['coefficients']['X2'] - true_effects['ols_X2']) < 0.5
        assert abs(results['coefficients']['X3'] - true_effects['ols_X3']) < 0.5

    def test_ols_confidence_intervals(self, ols_data, true_effects):
        """Test that confidence intervals contain true coefficients."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1',
            constant=True
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results

        # True coefficient X1=2.0 should be in CI
        ci_low = results['ci_lower']['X1']
        ci_high = results['ci_upper']['X1']
        assert ci_low <= true_effects['ols_X1'] <= ci_high, \
            f"True X1 coef {true_effects['ols_X1']} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_ols_no_constant(self, ols_data):
        """Test OLS without constant term."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='HC1',
            constant=False
        )
        results = model.estimate()

        # Should not have 'const' in coefficients
        assert 'const' not in results['coefficients']
        assert 'X1' in results['coefficients']
        assert 'X2' in results['coefficients']
        assert 'X3' in results['coefficients']

    def test_ols_hc_types(self, ols_data):
        """Test that different HC types produce results."""
        for hc_type in ['HC1', 'HC2', 'HC3']:
            model = OLSRegression(
                data=ols_data,
                outcome='y',
                covariates=['X1', 'X2'],
                hc_type=hc_type
            )
            results = model.estimate()

            assert 'coefficients' in results
            assert 'diagnostics' in results
            assert results['diagnostics']['hc_type'] == hc_type

    def test_ols_auto_hc_selection(self, ols_data):
        """Test automatic HC type selection."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3'],
            hc_type='auto'
        )
        results = model.estimate()

        # With n=500, k=4 (3 covariates + const), n/k = 125
        # Should select HC2 (100 <= n/k < 250)
        assert 'diagnostics' in results
        assert results['diagnostics']['hc_type'] in ['HC1', 'HC2', 'HC3']

    def test_ols_fit_statistics(self, ols_data):
        """Test that fit statistics are included."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'rsquared' in results['fit_stats']
        assert 'rsquared_adj' in results['fit_stats']
        assert 'obs_per_regressor' in results['fit_stats']

        # R-squared should be between 0 and 1
        assert 0 <= results['fit_stats']['rsquared'] <= 1
        assert results['fit_stats']['obs_per_regressor'] > 0

    def test_ols_summary(self, ols_data):
        """Test summary generation."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_ols_residuals_and_fitted(self, ols_data):
        """Test that residuals and fitted values are available."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        model.estimate()

        residuals = model.get_residuals()
        fitted = model.get_fitted_values()

        assert isinstance(residuals, pd.Series)
        assert isinstance(fitted, pd.Series)
        assert len(residuals) > 0
        assert len(fitted) > 0

    def test_ols_leverage(self, ols_data):
        """Test leverage calculation."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        model.estimate()

        leverage = model.get_leverage()
        assert isinstance(leverage, np.ndarray)
        assert len(leverage) > 0

        # Mean leverage should equal k/n
        k = 4  # 3 covariates + const
        n = len(leverage)
        expected_mean_leverage = k / n
        assert abs(np.mean(leverage) - expected_mean_leverage) < 0.01

    def test_ols_leverage_statistics(self, ols_data):
        """Test leverage statistics."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        model.estimate()

        leverage_stats = model.get_leverage_statistics()

        assert 'mean_leverage' in leverage_stats
        assert 'max_leverage' in leverage_stats
        assert 'high_leverage_count' in leverage_stats
        assert 'obs_per_regressor' in leverage_stats
        assert 'recommendation' in leverage_stats


class TestOLSEdgeCases:
    """Edge case tests for OLS."""

    def test_ols_with_missing_values(self, ols_data):
        """Test handling of missing values."""
        data = ols_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan
        data.loc[data.index[20:30], 'X1'] = np.nan

        model = OLSRegression(
            data=data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(ols_data)
        assert 'coefficients' in results

    def test_ols_requires_estimate_before_summary(self):
        """Test that methods fail before estimate()."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'X': [1, 2, 3, 4, 5]
        })

        model = OLSRegression(
            data=data,
            outcome='y',
            covariates=['X']
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

        with pytest.raises(ValueError, match="Model not estimated"):
            model.get_residuals()

        with pytest.raises(ValueError, match="Model not estimated"):
            model.get_fitted_values()

    def test_ols_insufficient_observations(self):
        """Test that insufficient observations raise error."""
        data = pd.DataFrame({
            'y': [1, 2, 3],
            'X1': [1, 2, 3],
            'X2': [4, 5, 6]
        })

        # With const=True, we have 3 parameters (const, X1, X2)
        # Need at least 4 observations
        with pytest.raises(ValueError, match="Insufficient observations"):
            OLSRegression(
                data=data,
                outcome='y',
                covariates=['X1', 'X2'],
                constant=True
            )

    def test_ols_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'X1': [1, 2, 3, 4, 5]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            OLSRegression(
                data=data,
                outcome='y',
                covariates=['X1', 'X2']  # X2 missing
            )

    def test_ols_heteroskedastic_data(self, ols_heteroskedastic_data):
        """Test OLS with heteroskedastic data."""
        model = OLSRegression(
            data=ols_heteroskedastic_data,
            outcome='y',
            covariates=['x'],
            hc_type='HC3'  # Use HC3 for heteroskedasticity
        )
        results = model.estimate()

        # Should still estimate (HC3 provides robust SEs)
        assert 'coefficients' in results
        assert 'x' in results['coefficients']

        # True coefficient is 3.0
        assert abs(results['coefficients']['x'] - 3.0) < 0.5

    def test_ols_model_type(self, ols_data):
        """Test that model_type is correctly set."""
        model = OLSRegression(
            data=ols_data,
            outcome='y',
            covariates=['X1', 'X2', 'X3']
        )
        results = model.estimate()

        assert results['model_type'] == 'ols'
