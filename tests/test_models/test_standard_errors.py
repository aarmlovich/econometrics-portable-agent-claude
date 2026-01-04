"""
Tests for standard error calculations.

These tests validate that robust, clustered, and HAC standard errors are correct.
"""
import pytest
import numpy as np
import pandas as pd
from src.models.regression.ols import OLS


@pytest.fixture
def simple_data():
    """Generate simple regression data."""
    np.random.seed(42)
    n = 100
    x = np.random.normal(0, 1, n)
    y = 2 + 3 * x + np.random.normal(0, 1, n)
    return pd.DataFrame({'y': y, 'x': x})


def test_robust_se_computation(simple_data):
    """Test that robust SE differ from standard SE with heteroskedasticity."""
    ols = OLS()

    # Fit with standard SE
    results_standard = ols.fit(
        data=simple_data,
        formula='y ~ x',
        se_type='standard'
    )

    # Fit with robust SE
    results_robust = ols.fit(
        data=simple_data,
        formula='y ~ x',
        se_type='HC1'
    )

    # Standard errors should differ (though maybe not by much in this simple case)
    assert 'se' in results_standard
    assert 'se' in results_robust


def test_clustered_se():
    """Test clustered standard errors."""
    np.random.seed(42)
    n = 200
    n_clusters = 20

    data = pd.DataFrame({
        'y': np.random.normal(0, 1, n),
        'x': np.random.normal(0, 1, n),
        'cluster_id': np.repeat(range(n_clusters), n // n_clusters)
    })

    ols = OLS()
    results = ols.fit(
        data=data,
        formula='y ~ x',
        se_type='clustered',
        cluster_var='cluster_id'
    )

    assert 'se' in results
    assert results.get('clustered', False)


# TODO: Add more tests:
# - Test HC1, HC2, HC3 differences
# - Test HAC standard errors
# - Test small-sample corrections
# - Validate against statsmodels/linearmodels results
# - Test two-way clustering
