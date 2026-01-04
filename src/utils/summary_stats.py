"""Utilities for computing summary statistics by group."""

from typing import List, Dict, Optional, Union
import numpy as np
import pandas as pd


def summary_statistics_by_group(
    data: pd.DataFrame,
    variables: List[str],
    group_by: str,
    group_names: Optional[Dict[Union[int, float, str], str]] = None
) -> pd.DataFrame:
    """Compute summary statistics by group (e.g., treatment/control, time periods).
    
    Provides standardized summary statistics table suitable for reporting.
    Useful for exploratory data analysis before modeling, especially for:
    - Treatment vs. control group comparisons (matching, DiD)
    - Time period comparisons (DiD pre/post periods)
    - Any group-based comparisons
    
    Args:
        data: DataFrame containing variables of interest
        variables: List of variable names to compute statistics for
        group_by: Column name to group by (e.g., treatment indicator, time period)
        group_names: Optional dictionary mapping group values to labels.
                    If None, uses group values as labels.
        
    Returns:
        DataFrame with:
            - Rows: Variables
            - Columns: Groups (with statistics: Mean, Std, Min, Max, Count)
            - Additional columns: Overall statistics (across all groups)
            
    Raises:
        ValueError: If group_by column not in data
        ValueError: If any variable not in data
        ValueError: If variables list is empty
    """
    if group_by not in data.columns:
        raise ValueError(f"group_by column '{group_by}' not found in data")
    
    missing_vars = [v for v in variables if v not in data.columns]
    if missing_vars:
        raise ValueError(f"Variables not found in data: {missing_vars}")
    
    if not variables:
        raise ValueError("variables list cannot be empty")
    
    # Get unique groups
    groups = sorted(data[group_by].dropna().unique())
    
    # Map group values to names
    if group_names is None:
        group_names = {g: str(g) for g in groups}
    else:
        # Ensure all groups have names
        for g in groups:
            if g not in group_names:
                group_names[g] = str(g)
    
    # Compute statistics for each group
    stats_list = []
    
    for var in variables:
        var_data = data[var].dropna()
        
        # Overall statistics
        overall_stats = {
            'Variable': var,
            'Group': 'Overall',
            'Mean': var_data.mean(),
            'Std': var_data.std(),
            'Min': var_data.min(),
            'Max': var_data.max(),
            'Count': len(var_data)
        }
        stats_list.append(overall_stats)
        
        # Statistics by group
        for group_val in groups:
            group_data = data[data[group_by] == group_val][var].dropna()
            
            if len(group_data) == 0:
                # No data for this group
                group_stats = {
                    'Variable': var,
                    'Group': group_names[group_val],
                    'Mean': np.nan,
                    'Std': np.nan,
                    'Min': np.nan,
                    'Max': np.nan,
                    'Count': 0
                }
            else:
                group_stats = {
                    'Variable': var,
                    'Group': group_names[group_val],
                    'Mean': group_data.mean(),
                    'Std': group_data.std(),
                    'Min': group_data.min(),
                    'Max': group_data.max(),
                    'Count': len(group_data)
                }
            stats_list.append(group_stats)
    
    # Create DataFrame
    stats_df = pd.DataFrame(stats_list)
    
    # Pivot to wide format: variables as rows, groups as columns
    # Create multi-level columns for each statistic
    pivot_dfs = []
    for stat in ['Mean', 'Std', 'Min', 'Max', 'Count']:
        pivot_df = stats_df.pivot(index='Variable', columns='Group', values=stat)
        pivot_df.columns = pd.MultiIndex.from_product([[stat], pivot_df.columns])
        pivot_dfs.append(pivot_df)
    
    # Combine
    result_df = pd.concat(pivot_dfs, axis=1)
    
    # Reorder columns: put Overall first, then groups
    if 'Overall' in result_df.columns.levels[1]:
        overall_cols = [col for col in result_df.columns if col[1] == 'Overall']
        group_cols = [col for col in result_df.columns if col[1] != 'Overall']
        # Sort group columns by original group order
        group_order = [group_names[g] for g in groups]
        group_cols_sorted = []
        for group_name in group_order:
            group_cols_sorted.extend([col for col in group_cols if col[1] == group_name])
        result_df = result_df[overall_cols + group_cols_sorted]
    
    return result_df


__all__ = ['summary_statistics_by_group']

