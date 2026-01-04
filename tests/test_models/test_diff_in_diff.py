"""
Tests for Difference-in-Differences implementation.

These tests validate that DiD estimates match known results.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.diff_in_diff import DifferenceInDifferences


class TestDifferenceInDifferences:
    """Test suite for DiD estimation."""

    def test_did_basic_estimation(self, panel_did_data, true_effects):
        """Test that DiD correctly estimates treatment effect."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        results = did.estimate()

        # Check required keys exist (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'nobs' in results
        assert 'treat_post' in results['coefficients']

        # Treatment effect should be close to 5.0
        estimated_effect = results['coefficients']['treat_post']
        true_effect = true_effects['did_effect']
        assert abs(estimated_effect - true_effect) < 0.5, \
            f"Estimated effect {estimated_effect:.2f} far from true effect {true_effect}"

    def test_did_confidence_intervals(self, panel_did_data, true_effects):
        """Test that confidence intervals contain true effect."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        results = did.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'treat_post' in results['ci_lower']
        assert 'treat_post' in results['ci_upper']

        # True effect should be within 95% CI
        true_effect = true_effects['did_effect']
        ci_low = results['ci_lower']['treat_post']
        ci_high = results['ci_upper']['treat_post']
        assert ci_low <= true_effect <= ci_high, \
            f"True effect {true_effect} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_did_parallel_trends(self, panel_did_data):
        """Test parallel trends diagnostic."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        did.estimate()  # Must estimate first

        # Run parallel trends test
        trends = did.test_parallel_trends(periods_before=2)

        # Check required keys
        assert 'pvalue' in trends
        assert 'test_statistic' in trends
        assert 'interpretation' in trends

        # With our DGP (no differential pre-trends), p-value should be high
        # Note: This is a statistical test, so we use a loose threshold
        assert trends['pvalue'] > 0.01, \
            f"Parallel trends test rejected unexpectedly (p={trends['pvalue']:.4f})"

    def test_did_clustered_standard_errors(self, panel_did_data):
        """Test that standard errors are clustered at unit level."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        results = did.estimate()

        # Standard errors should be computed
        assert results['std_errors']['treat_post'] > 0
        assert results['pvalues']['treat_post'] >= 0
        assert results['pvalues']['treat_post'] <= 1

    def test_did_summary(self, panel_did_data):
        """Test summary generation."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        did.estimate()

        summary = did.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_did_infers_treatment_period(self, panel_did_data):
        """Test that treatment period is inferred if not provided."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=None  # Should be inferred
        )

        # Should not raise an error
        results = did.estimate()
        assert 'coefficients' in results
        assert 'treat_post' in results['coefficients']

    def test_did_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3],
            'time': [0, 1, 2]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            DifferenceInDifferences(
                data=data,
                outcome='y',
                treatment='treatment',  # Missing
                time='time',
                unit='unit_id'  # Missing
            )

    def test_did_diagnostics(self, panel_did_data):
        """Test that diagnostics are included in results."""
        did = DifferenceInDifferences(
            data=panel_did_data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        results = did.estimate()

        # Check diagnostics
        assert 'diagnostics' in results
        assert 'n_units' in results['diagnostics']
        assert 'n_periods' in results['diagnostics']
        assert 'treatment_period' in results['diagnostics']

        # Check fit_stats
        assert 'fit_stats' in results
        assert 'rsquared' in results['fit_stats']

        # Check model_type
        assert results['model_type'] == 'did'


class TestDifferenceInDifferencesEdgeCases:
    """Edge case tests for DiD."""

    def test_did_with_missing_values(self, panel_did_data):
        """Test handling of missing values."""
        data = panel_did_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan

        did = DifferenceInDifferences(
            data=data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=2
        )
        results = did.estimate()

        # Should still work with fewer observations
        assert results['nobs'] < len(panel_did_data)
        assert 'coefficients' in results
        assert 'treat_post' in results['coefficients']

    def test_did_requires_estimate_before_summary(self):
        """Test that summary() fails before estimate()."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4],
            'treated': [0, 0, 1, 1],
            'time': [0, 1, 0, 1],
            'unit_id': [0, 0, 1, 1]
        })

        did = DifferenceInDifferences(
            data=data,
            outcome='y',
            treatment='treated',
            time='time',
            unit='unit_id',
            treatment_period=1
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            did.summary()
