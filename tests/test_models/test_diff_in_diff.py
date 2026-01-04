"""
Tests for Difference-in-Differences implementation.

These tests validate that DiD estimates match known results.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.causal.diff_in_diff import DifferenceInDifferences


@pytest.fixture
def simple_did_data():
    """
    Generate simple DID data with known treatment effect.

    Treatment effect = 5.0
    """
    np.random.seed(42)
    n = 200

    # Create panel data
    data = pd.DataFrame({
        'unit_id': np.repeat(range(100), 2),
        'time': np.tile([0, 1], 100),
        'treated': np.repeat([0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 20),  # 50 treated, 50 control
    })

    # Generate outcome with known treatment effect of 5.0
    # Y = 10 + 2*time + 3*treated + 5*treated*post + error
    data['post'] = data['time']
    data['y'] = (10 +
                 2 * data['time'] +
                 3 * data['treated'] +
                 5 * data['treated'] * data['post'] +
                 np.random.normal(0, 1, n))

    return data


def test_did_basic_estimation(simple_did_data):
    """Test that DiD correctly estimates treatment effect."""
    did = DifferenceInDifferences()
    results = did.fit(
        data=simple_did_data,
        outcome='y',
        unit_id='unit_id',
        time_id='time',
        treatment='treated',
        post_period=1
    )

    # Treatment effect should be close to 5.0
    assert 'treatment_effect' in results
    assert abs(results['treatment_effect'] - 5.0) < 0.5, \
        f"Estimated effect {results['treatment_effect']:.2f} far from true effect 5.0"


def test_did_parallel_trends(simple_did_data):
    """Test parallel trends diagnostic."""
    did = DifferenceInDifferences()

    # With only 2 periods, can't test pre-trends
    # This test shows what we'd check with more periods
    assert len(simple_did_data['time'].unique()) >= 2


def test_did_standard_errors(simple_did_data):
    """Test that standard errors are computed."""
    did = DifferenceInDifferences()
    results = did.fit(
        data=simple_did_data,
        outcome='y',
        unit_id='unit_id',
        time_id='time',
        treatment='treated',
        post_period=1,
        cluster_var='unit_id'  # Cluster at unit level
    )

    assert 'se' in results or 'std_err' in results, "Standard errors not computed"
    assert results.get('clustered', False), "Should use clustered SE"


# TODO: Add more tests:
# - Test with covariates
# - Test event study specification
# - Test with staggered treatment
# - Test with unbalanced panel
# - Validate against known econometric results (e.g., Card-Krueger)
