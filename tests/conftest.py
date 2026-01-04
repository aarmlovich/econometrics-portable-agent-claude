"""
Shared test fixtures for econometrics agent tests.

All fixtures generate synthetic data with known true effects
to validate that models recover the correct parameters.
"""
import pytest
import numpy as np
import pandas as pd


# =============================================================================
# Panel Data Fixtures (DiD, Fixed Effects)
# =============================================================================

@pytest.fixture
def panel_did_data():
    """
    Generate panel data for DiD testing with known treatment effect.

    DGP: Y_it = 10 + 2*time + 3*treated + 5*treated*post + unit_fe + error

    True treatment effect (DiD coefficient) = 5.0
    """
    np.random.seed(42)
    n_units = 100
    n_periods = 4
    treatment_period = 2  # Treatment starts at period 2

    # Create panel structure
    units = np.repeat(range(n_units), n_periods)
    times = np.tile(range(n_periods), n_units)

    # 50 treated, 50 control units
    treated = np.repeat([0] * 50 + [1] * 50, n_periods)
    post = (times >= treatment_period).astype(int)

    # Unit fixed effects
    unit_fe = np.repeat(np.random.normal(0, 2, n_units), n_periods)

    # Generate outcome with known DGP
    y = (10 +
         2 * times +
         3 * treated +
         5 * treated * post +  # True DiD effect = 5.0
         unit_fe +
         np.random.normal(0, 1, n_units * n_periods))

    return pd.DataFrame({
        'unit_id': units,
        'time': times,
        'treated': treated,
        'post': post,
        'y': y
    })


@pytest.fixture
def panel_fe_data():
    """
    Generate panel data for fixed effects testing.

    DGP: Y_it = 2*X1 + 3*X2 + unit_fe + time_fe + error

    True coefficients: X1=2.0, X2=3.0
    """
    np.random.seed(42)
    n_units = 50
    n_periods = 5

    units = np.repeat(range(n_units), n_periods)
    times = np.tile(range(n_periods), n_units)

    # Covariates (time-varying)
    X1 = np.random.normal(0, 1, n_units * n_periods)
    X2 = np.random.normal(0, 1, n_units * n_periods)

    # Fixed effects
    unit_fe = np.repeat(np.random.normal(0, 2, n_units), n_periods)
    time_fe = np.tile(np.random.normal(0, 1, n_periods), n_units)

    # Generate outcome
    y = (2 * X1 +  # True coef = 2.0
         3 * X2 +  # True coef = 3.0
         unit_fe +
         time_fe +
         np.random.normal(0, 0.5, n_units * n_periods))

    return pd.DataFrame({
        'entity_id': units,
        'year': times,
        'X1': X1,
        'X2': X2,
        'y': y
    })


# =============================================================================
# Cross-Sectional Data Fixtures (OLS)
# =============================================================================

@pytest.fixture
def ols_data():
    """
    Generate cross-sectional data for OLS testing.

    DGP: Y = 5 + 2*X1 + 3*X2 - 1*X3 + error

    True coefficients: const=5.0, X1=2.0, X2=3.0, X3=-1.0
    """
    np.random.seed(42)
    n = 500

    X1 = np.random.normal(0, 1, n)
    X2 = np.random.normal(0, 1, n)
    X3 = np.random.normal(0, 1, n)

    y = (5 +        # True intercept = 5.0
         2 * X1 +   # True coef = 2.0
         3 * X2 +   # True coef = 3.0
         -1 * X3 +  # True coef = -1.0
         np.random.normal(0, 1, n))

    return pd.DataFrame({
        'y': y,
        'X1': X1,
        'X2': X2,
        'X3': X3
    })


@pytest.fixture
def ols_heteroskedastic_data():
    """
    Generate data with heteroskedasticity for robust SE testing.

    DGP: Y = 2 + 3*X + error, where Var(error) = X^2
    """
    np.random.seed(42)
    n = 500

    X = np.random.uniform(1, 5, n)
    error = np.random.normal(0, 1, n) * X  # Heteroskedastic errors
    y = 2 + 3 * X + error

    return pd.DataFrame({
        'y': y,
        'x': X
    })


@pytest.fixture
def clustered_data():
    """
    Generate clustered data for clustered SE testing.

    100 clusters with 10 observations each.
    """
    np.random.seed(42)
    n_clusters = 100
    obs_per_cluster = 10
    n = n_clusters * obs_per_cluster

    cluster_ids = np.repeat(range(n_clusters), obs_per_cluster)
    cluster_effects = np.repeat(np.random.normal(0, 2, n_clusters), obs_per_cluster)

    X = np.random.normal(0, 1, n)
    y = 2 + 3 * X + cluster_effects + np.random.normal(0, 1, n)

    return pd.DataFrame({
        'y': y,
        'x': X,
        'cluster_id': cluster_ids
    })


# =============================================================================
# Instrumental Variables Fixtures
# =============================================================================

@pytest.fixture
def iv_strong_data():
    """
    Generate IV data with strong instruments (F > 20).

    DGP:
    - First stage: X = 0.8*Z + error_x  (strong instrument)
    - Second stage: Y = 5 + 2*X + error_y (true effect = 2.0)
    - Endogeneity: corr(error_x, error_y) = 0.5
    """
    np.random.seed(42)
    n = 1000

    # Instrument
    Z = np.random.normal(0, 1, n)

    # Correlated errors (endogeneity)
    error_common = np.random.normal(0, 1, n)
    error_x = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)
    error_y = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)

    # First stage (strong: coefficient = 0.8)
    X = 0.8 * Z + error_x

    # Second stage
    Y = 5 + 2 * X + error_y  # True effect = 2.0

    return pd.DataFrame({
        'y': Y,
        'x': X,
        'z': Z
    })


@pytest.fixture
def iv_weak_data():
    """
    Generate IV data with weak instruments (F < 10).

    DGP:
    - First stage: X = 0.1*Z + error_x  (weak instrument)
    - Second stage: Y = 5 + 2*X + error_y
    """
    np.random.seed(42)
    n = 500

    Z = np.random.normal(0, 1, n)

    error_common = np.random.normal(0, 1, n)
    error_x = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)
    error_y = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)

    # First stage (weak: coefficient = 0.1)
    X = 0.1 * Z + error_x

    Y = 5 + 2 * X + error_y

    return pd.DataFrame({
        'y': Y,
        'x': X,
        'z': Z
    })


@pytest.fixture
def iv_overidentified_data():
    """
    Generate IV data with multiple instruments (overidentified).

    Two valid instruments Z1, Z2.
    """
    np.random.seed(42)
    n = 1000

    Z1 = np.random.normal(0, 1, n)
    Z2 = np.random.normal(0, 1, n)

    error_common = np.random.normal(0, 1, n)
    error_x = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)
    error_y = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n)

    # First stage with two instruments
    X = 0.5 * Z1 + 0.4 * Z2 + error_x

    Y = 5 + 2 * X + error_y

    return pd.DataFrame({
        'y': Y,
        'x': X,
        'z1': Z1,
        'z2': Z2
    })


# =============================================================================
# Regression Discontinuity Fixtures
# =============================================================================

@pytest.fixture
def rd_data():
    """
    Generate RD data with known discontinuity.

    DGP: Y = 2 + 0.5*R + 3*D + error
    where D = 1(R >= 0), R is the running variable

    True treatment effect at cutoff = 3.0
    """
    np.random.seed(42)
    n = 1000

    # Running variable centered at 0
    R = np.random.uniform(-5, 5, n)

    # Treatment indicator
    D = (R >= 0).astype(int)

    # Outcome with discontinuity
    Y = 2 + 0.5 * R + 3 * D + np.random.normal(0, 1, n)  # True effect = 3.0

    return pd.DataFrame({
        'y': Y,
        'running': R,
        'treatment': D
    })


@pytest.fixture
def rd_nonlinear_data():
    """
    Generate RD data with nonlinear relationship.

    DGP: Y = 2 + 0.5*R + 0.1*R^2 + 3*D + error
    """
    np.random.seed(42)
    n = 1000

    R = np.random.uniform(-5, 5, n)
    D = (R >= 0).astype(int)

    Y = 2 + 0.5 * R + 0.1 * R**2 + 3 * D + np.random.normal(0, 1, n)

    return pd.DataFrame({
        'y': Y,
        'running': R,
        'treatment': D
    })


# =============================================================================
# Matching Fixtures
# =============================================================================

@pytest.fixture
def matching_data():
    """
    Generate data for matching/propensity score estimation.

    DGP:
    - Treatment assignment: P(D=1) = logit(0.5*X1 + 0.3*X2)
    - Outcome: Y = 2 + X1 + X2 + 3*D + error

    True ATE = 3.0
    """
    np.random.seed(42)
    n = 1000

    # Covariates
    X1 = np.random.normal(0, 1, n)
    X2 = np.random.normal(0, 1, n)

    # Treatment assignment (selection on observables)
    propensity = 1 / (1 + np.exp(-(0.5 * X1 + 0.3 * X2)))
    D = (np.random.uniform(0, 1, n) < propensity).astype(int)

    # Outcome with treatment effect
    Y = 2 + X1 + X2 + 3 * D + np.random.normal(0, 1, n)  # True ATE = 3.0

    return pd.DataFrame({
        'y': Y,
        'treatment': D,
        'X1': X1,
        'X2': X2
    })


@pytest.fixture
def matching_unbalanced_data():
    """
    Generate data with imbalanced treatment/control groups.

    10% treated, 90% control.
    """
    np.random.seed(42)
    n = 1000

    X1 = np.random.normal(0, 1, n)
    X2 = np.random.normal(0, 1, n)

    # Strong selection into treatment
    propensity = 1 / (1 + np.exp(-(- 2 + 0.5 * X1 + 0.3 * X2)))
    D = (np.random.uniform(0, 1, n) < propensity).astype(int)

    Y = 2 + X1 + X2 + 3 * D + np.random.normal(0, 1, n)

    return pd.DataFrame({
        'y': Y,
        'treatment': D,
        'X1': X1,
        'X2': X2
    })


# =============================================================================
# Panel IV Fixtures
# =============================================================================

@pytest.fixture
def panel_iv_data():
    """
    Generate panel data for panel IV testing with known treatment effect.

    DGP:
    - First stage: X_it = 0.7*Z_it + α_i + u_it (strong instrument)
    - Second stage: Y_it = 2*X_it + α_i + γ_t + ε_it (true effect = 2.0)
    - Endogeneity: corr(u_it, ε_it) = 0.5

    True IV effect = 2.0
    """
    np.random.seed(42)
    n_units = 50
    n_periods = 5

    # Create panel structure
    units = np.repeat(range(n_units), n_periods)
    times = np.tile(range(n_periods), n_units)

    # Instrument (varies over time)
    Z = np.random.normal(0, 1, n_units * n_periods)

    # Fixed effects
    unit_fe = np.repeat(np.random.normal(0, 2, n_units), n_periods)
    time_fe = np.tile(np.random.normal(0, 1, n_periods), n_units)

    # Correlated errors (endogeneity)
    error_common = np.random.normal(0, 1, n_units * n_periods)
    error_x = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n_units * n_periods)
    error_y = 0.5 * error_common + np.sqrt(1 - 0.5**2) * np.random.normal(0, 1, n_units * n_periods)

    # First stage (strong: coefficient = 0.7)
    X = 0.7 * Z + unit_fe + error_x

    # Second stage (true effect = 2.0)
    Y = 2 * X + unit_fe + time_fe + error_y

    return pd.DataFrame({
        'entity_id': units,
        'year': times,
        'y': Y,
        'x': X,
        'z': Z
    })


# =============================================================================
# True Values for Validation
# =============================================================================

@pytest.fixture
def true_effects():
    """
    Dictionary of true effects for validation.

    Use these to assert that estimated coefficients are within tolerance.
    """
    return {
        'did_effect': 5.0,
        'fe_X1': 2.0,
        'fe_X2': 3.0,
        'ols_const': 5.0,
        'ols_X1': 2.0,
        'ols_X2': 3.0,
        'ols_X3': -1.0,
        'iv_effect': 2.0,
        'rd_effect': 3.0,
        'matching_ate': 3.0,
        'panel_iv_effect': 2.0,
    }
