"""
Tests for instrumental variables diagnostics.
"""
import pytest
import numpy as np
import pandas as pd
from src.diagnostics.iv_diagnostics import first_stage_f_statistic, weak_instrument_test


@pytest.fixture
def strong_iv_data():
    """Generate data with strong instrument (F > 20)."""
    np.random.seed(42)
    n = 500
    z = np.random.normal(0, 1, n)  # Instrument
    x = 2 * z + np.random.normal(0, 1, n)  # Strong first stage
    y = 3 * x + np.random.normal(0, 2, n)  # Outcome

    return pd.DataFrame({'y': y, 'x': x, 'z': z})


@pytest.fixture
def weak_iv_data():
    """Generate data with weak instrument (F < 10)."""
    np.random.seed(42)
    n = 500
    z = np.random.normal(0, 1, n)  # Instrument
    x = 0.1 * z + np.random.normal(0, 1, n)  # Weak first stage
    y = 3 * x + np.random.normal(0, 2, n)  # Outcome

    return pd.DataFrame({'y': y, 'x': x, 'z': z})


def test_strong_instrument_detection(strong_iv_data):
    """Test that strong instruments are correctly identified."""
    f_stat = first_stage_f_statistic(
        data=strong_iv_data,
        endog='x',
        instrument='z'
    )

    assert f_stat > 20, f"F-statistic {f_stat:.2f} should be > 20 for strong instrument"


def test_weak_instrument_detection(weak_iv_data):
    """Test that weak instruments are correctly identified."""
    f_stat = first_stage_f_statistic(
        data=weak_iv_data,
        endog='x',
        instrument='z'
    )

    assert f_stat < 10, f"F-statistic {f_stat:.2f} should be < 10 for weak instrument"


def test_weak_instrument_warning(weak_iv_data):
    """Test that weak instrument test raises warning."""
    result = weak_instrument_test(
        data=weak_iv_data,
        endog='x',
        instrument='z'
    )

    assert result['is_weak'], "Should flag weak instruments"
    assert 'warning' in result or 'message' in result


# TODO: Add more tests:
# - Test with multiple instruments
# - Test overidentification tests
# - Test reduced form
# - Validate against known IV examples (e.g., Angrist-Krueger)
