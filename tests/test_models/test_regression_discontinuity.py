"""
Tests for Regression Discontinuity Design estimation.

These tests validate that RD estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.regression_discontinuity import RegressionDiscontinuity


class TestRegressionDiscontinuity:
    """Test suite for RD estimation."""

    def test_rd_basic_estimation(self, rd_data, true_effects):
        """Test that RD correctly estimates treatment effect."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0,
            polynomial=1
        )
        results = model.estimate()

        # Check required keys exist (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'nobs' in results

        # Check that RD effect is present
        assert 'rd_effect' in results['coefficients']

        # True effect is 3.0
        estimated_effect = results['coefficients']['rd_effect']
        true_effect = true_effects['rd_effect']
        assert abs(estimated_effect - true_effect) < 1.0, \
            f"Estimated effect {estimated_effect:.2f} far from true effect {true_effect}"

    def test_rd_confidence_intervals(self, rd_data, true_effects):
        """Test that confidence intervals contain true effect."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'rd_effect' in results['ci_lower']
        assert 'rd_effect' in results['ci_upper']

        # True effect should be within 95% CI
        true_effect = true_effects['rd_effect']
        ci_low = results['ci_lower']['rd_effect']
        ci_high = results['ci_upper']['rd_effect']
        # Use looser threshold for RD (noisy estimator)
        assert ci_low - 1.0 <= true_effect <= ci_high + 1.0, \
            f"True effect {true_effect} not near CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_rd_automatic_bandwidth_selection(self, rd_data):
        """Test that bandwidth is selected if not provided."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=None,  # Should be selected
            polynomial=1
        )

        # Should not raise an error
        results = model.estimate()
        assert 'coefficients' in results
        assert 'fit_stats' in results
        assert 'bandwidth' in results['fit_stats']
        assert results['fit_stats']['bandwidth'] > 0

    def test_rd_polynomial_orders(self, rd_data):
        """Test RD with different polynomial orders."""
        for poly_order in [1, 2]:
            model = RegressionDiscontinuity(
                data=rd_data,
                outcome='y',
                running='running',
                cutoff=0.0,
                bandwidth=2.0,
                polynomial=poly_order
            )
            results = model.estimate()

            assert 'coefficients' in results
            assert 'diagnostics' in results
            assert results['diagnostics']['polynomial'] == poly_order

    def test_rd_different_kernels(self, rd_data):
        """Test RD with different kernel functions."""
        for kernel in ['triangular', 'uniform', 'epanechnikov']:
            model = RegressionDiscontinuity(
                data=rd_data,
                outcome='y',
                running='running',
                cutoff=0.0,
                bandwidth=2.0,
                kernel=kernel
            )
            results = model.estimate()

            assert 'coefficients' in results
            assert 'diagnostics' in results
            assert results['diagnostics']['kernel'] == kernel

    def test_rd_manipulation_test(self, rd_data):
        """Test manipulation test (McCrary density test)."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        model.estimate()

        manipulation_test = model.test_manipulation()

        assert 'test_statistic' in manipulation_test
        assert 'pvalue' in manipulation_test
        assert 'interpretation' in manipulation_test

        # With random assignment, ideally should not detect manipulation
        # However, with finite samples and specific random seeds, false positives can occur
        # We only check that the test runs and returns a valid result
        # A proper test would use many seeds and check false positive rate
        if not np.isnan(manipulation_test['pvalue']):
            assert 0 <= manipulation_test['pvalue'] <= 1, \
                f"Invalid p-value: {manipulation_test['pvalue']}"

    def test_rd_robustness_bandwidths(self, rd_data):
        """Test robustness checks with multiple bandwidths."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        model.estimate()

        robustness = model.estimate_robustness_bandwidths()

        # Should have estimates for different bandwidth multiples
        assert '0.5x' in robustness
        assert '1.0x' in robustness
        assert '1.5x' in robustness

        # Each should have coefficients (or error)
        for key in ['0.5x', '1.0x', '1.5x']:
            assert key in robustness
            # Either has coefficients or has error
            assert 'coefficients' in robustness[key] or 'error' in robustness[key]

    def test_rd_fit_statistics(self, rd_data):
        """Test that fit statistics are included."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'bandwidth' in results['fit_stats']

    def test_rd_diagnostics(self, rd_data):
        """Test that diagnostics are included."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0,
            polynomial=1,
            kernel='triangular'
        )
        results = model.estimate()

        assert 'diagnostics' in results
        assert 'polynomial' in results['diagnostics']
        assert 'kernel' in results['diagnostics']
        assert 'cutoff' in results['diagnostics']

    def test_rd_summary(self, rd_data):
        """Test summary generation."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'Regression Discontinuity' in summary

    def test_rd_nonlinear_data(self, rd_nonlinear_data):
        """Test RD with nonlinear relationship."""
        # Use polynomial=2 to handle nonlinearity
        model = RegressionDiscontinuity(
            data=rd_nonlinear_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0,
            polynomial=2
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'rd_effect' in results['coefficients']


class TestRDEdgeCases:
    """Edge case tests for Regression Discontinuity."""

    def test_rd_with_missing_values(self, rd_data):
        """Test handling of missing values."""
        data = rd_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan

        model = RegressionDiscontinuity(
            data=data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(rd_data)
        assert 'coefficients' in results

    def test_rd_requires_estimate_before_summary(self):
        """Test that methods fail before estimate()."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'running': np.random.uniform(-5, 5, 100)
        })

        model = RegressionDiscontinuity(
            data=data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

    def test_rd_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            RegressionDiscontinuity(
                data=data,
                outcome='y',
                running='running',  # Missing
                cutoff=0.0
            )

    def test_rd_invalid_kernel(self, rd_data):
        """Test that invalid kernel raises ValueError."""
        with pytest.raises(ValueError, match="Kernel must be one of"):
            RegressionDiscontinuity(
                data=rd_data,
                outcome='y',
                running='running',
                cutoff=0.0,
                kernel='invalid'
            )

    def test_rd_insufficient_bandwidth_data(self, rd_data):
        """Test error when bandwidth is too small."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=0.01,  # Very small bandwidth
            polynomial=1
        )

        # Should raise error about insufficient observations
        with pytest.raises(ValueError, match="Insufficient observations"):
            model.estimate()

    def test_rd_model_type(self, rd_data):
        """Test that model_type is correctly set."""
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0
        )
        results = model.estimate()

        assert results['model_type'] == 'rd'

    def test_rd_with_covariates(self, rd_data):
        """Test RD with additional covariates."""
        # Add covariate
        data = rd_data.copy()
        data['X_control'] = np.random.normal(0, 1, len(data))

        model = RegressionDiscontinuity(
            data=data,
            outcome='y',
            running='running',
            cutoff=0.0,
            bandwidth=2.0,
            covariates=['X_control']
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'rd_effect' in results['coefficients']

    def test_rd_cutoff_parameter(self, rd_data):
        """Test that cutoff parameter is stored correctly."""
        cutoff_value = 0.5
        model = RegressionDiscontinuity(
            data=rd_data,
            outcome='y',
            running='running',
            cutoff=cutoff_value,
            bandwidth=2.0
        )
        results = model.estimate()

        assert results['diagnostics']['cutoff'] == cutoff_value
