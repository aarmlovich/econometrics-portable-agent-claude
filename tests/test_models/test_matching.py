"""
Tests for Propensity Score Matching estimation.

These tests validate that matching estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.matching import Matching


class TestMatching:
    """Test suite for Propensity Score Matching estimation."""

    def test_matching_basic_estimation(self, matching_data, true_effects):
        """Test that matching correctly estimates ATE."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            matching_method='nearest_neighbor',
            trim_support=True
        )
        results = model.estimate()

        # Check required keys exist (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'nobs' in results

        # Check that ATE is present
        assert 'ate' in results['coefficients']

        # True ATE is 3.0
        estimated_ate = results['coefficients']['ate']
        true_ate = true_effects['matching_ate']
        assert abs(estimated_ate - true_ate) < 1.0, \
            f"Estimated ATE {estimated_ate:.2f} far from true ATE {true_ate}"

    def test_matching_confidence_intervals(self, matching_data, true_effects):
        """Test that confidence intervals contain true ATE."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            matching_method='nearest_neighbor'
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'ate' in results['ci_lower']
        assert 'ate' in results['ci_upper']

        # True ATE should be within 95% CI
        true_ate = true_effects['matching_ate']
        ci_low = results['ci_lower']['ate']
        ci_high = results['ci_upper']['ate']
        assert ci_low <= true_ate <= ci_high, \
            f"True ATE {true_ate} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_matching_propensity_scores(self, matching_data):
        """Test propensity score estimation."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )

        propensity_scores = model.estimate_propensity_scores()

        assert isinstance(propensity_scores, pd.Series)
        assert len(propensity_scores) > 0
        # Propensity scores should be between 0 and 1
        assert (propensity_scores >= 0).all()
        assert (propensity_scores <= 1).all()

    def test_matching_balance_pre_matching(self, matching_data):
        """Test covariate balance before matching."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )

        balance_pre = model.test_balance_pre_matching()

        assert 'standardized_differences' in balance_pre
        assert 'variance_ratios' in balance_pre
        assert 'balance_table' in balance_pre

        # Should have balance stats for each covariate
        assert 'X1' in balance_pre['standardized_differences']
        assert 'X2' in balance_pre['standardized_differences']

    def test_matching_balance_post_matching(self, matching_data):
        """Test covariate balance after matching."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        model.estimate()  # Must estimate first

        balance_post = model.test_balance_post_matching()

        assert 'standardized_differences' in balance_post
        assert 'variance_ratios' in balance_post
        assert 'balance_table' in balance_post

        # Standardized differences should be smaller after matching
        # (though not guaranteed with small samples)
        assert 'X1' in balance_post['standardized_differences']
        assert 'X2' in balance_post['standardized_differences']

    def test_matching_methods(self, matching_data):
        """Test different matching methods."""
        for method in ['nearest_neighbor', 'radius']:
            model = Matching(
                data=matching_data,
                outcome='y',
                treatment='treatment',
                covariates=['X1', 'X2'],
                matching_method=method
            )
            results = model.estimate()

            assert 'coefficients' in results
            assert 'diagnostics' in results
            assert results['diagnostics']['matching_method'] == method

    def test_matching_kernel_method_warning(self, matching_data):
        """Test that kernel matching gives warning (not fully implemented)."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            matching_method='kernel'
        )

        # Should warn that kernel matching is not fully implemented
        with pytest.warns(UserWarning, match="Kernel matching not fully implemented"):
            model.estimate()

    def test_matching_with_replacement(self, matching_data):
        """Test matching with replacement."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            replacement=True
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'ate' in results['coefficients']

    def test_matching_without_replacement(self, matching_data):
        """Test matching without replacement."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            replacement=False
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'ate' in results['coefficients']

    def test_matching_trim_support(self, matching_data):
        """Test common support trimming."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            trim_support=True,
            trim_threshold_low=0.1,
            trim_threshold_high=0.9
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'n_trimmed' in results['fit_stats']
        assert results['diagnostics']['trim_support'] is True

    def test_matching_no_trim_support(self, matching_data):
        """Test matching without trimming."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            trim_support=False
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert results['fit_stats']['n_trimmed'] == 0

    def test_matching_fit_statistics(self, matching_data):
        """Test that fit statistics are included."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'n_treated' in results['fit_stats']
        assert 'n_control' in results['fit_stats']
        assert 'n_matched' in results['fit_stats']
        assert 'n_trimmed' in results['fit_stats']

        # Check reasonable values
        assert results['fit_stats']['n_treated'] > 0
        assert results['fit_stats']['n_control'] > 0
        assert results['fit_stats']['n_matched'] > 0

    def test_matching_diagnostics(self, matching_data):
        """Test that diagnostics are included."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            matching_method='nearest_neighbor'
        )
        results = model.estimate()

        assert 'diagnostics' in results
        assert 'matching_method' in results['diagnostics']
        assert 'caliper' in results['diagnostics']
        assert 'trim_support' in results['diagnostics']

    def test_matching_summary(self, matching_data):
        """Test summary generation."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'Matching' in summary

    def test_matching_unbalanced_data(self, matching_unbalanced_data):
        """Test matching with imbalanced treatment/control groups."""
        model = Matching(
            data=matching_unbalanced_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        results = model.estimate()

        # Should still work even with imbalance
        assert 'coefficients' in results
        assert 'ate' in results['coefficients']


class TestMatchingEdgeCases:
    """Edge case tests for Matching."""

    def test_matching_with_missing_values(self, matching_data):
        """Test handling of missing values."""
        data = matching_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan

        model = Matching(
            data=data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(matching_data)
        assert 'coefficients' in results

    def test_matching_requires_estimate_before_summary(self):
        """Test that methods fail before estimate()."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'treatment': np.random.binomial(1, 0.5, 100),
            'X1': np.random.normal(0, 1, 100),
            'X2': np.random.normal(0, 1, 100)
        })

        model = Matching(
            data=data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

    def test_matching_requires_estimate_for_post_balance(self):
        """Test that post-matching balance requires estimation."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'treatment': np.random.binomial(1, 0.5, 100),
            'X1': np.random.normal(0, 1, 100),
            'X2': np.random.normal(0, 1, 100)
        })

        model = Matching(
            data=data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )

        with pytest.raises(ValueError, match="Must run matching first"):
            model.test_balance_post_matching()

    def test_matching_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'treatment': [0, 1, 0, 1, 0]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            Matching(
                data=data,
                outcome='y',
                treatment='treatment',
                covariates=['X1']  # X1 missing
            )

    def test_matching_validates_binary_treatment(self):
        """Test that non-binary treatment raises ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'treatment': [0, 1, 2, 1, 0],  # Not binary
            'X1': [1, 2, 3, 4, 5]
        })

        with pytest.raises(ValueError, match="Treatment variable must be binary"):
            Matching(
                data=data,
                outcome='y',
                treatment='treatment',
                covariates=['X1']
            )

    def test_matching_model_type(self, matching_data):
        """Test that model_type is correctly set."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2']
        )
        results = model.estimate()

        assert results['model_type'] == 'matching'

    def test_matching_n_neighbors(self, matching_data):
        """Test matching with multiple neighbors."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            matching_method='nearest_neighbor',
            n_neighbors=3
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'ate' in results['coefficients']

    def test_matching_caliper_specification(self, matching_data):
        """Test matching with custom caliper."""
        model = Matching(
            data=matching_data,
            outcome='y',
            treatment='treatment',
            covariates=['X1', 'X2'],
            caliper=0.1
        )
        results = model.estimate()

        assert results['diagnostics']['caliper'] == 0.1
