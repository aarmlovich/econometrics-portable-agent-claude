"""
Tests for Fixed Effects panel data estimation.

These tests validate that FE estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.panel.fixed_effects import FixedEffects


class TestFixedEffects:
    """Test suite for Fixed Effects estimation."""

    def test_fe_basic_estimation(self, panel_fe_data, true_effects):
        """Test that FE correctly estimates coefficients."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True,
            cluster_se=True
        )
        results = model.estimate()

        # Check required keys exist (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'nobs' in results

        # Check that coefficients are present
        assert 'X1' in results['coefficients']
        assert 'X2' in results['coefficients']

        # True coefficients: X1=2.0, X2=3.0
        estimated_X1 = results['coefficients']['X1']
        estimated_X2 = results['coefficients']['X2']
        assert abs(estimated_X1 - true_effects['fe_X1']) < 0.5, \
            f"Estimated X1 {estimated_X1:.2f} far from true {true_effects['fe_X1']}"
        assert abs(estimated_X2 - true_effects['fe_X2']) < 0.5, \
            f"Estimated X2 {estimated_X2:.2f} far from true {true_effects['fe_X2']}"

    def test_fe_confidence_intervals(self, panel_fe_data, true_effects):
        """Test that confidence intervals contain true coefficients."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'X1' in results['ci_lower']
        assert 'X1' in results['ci_upper']

        # True coefficient X1=2.0 should be in CI
        ci_low = results['ci_lower']['X1']
        ci_high = results['ci_upper']['X1']
        assert ci_low <= true_effects['fe_X1'] <= ci_high, \
            f"True X1 coef {true_effects['fe_X1']} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_fe_entity_effects_only(self, panel_fe_data):
        """Test FE with only entity effects."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=False
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'diagnostics' in results
        assert results['diagnostics']['entity_effects'] is True
        assert results['diagnostics']['time_effects'] is False

    def test_fe_time_effects_only(self, panel_fe_data):
        """Test FE with only time effects."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=False,
            time_effects=True
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'diagnostics' in results
        assert results['diagnostics']['entity_effects'] is False
        assert results['diagnostics']['time_effects'] is True

    def test_fe_no_clustering(self, panel_fe_data):
        """Test FE without clustered standard errors."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            cluster_se=False
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert results['diagnostics']['cluster_se'] is False

    def test_fe_fit_statistics(self, panel_fe_data):
        """Test that fit statistics are included."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'rsquared' in results['fit_stats']
        assert 'rsquared_within' in results['fit_stats']
        assert 'nentities' in results['fit_stats']
        assert 'ntime' in results['fit_stats']

        # Check reasonable values
        assert 0 <= results['fit_stats']['rsquared'] <= 1
        assert results['fit_stats']['nentities'] > 0
        assert results['fit_stats']['ntime'] > 0

    def test_fe_diagnostics(self, panel_fe_data):
        """Test that diagnostics are included."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True,
            cluster_se=True
        )
        results = model.estimate()

        assert 'diagnostics' in results
        assert 'entity_effects' in results['diagnostics']
        assert 'time_effects' in results['diagnostics']
        assert 'cluster_se' in results['diagnostics']

    def test_fe_summary(self, panel_fe_data):
        """Test summary generation."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year'
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_fe_residuals(self, panel_fe_data):
        """Test that residuals are available."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year'
        )
        model.estimate()

        residuals = model.get_residuals()
        assert isinstance(residuals, pd.Series)
        assert len(residuals) > 0

    def test_fe_single_covariate(self, panel_fe_data):
        """Test FE with single covariate."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'X1' in results['coefficients']


class TestFixedEffectsEdgeCases:
    """Edge case tests for Fixed Effects."""

    def test_fe_with_missing_values(self, panel_fe_data):
        """Test handling of missing values."""
        data = panel_fe_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan
        data.loc[data.index[20:30], 'X1'] = np.nan

        # Reset index since FE will set it
        data = data.reset_index(drop=True)
        data['entity_id'] = np.repeat(range(50), 5)
        data['year'] = np.tile(range(5), 50)

        model = FixedEffects(
            data=data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(panel_fe_data)
        assert 'coefficients' in results

    def test_fe_requires_estimate_before_summary(self):
        """Test that methods fail before estimate()."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5, 6],
            'X': [1, 2, 3, 4, 5, 6],
            'entity': [0, 0, 1, 1, 2, 2],
            'time': [0, 1, 0, 1, 0, 1]
        })

        model = FixedEffects(
            data=data,
            outcome='y',
            covariates=['X'],
            entity='entity',
            time='time'
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

        with pytest.raises(ValueError, match="Model not estimated"):
            model.get_residuals()

    def test_fe_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5, 6],
            'X1': [1, 2, 3, 4, 5, 6],
            'entity': [0, 0, 1, 1, 2, 2],
            'time': [0, 1, 0, 1, 0, 1]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            FixedEffects(
                data=data,
                outcome='y',
                covariates=['X1', 'X2'],  # X2 missing
                entity='entity',
                time='time'
            )

    def test_fe_model_type(self, panel_fe_data):
        """Test that model_type is correctly set."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        assert results['model_type'] == 'fe'

    def test_fe_both_effects(self, panel_fe_data):
        """Test FE with both entity and time effects."""
        model = FixedEffects(
            data=panel_fe_data,
            outcome='y',
            covariates=['X1', 'X2'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True
        )
        results = model.estimate()

        assert results['diagnostics']['entity_effects'] is True
        assert results['diagnostics']['time_effects'] is True
