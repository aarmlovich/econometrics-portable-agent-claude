"""
Tests for instrumental variables diagnostics.

These tests validate weak instrument detection and IV estimation.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.instrumental_variables import InstrumentalVariables


class TestWeakInstrumentDetection:
    """Test suite for weak instrument detection."""

    def test_strong_instrument_detection(self, iv_strong_data):
        """Test that strong instruments are correctly identified."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        # Run first stage
        first_stage = model.estimate_first_stage()

        # F-statistic should be high (> 10)
        assert first_stage['f_statistic'] > 10, \
            f"F-statistic {first_stage['f_statistic']:.2f} should be > 10 for strong instrument"

        # Weak instrument test should pass
        weak_test = model.test_weak_instruments()
        assert not weak_test['is_weak'], "Should NOT flag strong instruments as weak"
        assert 'Strong' in weak_test['interpretation']

    def test_weak_instrument_detection(self, iv_weak_data):
        """Test that weak instruments are correctly identified."""
        model = InstrumentalVariables(
            data=iv_weak_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        # Run first stage
        first_stage = model.estimate_first_stage()

        # F-statistic should be low (< 10)
        assert first_stage['f_statistic'] < 10, \
            f"F-statistic {first_stage['f_statistic']:.2f} should be < 10 for weak instrument"

        # Weak instrument test should flag it
        weak_test = model.test_weak_instruments()
        assert weak_test['is_weak'], "Should flag weak instruments"
        assert 'Weak' in weak_test['interpretation'] or 'weak' in weak_test['interpretation'].lower()

    def test_first_stage_returns_required_keys(self, iv_strong_data):
        """Test that first stage returns all required diagnostic information."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        first_stage = model.estimate_first_stage()

        # Check required keys
        required_keys = ['coefficients', 'std_errors', 'pvalues', 'rsquared', 'f_statistic', 'f_pvalue', 'nobs']
        for key in required_keys:
            assert key in first_stage, f"Missing key: {key}"

        # F-statistic and R-squared should be reasonable
        assert first_stage['f_statistic'] >= 0
        assert 0 <= first_stage['rsquared'] <= 1
        assert 0 <= first_stage['f_pvalue'] <= 1


class TestIVEstimation:
    """Test suite for IV (2SLS) estimation."""

    def test_iv_recovers_true_coefficient(self, iv_strong_data, true_effects):
        """Test that IV correctly estimates the true causal effect."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        results = model.estimate()

        # Check required keys (EstimationResult format)
        assert 'coefficients' in results
        assert 'std_errors' in results
        assert 'pvalues' in results
        assert 'ci_lower' in results
        assert 'ci_upper' in results
        assert 'nobs' in results
        assert 'fit_stats' in results
        assert 'first_stage_f' in results['fit_stats']
        assert 'x' in results['coefficients']

        # Coefficient should be close to true value (2.0)
        true_effect = true_effects['iv_effect']
        estimated = results['coefficients']['x']
        assert abs(estimated - true_effect) < 0.5, \
            f"Estimated effect {estimated:.2f} far from true effect {true_effect}"

        # True effect should be within 95% CI
        ci_low = results['ci_lower']['x']
        ci_high = results['ci_upper']['x']
        assert ci_low <= true_effect <= ci_high, \
            f"True effect {true_effect} not in CI [{ci_low:.2f}, {ci_high:.2f}]"

    def test_iv_warns_on_weak_instruments(self, iv_weak_data):
        """Test that IV estimation warns about weak instruments."""
        model = InstrumentalVariables(
            data=iv_weak_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        # Should warn about weak instruments
        with pytest.warns(UserWarning, match="Weak instruments"):
            model.estimate()


class TestOveridentificationTest:
    """Test suite for overidentification tests."""

    def test_overidentification_with_multiple_instruments(self, iv_overidentified_data):
        """Test Sargan overidentification test with multiple instruments."""
        model = InstrumentalVariables(
            data=iv_overidentified_data,
            outcome='y',
            treatment='x',
            instruments=['z1', 'z2'],
            hc_type='HC1'
        )

        model.estimate()
        overid_test = model.test_overidentification()

        # Should return test results (not None for overidentified case)
        assert overid_test is not None

        # Check required keys
        assert 'sargan_statistic' in overid_test
        assert 'pvalue' in overid_test
        assert 'degrees_of_freedom' in overid_test
        assert 'interpretation' in overid_test

        # Degrees of freedom should be # instruments - 1
        assert overid_test['degrees_of_freedom'] == 1  # 2 instruments - 1

        # With valid instruments, p-value should be high (fail to reject null)
        assert overid_test['pvalue'] > 0.05, \
            f"Overid test rejected valid instruments (p={overid_test['pvalue']:.4f})"

    def test_overidentification_exactly_identified(self, iv_strong_data):
        """Test that overidentification test returns None when exactly identified."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],  # One instrument, one treatment = exactly identified
            hc_type='HC1'
        )

        model.estimate()
        overid_test = model.test_overidentification()

        # Should return None for exactly identified case
        assert overid_test is None


class TestReducedForm:
    """Test suite for reduced form estimation."""

    def test_reduced_form_estimation(self, iv_strong_data):
        """Test reduced form (outcome regressed on instruments)."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )

        reduced_form = model.estimate_reduced_form()

        # Check required keys
        assert 'instrument_coefficients' in reduced_form
        assert 'nobs' in reduced_form
        assert 'rsquared' in reduced_form

        # Should have coefficient for the instrument
        assert 'z' in reduced_form['instrument_coefficients']
        z_coef = reduced_form['instrument_coefficients']['z']

        assert 'coefficient' in z_coef
        assert 'std_error' in z_coef
        assert 'pvalue' in z_coef


class TestIVValidation:
    """Test input validation for IV."""

    def test_missing_columns_raises_error(self):
        """Test that missing columns raise ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3],
            'x': [1, 2, 3]
        })

        with pytest.raises(ValueError, match="Missing required columns"):
            InstrumentalVariables(
                data=data,
                outcome='y',
                treatment='x',
                instruments=['z']  # Missing
            )

    def test_no_instruments_raises_error(self):
        """Test that empty instruments list raises ValueError."""
        data = pd.DataFrame({
            'y': [1, 2, 3],
            'x': [1, 2, 3]
        })

        with pytest.raises(ValueError, match="At least one instrument"):
            InstrumentalVariables(
                data=data,
                outcome='y',
                treatment='x',
                instruments=[]
            )

    def test_summary_generation(self, iv_strong_data):
        """Test summary table generation."""
        model = InstrumentalVariables(
            data=iv_strong_data,
            outcome='y',
            treatment='x',
            instruments=['z'],
            hc_type='HC1'
        )
        model.estimate()

        summary = model.summary()
        assert isinstance(summary, str)
        assert len(summary) > 0
        assert 'First Stage' in summary or 'first stage' in summary.lower()
        assert 'Weak Instrument' in summary or 'weak' in summary.lower()


# TODO: Add more tests:
# - Test with covariates
# - Test with multiple endogenous variables
# - Validate against known IV results (e.g., Angrist-Krueger 1991 if data available)
