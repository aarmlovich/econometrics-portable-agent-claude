"""Specification tests for regression models.

Includes:
- RESET test for functional form misspecification (Wooldridge, Ch. 6, p.124-125)
- Variance Inflation Factors (VIF) for multicollinearity (Wooldridge, Ch. 4)

Reference:
Wooldridge, J.M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
MIT Press.
"""

from typing import Dict, List, Optional, Union, Any
import numpy as np
import pandas as pd
from scipy import stats
import warnings


def reset_test(
    y: Union[np.ndarray, pd.Series],
    X: Union[np.ndarray, pd.DataFrame],
    fitted_values: Optional[np.ndarray] = None,
    power_terms: List[int] = [2, 3]
) -> Dict[str, Any]:
    """Ramsey's RESET test for functional form misspecification.

    Tests H0: Model is correctly specified (no omitted nonlinear terms).

    The test adds powers of fitted values (y-hat^2, y-hat^3, etc.) to the
    regression and tests their joint significance. Rejection suggests
    functional form misspecification.

    Reference: Wooldridge, Ch. 6, Section 6.2.3, p.124-125

    Args:
        y: Dependent variable (n,)
        X: Independent variables (n, k). Should include constant if desired.
        fitted_values: Pre-computed fitted values. If None, computed via OLS.
        power_terms: Powers of fitted values to include. Default [2, 3].

    Returns:
        Dictionary with:
            - f_statistic: F-statistic for joint significance of power terms
            - f_pvalue: P-value of F-test
            - df: Degrees of freedom (numerator, denominator)
            - reject_h0: True if p < 0.05 (misspecification detected)
            - interpretation: Text interpretation
            - citation: Wooldridge reference
    """
    # Convert to numpy arrays
    y = np.asarray(y).flatten()
    X = np.asarray(X)

    if X.ndim == 1:
        X = X.reshape(-1, 1)

    n, k = X.shape

    # Step 1: Estimate original model if fitted values not provided
    if fitted_values is None:
        # OLS: beta = (X'X)^(-1) X'y
        try:
            XtX_inv = np.linalg.inv(X.T @ X)
            beta = XtX_inv @ X.T @ y
            fitted_values = X @ beta
        except np.linalg.LinAlgError:
            return {
                'f_statistic': np.nan,
                'f_pvalue': np.nan,
                'df': (len(power_terms), n - k - len(power_terms)),
                'reject_h0': False,
                'interpretation': 'RESET test failed: singular matrix',
                'citation': 'Wooldridge, Ch. 6, Section 6.2.3, p.124-125'
            }

    # Step 2: Add powers of fitted values
    # y_hat^2, y_hat^3, etc.
    power_cols = []
    for p in power_terms:
        power_cols.append(fitted_values ** p)

    # Augmented design matrix
    X_aug = np.column_stack([X] + power_cols)
    q = len(power_terms)  # Number of restrictions

    # Step 3: Estimate augmented model
    try:
        XtX_aug_inv = np.linalg.inv(X_aug.T @ X_aug)
        beta_aug = XtX_aug_inv @ X_aug.T @ y
        residuals_aug = y - X_aug @ beta_aug
        ssr_aug = residuals_aug.T @ residuals_aug

        # Unrestricted R-squared
        sst = np.sum((y - np.mean(y)) ** 2)
        r2_aug = 1 - ssr_aug / sst

        # Restricted model (original) R-squared
        residuals_orig = y - fitted_values
        ssr_orig = residuals_orig.T @ residuals_orig
        r2_orig = 1 - ssr_orig / sst

    except np.linalg.LinAlgError:
        return {
            'f_statistic': np.nan,
            'f_pvalue': np.nan,
            'df': (q, n - k - q),
            'reject_h0': False,
            'interpretation': 'RESET test failed: singular augmented matrix',
            'citation': 'Wooldridge, Ch. 6, Section 6.2.3, p.124-125'
        }

    # Step 4: F-test for joint significance of power terms
    # F = [(R2_aug - R2_orig) / q] / [(1 - R2_aug) / (n - k - q)]
    df_num = q
    df_denom = n - k - q

    if r2_aug >= 1.0:
        f_stat = np.inf
    else:
        f_stat = ((r2_aug - r2_orig) / q) / ((1 - r2_aug) / df_denom)

    f_pvalue = 1 - stats.f.cdf(f_stat, df_num, df_denom)

    reject = f_pvalue < 0.05

    interpretation = (
        f"RESET test: F({df_num}, {df_denom}) = {f_stat:.3f}, p = {f_pvalue:.4f}. "
    )
    if reject:
        interpretation += (
            "Reject H0: Evidence of functional form misspecification. "
            "Consider adding nonlinear terms (squared, interactions) or "
            "transforming the dependent variable."
        )
    else:
        interpretation += (
            "Fail to reject H0: No evidence of functional form misspecification."
        )

    return {
        'f_statistic': float(f_stat),
        'f_pvalue': float(f_pvalue),
        'df': (df_num, df_denom),
        'reject_h0': bool(reject),
        'interpretation': interpretation,
        'citation': 'Wooldridge, Ch. 6, Section 6.2.3, p.124-125'
    }


def variance_inflation_factors(
    X: Union[np.ndarray, pd.DataFrame],
    variable_names: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Compute Variance Inflation Factors (VIF) for multicollinearity detection.

    VIF measures how much the variance of an estimated coefficient is increased
    due to multicollinearity. VIF_j = 1 / (1 - R_j^2), where R_j^2 is from
    regressing X_j on all other X variables.

    Thresholds (Wooldridge, Ch. 4):
    - VIF < 5: No concern
    - VIF 5-10: Moderate multicollinearity
    - VIF > 10: High multicollinearity, consider remedial action

    Args:
        X: Independent variables (n, k). Can include constant (will be excluded).
        variable_names: Names for variables. If None, uses X0, X1, etc.

    Returns:
        Dictionary with:
            - vif: Dict mapping variable names to VIF values
            - max_vif: Maximum VIF value
            - mean_vif: Mean VIF value (excluding constant)
            - high_vif_vars: Variables with VIF > 10
            - interpretation: Text interpretation
            - citation: Wooldridge reference
    """
    # Convert to numpy array
    X = np.asarray(X)

    if X.ndim == 1:
        X = X.reshape(-1, 1)

    n, k = X.shape

    # Set variable names
    if variable_names is None:
        if hasattr(X, 'columns'):
            variable_names = list(X.columns)
        else:
            variable_names = [f'X{i}' for i in range(k)]

    # Detect and exclude constant column (all same value)
    non_const_mask = np.std(X, axis=0) > 1e-10
    X_no_const = X[:, non_const_mask]
    names_no_const = [n for n, m in zip(variable_names, non_const_mask) if m]

    if X_no_const.shape[1] == 0:
        return {
            'vif': {},
            'max_vif': np.nan,
            'mean_vif': np.nan,
            'high_vif_vars': [],
            'interpretation': 'No non-constant variables to test',
            'citation': 'Wooldridge, Ch. 4'
        }

    # Calculate VIF for each variable
    vif_values = {}
    k_nc = X_no_const.shape[1]

    for j in range(k_nc):
        # Regress X_j on all other X variables
        y_j = X_no_const[:, j]
        X_others = np.delete(X_no_const, j, axis=1)

        # Add constant to other variables
        X_others_c = np.column_stack([np.ones(n), X_others])

        try:
            # OLS R-squared
            XtX_inv = np.linalg.inv(X_others_c.T @ X_others_c)
            beta = XtX_inv @ X_others_c.T @ y_j
            fitted = X_others_c @ beta
            ss_res = np.sum((y_j - fitted) ** 2)
            ss_tot = np.sum((y_j - np.mean(y_j)) ** 2)

            if ss_tot < 1e-10:
                r2_j = 0  # Constant variable
            else:
                r2_j = 1 - ss_res / ss_tot

            # VIF = 1 / (1 - R^2)
            if r2_j >= 1.0:
                vif_j = np.inf
            else:
                vif_j = 1.0 / (1.0 - r2_j)

        except np.linalg.LinAlgError:
            vif_j = np.inf

        vif_values[names_no_const[j]] = vif_j

    # Summary statistics
    vif_array = np.array(list(vif_values.values()))
    vif_array_finite = vif_array[np.isfinite(vif_array)]

    max_vif = float(np.max(vif_array)) if len(vif_array) > 0 else np.nan
    mean_vif = float(np.mean(vif_array_finite)) if len(vif_array_finite) > 0 else np.nan

    # Identify high VIF variables (> 10)
    high_vif_vars = [name for name, vif in vif_values.items() if vif > 10]

    # Interpretation
    if len(high_vif_vars) == 0:
        if max_vif > 5:
            interpretation = (
                f"Moderate multicollinearity detected. Max VIF = {max_vif:.2f}. "
                "Consider monitoring for stability."
            )
        else:
            interpretation = (
                f"No concerning multicollinearity. Max VIF = {max_vif:.2f}. "
                "All VIF values below 5."
            )
    else:
        interpretation = (
            f"High multicollinearity detected. Variables with VIF > 10: {high_vif_vars}. "
            f"Max VIF = {max_vif:.2f}. Consider: (1) dropping a collinear variable, "
            "(2) combining variables, or (3) using ridge regression."
        )

    return {
        'vif': {k: float(v) for k, v in vif_values.items()},
        'max_vif': max_vif,
        'mean_vif': mean_vif,
        'high_vif_vars': high_vif_vars,
        'interpretation': interpretation,
        'citation': 'Wooldridge, Ch. 4'
    }


def condition_number(X: Union[np.ndarray, pd.DataFrame]) -> Dict[str, Any]:
    """Compute condition number for multicollinearity detection.

    The condition number is the ratio of the largest to smallest singular value
    of X. High condition numbers indicate near-singularity.

    Thresholds:
    - κ < 30: No concern
    - κ 30-100: Moderate multicollinearity
    - κ > 100: Severe multicollinearity

    Args:
        X: Design matrix (n, k)

    Returns:
        Dictionary with condition number and interpretation
    """
    X = np.asarray(X)

    if X.ndim == 1:
        X = X.reshape(-1, 1)

    # Compute condition number via SVD
    try:
        singular_values = np.linalg.svd(X, compute_uv=False)
        if singular_values[-1] < 1e-15:
            cond = np.inf
        else:
            cond = singular_values[0] / singular_values[-1]
    except np.linalg.LinAlgError:
        cond = np.inf

    # Interpretation
    if cond < 30:
        interpretation = f"Condition number = {cond:.1f}. No multicollinearity concern."
    elif cond < 100:
        interpretation = (
            f"Condition number = {cond:.1f}. Moderate multicollinearity. "
            "Monitor coefficient stability."
        )
    else:
        interpretation = (
            f"Condition number = {cond:.1f}. Severe multicollinearity. "
            "Consider remedial measures."
        )

    return {
        'condition_number': float(cond),
        'interpretation': interpretation
    }


__all__ = ['reset_test', 'variance_inflation_factors', 'condition_number']
