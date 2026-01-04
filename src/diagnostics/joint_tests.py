"""Joint hypothesis testing utilities for econometric models."""

from typing import List, Dict, Any, Literal, Union
import numpy as np
import pandas as pd
from scipy import stats
import warnings


def test_joint_significance(
    model_results: Any,
    variable_names: List[str],
    test_type: Literal['F', 'Wald'] = 'F'
) -> Dict[str, Any]:
    """Test joint significance of multiple coefficients.
    
    Tests the null hypothesis that all specified coefficients are jointly zero.
    Works with both statsmodels and linearmodels results.
    
    Args:
        model_results: Model estimation results object. Can be:
            - statsmodels RegressionResults (from OLS.fit())
            - linearmodels PanelResults (from PanelOLS/RandomEffects/PanelIV.fit())
            - Dictionary with keys: 'coefficients', 'std_errors', 'cov'
        variable_names: List of variable names to test (coefficients to test jointly)
        test_type: Type of test ('F' or 'Wald'). F-test is typically preferred
                   for linear models. Wald test is asymptotically equivalent.
        
    Returns:
        Dictionary containing:
            - test_statistic: Test statistic value
            - pvalue: P-value of the test
            - degrees_of_freedom: Degrees of freedom (number of restrictions)
            - null_hypothesis: Description of null hypothesis
            - interpretation: Text interpretation of results
            
    Raises:
        ValueError: If variable_names not found in model results
        TypeError: If model_results type not recognized
    """
    # Extract coefficients and covariance matrix
    if hasattr(model_results, 'params'):
        # statsmodels or linearmodels results object
        params = model_results.params
        if hasattr(model_results, 'cov'):
            cov = model_results.cov
        elif hasattr(model_results, 'cov_params'):
            cov = model_results.cov_params()
        else:
            raise ValueError("Model results must have 'cov' or 'cov_params' attribute")
        
        # Convert to Series if needed
        if isinstance(params, pd.Series):
            param_series = params
        else:
            # Try to get index from params
            if hasattr(params, 'index'):
                param_series = pd.Series(params.values, index=params.index)
            else:
                raise ValueError("Could not extract parameter names from model results")
        
        # Convert covariance to DataFrame if needed
        if isinstance(cov, pd.DataFrame):
            cov_df = cov
        elif isinstance(cov, np.ndarray):
            # Create DataFrame with same index as params
            cov_df = pd.DataFrame(cov, index=param_series.index, columns=param_series.index)
        else:
            raise ValueError("Could not extract covariance matrix from model results")
        
        # Check if variables exist
        missing = [v for v in variable_names if v not in param_series.index]
        if missing:
            raise ValueError(f"Variables not found in model results: {missing}")
        
        # Extract coefficients and covariance for tested variables
        coefs = param_series.loc[variable_names]
        cov_subset = cov_df.loc[variable_names, variable_names]
        
        # Get degrees of freedom
        if hasattr(model_results, 'df_resid'):
            df_resid = model_results.df_resid
        elif hasattr(model_results, 'nobs') and hasattr(model_results, 'df_model'):
            df_resid = model_results.nobs - model_results.df_model - 1
        else:
            # Fallback: assume large sample (use chi-square approximation)
            df_resid = None
        
    elif isinstance(model_results, dict):
        # Dictionary format (like our model.estimate() returns)
        if 'coefficients' not in model_results or 'cov' not in model_results:
            raise ValueError("Dictionary results must contain 'coefficients' and 'cov' keys")
        
        coefs_dict = model_results['coefficients']
        cov_dict = model_results['cov']
        
        # Convert to Series/DataFrame
        if isinstance(coefs_dict, dict):
            param_series = pd.Series(coefs_dict)
        elif isinstance(coefs_dict, np.ndarray):
            # Need parameter names - try to get from variable_names or create index
            if 'param_names' in model_results:
                param_series = pd.Series(coefs_dict, index=model_results['param_names'])
            else:
                raise ValueError("For array coefficients, 'param_names' must be provided")
        else:
            param_series = pd.Series(coefs_dict)
        
        if isinstance(cov_dict, pd.DataFrame):
            cov_df = cov_dict
        elif isinstance(cov_dict, np.ndarray):
            cov_df = pd.DataFrame(cov_dict, index=param_series.index, columns=param_series.index)
        else:
            cov_df = pd.DataFrame(cov_dict, index=param_series.index, columns=param_series.index)
        
        # Check if variables exist
        missing = [v for v in variable_names if v not in param_series.index]
        if missing:
            raise ValueError(f"Variables not found in model results: {missing}")
        
        # Extract coefficients and covariance for tested variables
        coefs = param_series.loc[variable_names]
        cov_subset = cov_df.loc[variable_names, variable_names]
        
        # Degrees of freedom (may not be available in dict format)
        df_resid = model_results.get('df_resid', None)
        
    else:
        raise TypeError(f"Unsupported model_results type: {type(model_results)}")
    
    # Number of restrictions
    k = len(variable_names)
    
    # Compute test statistic
    coefs_array = coefs.values
    cov_array = cov_subset.values
    
    # Check if covariance matrix is invertible
    try:
        cov_inv = np.linalg.inv(cov_array)
    except np.linalg.LinAlgError:
        # Use pseudo-inverse if singular
        warnings.warn("Covariance matrix is singular, using pseudo-inverse")
        cov_inv = np.linalg.pinv(cov_array)
    
    if test_type == 'Wald':
        # Wald test: W = β' * Cov(β)^{-1} * β ~ χ²(k)
        wald_stat = float(coefs_array.T @ cov_inv @ coefs_array)
        pvalue = 1 - stats.chi2.cdf(wald_stat, k)
        test_statistic = wald_stat
        distribution = f"χ²({k})"
        
    elif test_type == 'F':
        # F-test: F = (β' * Cov(β)^{-1} * β) / k ~ F(k, df_resid)
        wald_stat = float(coefs_array.T @ cov_inv @ coefs_array)
        
        if df_resid is not None and df_resid > 0:
            f_stat = wald_stat / k
            pvalue = 1 - stats.f.cdf(f_stat, k, df_resid)
            test_statistic = f_stat
            distribution = f"F({k}, {df_resid})"
        else:
            # Large sample: use chi-square approximation
            pvalue = 1 - stats.chi2.cdf(wald_stat, k)
            test_statistic = wald_stat / k  # Report as F-stat but test as chi-square
            distribution = f"χ²({k}) (large sample approximation)"
            warnings.warn("Degrees of freedom not available, using chi-square approximation")
    
    else:
        raise ValueError(f"test_type must be 'F' or 'Wald', got {test_type}")
    
    # Interpretation
    if pvalue < 0.01:
        interpretation = f"Strongly reject H0 (p < 0.01): Variables are jointly significant"
    elif pvalue < 0.05:
        interpretation = f"Reject H0 (p < 0.05): Variables are jointly significant"
    elif pvalue < 0.10:
        interpretation = f"Reject H0 at 10% level (p < 0.10): Weak evidence of joint significance"
    else:
        interpretation = f"Fail to reject H0 (p ≥ 0.10): No evidence of joint significance"
    
    return {
        'test_statistic': test_statistic,
        'pvalue': float(pvalue),
        'degrees_of_freedom': k,
        'df_resid': df_resid,
        'test_type': test_type,
        'distribution': distribution,
        'null_hypothesis': f"H0: All coefficients in {variable_names} are jointly zero",
        'variables_tested': variable_names,
        'interpretation': interpretation
    }


__all__ = ['test_joint_significance']

