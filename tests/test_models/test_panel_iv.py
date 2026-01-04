"""
Tests for Panel Instrumental Variables estimation.

These tests validate that Panel IV/2SLS estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.panel.panel_iv import PanelIV


class TestPanelIV:
    """Test suite for Panel IV estimation."""

    def test_panel_iv_basic_estimation(self, panel_iv_data, true_effects):
        """Test that Panel IV correctly estimates treatment effect."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
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

        # Check that treatment coefficient is present
        assert 'x' in results['coefficients']

        # True treatment effect is 2.0
        estimated_effect = results['coefficients']['x']
        true_effect = true_effects['panel_iv_effect']
        assert abs(estimated_effect - true_effect) < 1.0, \
            f"Estimated effect {estimated_effect:.2f} far from true effect {true_effect}"

    def test_panel_iv_confidence_intervals(self, panel_iv_data, true_effects):
        """Test that confidence intervals contain true effect."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'x' in results['ci_lower']
        assert 'x' in results['ci_upper']

        # True effect should be within 95% CI
        true_effect = true_effects['panel_iv_effect']
        ci_low = results['ci_lower']['x']
        ci_high = results['ci_upper']['x']
        assert ci_low <= true_effect <= ci_high, \
            f"True effect {true_effect} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_panel_iv_first_stage(self, panel_iv_data):
        """Test first-stage estimation with fixed effects."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True
        )

        first_stage = model.estimate_first_stage()

        # Check first-stage results
        assert 'coefficients' in first_stage
        assert 'std_errors' in first_stage
        assert 'pvalues' in first_stage
        assert 'rsquared' in first_stage
        assert 'rsquared_within' in first_stage
        assert 'f_statistic' in first_stage
        assert 'f_pvalue' in first_stage

        # With strong instrument, F should be > 10
        assert first_stage['f_statistic'] > 10, \
            f"Strong instrument should have F > 10, got {first_stage['f_statistic']:.2f}"

    def test_panel_iv_weak_instrument_test(self, panel_iv_data):
        """Test weak instrument diagnostic."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        model.estimate()

        weak_test = model.test_weak_instruments()

        assert 'f_statistic' in weak_test
        assert 'is_weak' in weak_test
        assert 'interpretation' in weak_test

        # With strong instrument, should not be weak
        assert weak_test['is_weak'] is False

    def test_panel_iv_entity_effects_only(self, panel_iv_data):
        """Test Panel IV with only entity effects."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
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

    def test_panel_iv_time_effects_only(self, panel_iv_data):
        """Test Panel IV with only time effects."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
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

    def test_panel_iv_no_clustering(self, panel_iv_data):
        """Test Panel IV without clustered standard errors."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year',
            cluster_se=False
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert results['diagnostics']['cluster_se'] is False

    def test_panel_iv_with_covariates(self, panel_iv_data):
        """Test Panel IV with additional covariates."""
        # Add a covariate
        data = panel_iv_data.copy()
        data = data.reset_index(drop=True)
        data['X_control'] = np.random.normal(0, 1, len(data))

        model = PanelIV(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year',
            covariates=['X_control']
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'x' in results['coefficients']

    def test_panel_iv_reduced_form(self, panel_iv_data):
        """Test reduced-form estimation with fixed effects."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )

        reduced_form = model.estimate_reduced_form()

        assert 'instrument_coefficients' in reduced_form
        assert 'nobs' in reduced_form
        assert 'rsquared' in reduced_form
        assert 'rsquared_within' in reduced_form

        # Should have coefficient for instrument z
        assert 'z' in reduced_form['instrument_coefficients']
        assert 'coefficient' in reduced_form['instrument_coefficients']['z']
        assert 'std_error' in reduced_form['instrument_coefficients']['z']
        assert 'pvalue' in reduced_form['instrument_coefficients']['z']

    def test_panel_iv_fit_statistics(self, panel_iv_data):
        """Test that fit statistics are included."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'rsquared' in results['fit_stats']
        assert 'rsquared_within' in results['fit_stats']
        assert 'first_stage_f' in results['fit_stats']

    def test_panel_iv_diagnostics(self, panel_iv_data):
        """Test that diagnostics are included."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
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
        assert 'n_instruments' in results['diagnostics']

        assert results['diagnostics']['n_instruments'] == 1

    def test_panel_iv_summary(self, panel_iv_data):
        """Test summary generation."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'Panel IV' in summary
        assert 'First Stage' in summary

    def test_panel_iv_overidentification_test(self, panel_iv_data):
        """Test overidentification test (not fully implemented)."""
        # Add second instrument
        data = panel_iv_data.copy()
        data = data.reset_index(drop=True)
        data['z2'] = np.random.normal(0, 1, len(data))

        model = PanelIV(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z', 'z2'],
            entity='entity_id',
            time='year'
        )
        model.estimate()

        # Should warn that test is not fully implemented
        with pytest.warns(UserWarning, match="Overidentification test.*not fully implemented"):
            overid_test = model.test_overidentification()

        # Returns None since not fully implemented
        assert overid_test is None


class TestPanelIVEdgeCases:
    """Edge case tests for Panel IV."""

    def test_panel_iv_with_missing_values(self, panel_iv_data):
        """Test handling of missing values."""
        data = panel_iv_data.copy()
        data = data.reset_index(drop=True)
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan
        data.loc[data.index[20:30], 'x'] = np.nan

        model = PanelIV(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(panel_iv_data)
        assert 'coefficients' in results

    def test_panel_iv_requires_estimate_before_summary(self):
        """Test that summary() fails before estimate()."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'x': np.random.normal(0, 1, 100),
            'z': np.random.normal(0, 1, 100),
            'entity': np.repeat(range(20), 5),
            'time': np.tile(range(5), 20)
        })

        model = PanelIV(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity',
            time='time'
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

    def test_panel_iv_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5, 6],
            'x': [1, 2, 3, 4, 5, 6],
            'entity': [0, 0, 1, 1, 2, 2],
            'time': [0, 1, 0, 1, 0, 1]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            PanelIV(
                data=data,
                outcome='y',
                treatment='x',
                instruments=['z'],  # z is missing
                entity='entity',
                time='time'
            )

    def test_panel_iv_requires_instruments(self):
        """Test that at least one instrument is required."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5, 6],
            'x': [1, 2, 3, 4, 5, 6],
            'entity': [0, 0, 1, 1, 2, 2],
            'time': [0, 1, 0, 1, 0, 1]
        })

        with pytest.raises(ValueError, match="At least one instrument is required"):
            PanelIV(
                data=data,
                outcome='y',
                treatment='x',
                instruments=[],  # No instruments
                entity='entity',
                time='time'
            )

    def test_panel_iv_model_type(self, panel_iv_data):
        """Test that model_type is correctly set."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        assert results['model_type'] == 'panel_iv'

    def test_panel_iv_both_effects(self, panel_iv_data):
        """Test Panel IV with both entity and time effects."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            entity='entity_id',
            time='year',
            entity_effects=True,
            time_effects=True
        )
        results = model.estimate()

        assert results['diagnostics']['entity_effects'] is True
        assert results['diagnostics']['time_effects'] is True

    def test_panel_iv_exactly_identified(self, panel_iv_data):
        """Test Panel IV with exactly identified case."""
        model = PanelIV(
            data=panel_iv_data,
            outcome='y',
            treatment='x',
            instruments=['z'],  # One instrument, one endogenous var
            entity='entity_id',
            time='year'
        )
        results = model.estimate()

        # Should work fine
        assert 'coefficients' in results
        assert results['diagnostics']['n_instruments'] == 1
