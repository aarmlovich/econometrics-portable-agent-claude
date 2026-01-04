"""
Tests for Instrumental Variables (IV) estimation.

These tests validate that IV/2SLS estimates match known results with synthetic data.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.instrumental_variables import InstrumentalVariables


class TestInstrumentalVariables:
    """Test suite for IV estimation."""

    def test_iv_basic_estimation(self, iv_strong_data, true_effects):
        """Test that IV correctly estimates treatment effect with strong instruments."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
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
        true_effect = true_effects['iv_effect']
        assert abs(estimated_effect - true_effect) < 0.5, \
            f"Estimated effect {estimated_effect:.2f} far from true effect {true_effect}"

    def test_iv_confidence_intervals(self, iv_strong_data, true_effects):
        """Test that confidence intervals contain true effect."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        results = model.estimate()

        # Check CI keys exist
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'x' in results['ci_lower']
        assert 'x' in results['ci_upper']

        # True effect should be within 95% CI
        true_effect = true_effects['iv_effect']
        ci_low = results['ci_lower']['x']
        ci_high = results['ci_upper']['x']
        assert ci_low <= true_effect <= ci_high, \
            f"True effect {true_effect} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_iv_first_stage(self, iv_strong_data):
        """Test first-stage estimation."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )

        first_stage = model.estimate_first_stage()

        # Check first-stage results
        assert 'coefficients' in first_stage
        assert 'std_errors' in first_stage
        assert 'pvalues' in first_stage
        assert 'rsquared' in first_stage
        assert 'f_statistic' in first_stage
        assert 'f_pvalue' in first_stage

        # With strong instrument, F should be > 10
        assert first_stage['f_statistic'] > 10, \
            f"Strong instrument should have F > 10, got {first_stage['f_statistic']:.2f}"

    def test_iv_weak_instrument_detection(self, iv_weak_data):
        """Test that weak instruments are detected."""
        model = InstrumentalVariables(
            data=iv_weak_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )

        # Should warn about weak instruments
        with pytest.warns(UserWarning, match="Weak instruments detected"):
            results = model.estimate()

        # First-stage F should be < 10
        first_stage = model.estimate_first_stage()
        assert first_stage['f_statistic'] < 10, \
            f"Weak instrument should have F < 10, got {first_stage['f_statistic']:.2f}"

    def test_iv_weak_instrument_test(self, iv_strong_data, iv_weak_data):
        """Test weak instrument diagnostic."""
        # Strong instrument
        model_strong = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        model_strong.estimate()
        weak_test_strong = model_strong.test_weak_instruments()

        assert 'f_statistic' in weak_test_strong
        assert 'is_weak' in weak_test_strong
        assert 'interpretation' in weak_test_strong
        assert weak_test_strong['is_weak'] is False

        # Weak instrument
        model_weak = InstrumentalVariables(
            data=iv_weak_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        with pytest.warns(UserWarning):
            model_weak.estimate()
        weak_test_weak = model_weak.test_weak_instruments()

        assert weak_test_weak['is_weak'] is True

    def test_iv_overidentification_test(self, iv_overidentified_data):
        """Test overidentification test with multiple instruments."""
        model = InstrumentalVariables(
            data=iv_overidentified_data,
            outcome='y',
            treatment='x',
            instruments=['z1', 'z2']
        )
        model.estimate()

        overid_test = model.test_overidentification()

        # Should return test results (not None) because overidentified
        assert overid_test is not None
        assert 'sargan_statistic' in overid_test
        assert 'pvalue' in overid_test
        assert 'degrees_of_freedom' in overid_test
        assert 'interpretation' in overid_test

    def test_iv_exactly_identified_no_overid_test(self, iv_strong_data):
        """Test that overidentification test returns None when exactly identified."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']  # One instrument, one endogenous var
        )
        model.estimate()

        overid_test = model.test_overidentification()

        # Should return None for exactly identified model
        assert overid_test is None

    def test_iv_reduced_form(self, iv_strong_data):
        """Test reduced-form estimation."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )

        reduced_form = model.estimate_reduced_form()

        assert 'instrument_coefficients' in reduced_form
        assert 'nobs' in reduced_form
        assert 'rsquared' in reduced_form

        # Should have coefficient for instrument z
        assert 'z' in reduced_form['instrument_coefficients']
        assert 'coefficient' in reduced_form['instrument_coefficients']['z']
        assert 'std_error' in reduced_form['instrument_coefficients']['z']
        assert 'pvalue' in reduced_form['instrument_coefficients']['z']

    def test_iv_with_covariates(self, iv_strong_data):
        """Test IV with additional covariates."""
        # Add a covariate
        data = iv_strong_data.copy()
        data['X_control'] = np.random.normal(0, 1, len(data))

        model = InstrumentalVariables(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            covariates=['X_control']
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert 'x' in results['coefficients']

    def test_iv_fit_statistics(self, iv_strong_data):
        """Test that fit statistics are included."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        results = model.estimate()

        assert 'fit_stats' in results
        assert 'rsquared' in results['fit_stats']
        assert 'first_stage_f' in results['fit_stats']
        assert 'first_stage_rsquared' in results['fit_stats']

    def test_iv_diagnostics(self, iv_strong_data):
        """Test that diagnostics are included."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        results = model.estimate()

        assert 'diagnostics' in results
        assert 'hc_type' in results['diagnostics']
        assert 'n_instruments' in results['diagnostics']
        assert 'is_overidentified' in results['diagnostics']

        assert results['diagnostics']['n_instruments'] == 1
        assert results['diagnostics']['is_overidentified'] is False

    def test_iv_summary(self, iv_strong_data):
        """Test summary generation."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'First Stage' in summary
        assert 'Weak Instrument' in summary


class TestIVEdgeCases:
    """Edge case tests for IV."""

    def test_iv_with_missing_values(self, iv_strong_data):
        """Test handling of missing values."""
        data = iv_strong_data.copy()
        # Introduce some missing values
        data.loc[data.index[:10], 'y'] = np.nan
        data.loc[data.index[20:30], 'x'] = np.nan

        model = InstrumentalVariables(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        results = model.estimate()

        # Should work with fewer observations
        assert results['nobs'] < len(iv_strong_data)
        assert 'coefficients' in results

    def test_iv_requires_estimate_before_summary(self):
        """Test that summary() fails before estimate()."""
        data = pd.DataFrame({
            'y': np.random.normal(0, 1, 100),
            'x': np.random.normal(0, 1, 100),
            'z': np.random.normal(0, 1, 100)
        })

        model = InstrumentalVariables(
            data=data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )

        with pytest.raises(ValueError, match="Model not estimated"):
            model.summary()

    def test_iv_validates_columns(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'x': [1, 2, 3, 4, 5]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            InstrumentalVariables(
                data=data,
                outcome='y',
                treatment='x',
                instruments=['z']  # z is missing
            )

    def test_iv_requires_instruments(self):
        """Test that at least one instrument is required."""
        data = pd.DataFrame({
            'y': [1, 2, 3, 4, 5],
            'x': [1, 2, 3, 4, 5]
        })

        with pytest.raises(ValueError, match="At least one instrument is required"):
            InstrumentalVariables(
                data=data,
                outcome='y',
                treatment='x',
                instruments=[]  # No instruments
            )

    def test_iv_model_type(self, iv_strong_data):
        """Test that model_type is correctly set."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z']
        )
        results = model.estimate()

        assert results['model_type'] == 'iv'

    def test_iv_multiple_instruments(self, iv_overidentified_data):
        """Test IV with multiple instruments."""
        model = InstrumentalVariables(
            data=iv_overidentified_data,
            outcome='y',
            treatment='x',
            instruments=['z1', 'z2']
        )
        results = model.estimate()

        assert 'coefficients' in results
        assert results['diagnostics']['n_instruments'] == 2
        assert results['diagnostics']['is_overidentified'] is True
