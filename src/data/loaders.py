"""Data loading utilities for various file formats."""

from pathlib import Path
from typing import Optional, Union
import pandas as pd


def load_data(
    file_path: Union[str, Path],
    file_type: Optional[str] = None,
    **kwargs
) -> pd.DataFrame:
    """Load data from various file formats.
    
    Supports CSV, Parquet, Stata (.dta), and Excel files. Automatically
    detects file type from extension if not specified.
    
    Args:
        file_path: Path to the data file
        file_type: File type ('csv', 'parquet', 'stata', 'excel').
                   If None, inferred from file extension.
        **kwargs: Additional arguments passed to pandas read functions
        
    Returns:
        DataFrame containing the loaded data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file type is not supported
        
    Examples:
        >>> data = load_data("data.csv")
        >>> data = load_data("data.parquet")
        >>> data = load_data("data.dta", encoding='latin-1')
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Determine file type from extension if not specified
    if file_type is None:
        extension = file_path.suffix.lower()
        if extension == '.csv':
            file_type = 'csv'
        elif extension in ['.parquet', '.pq']:
            file_type = 'parquet'
        elif extension == '.dta':
            file_type = 'stata'
        elif extension in ['.xlsx', '.xls']:
            file_type = 'excel'
        else:
            raise ValueError(
                f"Unsupported file type: {extension}. "
                "Supported formats: .csv, .parquet, .dta, .xlsx, .xls"
            )
    
    # Load data based on file type
    if file_type == 'csv':
        encoding = kwargs.pop('encoding', 'utf-8')
        return pd.read_csv(file_path, encoding=encoding, **kwargs)
    elif file_type == 'parquet':
        return pd.read_parquet(file_path, **kwargs)
    elif file_type == 'stata':
        encoding = kwargs.pop('encoding', 'latin-1')
        return pd.read_stata(file_path, encoding=encoding, **kwargs)
    elif file_type == 'excel':
        return pd.read_excel(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


def validate_data_structure(
    data: pd.DataFrame,
    required_columns: list[str],
    min_observations: int = 10
) -> dict[str, Union[bool, list[str]]]:
    """Validate that data structure meets basic requirements.
    
    Args:
        data: DataFrame to validate
        required_columns: List of required column names
        min_observations: Minimum number of observations required
        
    Returns:
        Dictionary with validation results:
            - valid: Boolean indicating if data passes validation
            - issues: List of issues found (empty if valid)
    """
    issues = []
    
    # Check if DataFrame is empty
    if len(data) == 0:
        issues.append("DataFrame is empty")
    
    # Check minimum observations
    if len(data) < min_observations:
        issues.append(
            f"Insufficient observations: {len(data)} < {min_observations}"
        )
    
    # Check required columns
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        issues.append(f"Missing required columns: {missing_columns}")
    
    return {
        "valid": len(issues) == 0,
        "issues": issues
    }

