"""Base classes and types for econometric models.

This module provides the foundation for all econometric estimators in the package,
ensuring consistent APIs and result structures across different model types.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Union
from typing_extensions import TypedDict
import pandas as pd
import numpy as np


class EstimationResult(TypedDict, total=False):
    """Standardized result structure for all econometric models.

    All models return results in this format for consistency.
    Not all fields are required - models populate relevant fields.

    Attributes:
        coefficients: Named coefficients {var_name: coefficient_value}
        std_errors: Named standard errors {var_name: se_value}
        pvalues: Named p-values {var_name: pvalue}
        tvalues: Named t-statistics {var_name: tvalue}
        ci_lower: Named lower 95% CI bounds {var_name: lower}
        ci_upper: Named upper 95% CI bounds {var_name: upper}
        nobs: Number of observations
        fit_stats: Fit statistics (rsquared, rsquared_adj, rsquared_within, etc.)
        diagnostics: Model-specific diagnostic information
        model_type: Type of model (e.g., 'ols', 'iv', 'did', 'fe')
    """
    coefficients: Dict[str, float]
    std_errors: Dict[str, float]
    pvalues: Dict[str, float]
    tvalues: Dict[str, float]
    ci_lower: Dict[str, float]
    ci_upper: Dict[str, float]
    nobs: int
    fit_stats: Dict[str, float]
    diagnostics: Dict[str, Any]
    model_type: str


class BaseEconometricModel(ABC):
    """Abstract base class for all econometric models.

    Provides common functionality for data validation, preparation,
    and result formatting. All model classes should inherit from this.

    Attributes:
        data: The input DataFrame (copied to preserve original)
        outcome: Name of the outcome/dependent variable
        results: Raw results from underlying estimation library
        _estimated: Flag indicating if model has been estimated
    """

    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        **kwargs
    ):
        """Initialize base model.

        Args:
            data: DataFrame containing all variables
            outcome: Name of outcome variable
            **kwargs: Additional model-specific arguments
        """
        self.data = data.copy()
        self.outcome = outcome
        self.results = None
        self._estimated = False

    def _validate_columns(
        self,
        required_columns: List[str],
        data: Optional[pd.DataFrame] = None
    ) -> None:
        """Validate that required columns exist in data.

        Args:
            required_columns: List of column names that must be present
            data: DataFrame to check (defaults to self.data)

        Raises:
            ValueError: If any required columns are missing
        """
        df = data if data is not None else self.data
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    def _prepare_data(
        self,
        columns: List[str],
        dropna: bool = True
    ) -> pd.DataFrame:
        """Prepare data for estimation.

        Args:
            columns: List of columns to include
            dropna: If True, drop rows with missing values

        Returns:
            Prepared DataFrame with specified columns
        """
        df = self.data[columns].copy()
        if dropna:
            df = df.dropna()
        return df

    def _format_results_dict(
        self,
        params: Union[pd.Series, np.ndarray],
        bse: Union[pd.Series, np.ndarray],
        pvalues: Union[pd.Series, np.ndarray],
        tvalues: Optional[Union[pd.Series, np.ndarray]] = None,
        conf_int: Optional[pd.DataFrame] = None,
        param_names: Optional[List[str]] = None
    ) -> Dict[str, Dict[str, float]]:
        """Convert estimation results to standardized dictionary format.

        Args:
            params: Coefficient estimates
            bse: Standard errors
            pvalues: P-values
            tvalues: T-statistics (optional)
            conf_int: Confidence intervals DataFrame with columns [0, 1] or ['lower', 'upper']
            param_names: Parameter names (if params is ndarray)

        Returns:
            Dictionary with 'coefficients', 'std_errors', 'pvalues', etc.
        """
        # Get parameter names
        if isinstance(params, pd.Series):
            names = list(params.index)
        elif param_names is not None:
            names = param_names
        else:
            names = [f'x{i}' for i in range(len(params))]

        # Convert to arrays if needed
        params_arr = np.asarray(params)
        bse_arr = np.asarray(bse)
        pvalues_arr = np.asarray(pvalues)

        result = {
            'coefficients': {name: float(params_arr[i]) for i, name in enumerate(names)},
            'std_errors': {name: float(bse_arr[i]) for i, name in enumerate(names)},
            'pvalues': {name: float(pvalues_arr[i]) for i, name in enumerate(names)},
        }

        if tvalues is not None:
            tvalues_arr = np.asarray(tvalues)
            result['tvalues'] = {name: float(tvalues_arr[i]) for i, name in enumerate(names)}

        if conf_int is not None:
            ci_arr = np.asarray(conf_int)
            result['ci_lower'] = {name: float(ci_arr[i, 0]) for i, name in enumerate(names)}
            result['ci_upper'] = {name: float(ci_arr[i, 1]) for i, name in enumerate(names)}

        return result

    @abstractmethod
    def estimate(self) -> EstimationResult:
        """Estimate the model.

        Returns:
            EstimationResult dictionary with standardized structure
        """
        pass

    @abstractmethod
    def summary(self) -> str:
        """Generate a text summary of estimation results.

        Returns:
            Formatted summary string

        Raises:
            ValueError: If model has not been estimated
        """
        pass

    def _check_estimated(self) -> None:
        """Check if model has been estimated.

        Raises:
            ValueError: If model has not been estimated
        """
        if not self._estimated or self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")


def create_estimation_result(
    coefficients: Dict[str, float],
    std_errors: Dict[str, float],
    pvalues: Dict[str, float],
    nobs: int,
    model_type: str,
    tvalues: Optional[Dict[str, float]] = None,
    ci_lower: Optional[Dict[str, float]] = None,
    ci_upper: Optional[Dict[str, float]] = None,
    fit_stats: Optional[Dict[str, float]] = None,
    diagnostics: Optional[Dict[str, Any]] = None
) -> EstimationResult:
    """Helper function to create an EstimationResult dictionary.

    Args:
        coefficients: Named coefficients
        std_errors: Named standard errors
        pvalues: Named p-values
        nobs: Number of observations
        model_type: Type of model
        tvalues: Named t-statistics (optional)
        ci_lower: Named lower CI bounds (optional)
        ci_upper: Named upper CI bounds (optional)
        fit_stats: Fit statistics (optional)
        diagnostics: Diagnostic information (optional)

    Returns:
        EstimationResult dictionary
    """
    result: EstimationResult = {
        'coefficients': coefficients,
        'std_errors': std_errors,
        'pvalues': pvalues,
        'nobs': nobs,
        'model_type': model_type,
    }

    if tvalues is not None:
        result['tvalues'] = tvalues
    if ci_lower is not None:
        result['ci_lower'] = ci_lower
    if ci_upper is not None:
        result['ci_upper'] = ci_upper
    if fit_stats is not None:
        result['fit_stats'] = fit_stats
    else:
        result['fit_stats'] = {}
    if diagnostics is not None:
        result['diagnostics'] = diagnostics
    else:
        result['diagnostics'] = {}

    return result
