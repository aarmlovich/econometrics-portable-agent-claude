"""Utilities for creating comparison tables from multiple model specifications."""

from typing import List, Dict, Any, Optional, Literal, Union
import numpy as np
import pandas as pd
import warnings


def create_comparison_table(
    results_list: List[Dict[str, Any]],
    model_names: List[str],
    variable_names: Optional[List[str]] = None,
    format: Literal['dataframe', 'latex'] = 'dataframe',
    stats_to_include: Optional[List[str]] = None
) -> Union[pd.DataFrame, str]:
    """Create comparison table from multiple model estimation results.
    
    Combines results from multiple specifications into a side-by-side comparison table.
    Supports both dictionary results (from model.estimate()) and statsmodels/linearmodels
    results objects.
    
    Args:
        results_list: List of result dictionaries or model results objects.
                     Each should have 'coefficients', 'std_errors', 'pvalues' keys
                     (for dict) or params/std_errors/pvalues attributes (for results objects)
        model_names: List of names/labels for each specification (must match length of results_list)
        variable_names: Optional list of variable names to include. If None, includes all
                       variables present in any specification
        format: Output format ('dataframe' or 'latex')
        stats_to_include: Optional list of additional statistics to include at bottom.
                         Options: 'rsquared', 'nobs', 'nentities', 'ntime', 'rsquared_within'
                         Default: ['rsquared', 'nobs']
        
    Returns:
        If format='dataframe': DataFrame with variables as rows, specifications as columns
        If format='latex': LaTeX table as string
        
    Raises:
        ValueError: If results_list and model_names have different lengths
        ValueError: If results_list is empty
    """
    if len(results_list) != len(model_names):
        raise ValueError(f"results_list and model_names must have same length, "
                        f"got {len(results_list)} and {len(model_names)}")
    
    if len(results_list) == 0:
        raise ValueError("results_list cannot be empty")
    
    if stats_to_include is None:
        stats_to_include = ['rsquared', 'nobs']
    
    # Convert results objects to dictionaries if needed
    results_dicts = []
    for results in results_list:
        if isinstance(results, dict):
            results_dicts.append(results)
        elif hasattr(results, 'params'):
            # statsmodels or linearmodels results object
            results_dict = {
                'coefficients': results.params.to_dict() if hasattr(results.params, 'to_dict') 
                               else dict(results.params),
                'std_errors': results.std_errors.to_dict() if hasattr(results.std_errors, 'to_dict')
                             else dict(results.std_errors),
                'pvalues': results.pvalues.to_dict() if hasattr(results.pvalues, 'to_dict')
                          else dict(results.pvalues)
            }
            # Add optional statistics
            if hasattr(results, 'rsquared'):
                results_dict['rsquared'] = float(results.rsquared)
            if hasattr(results, 'nobs'):
                results_dict['nobs'] = int(results.nobs)
            if hasattr(results, 'rsquared_within'):
                results_dict['rsquared_within'] = float(results.rsquared_within)
            if hasattr(results, 'entity_info') and hasattr(results.entity_info, 'total'):
                results_dict['nentities'] = int(results.entity_info.total)
            if hasattr(results, 'time_info') and hasattr(results.time_info, 'total'):
                results_dict['ntime'] = int(results.time_info.total)
            results_dicts.append(results_dict)
        else:
            raise ValueError(f"Unsupported results type: {type(results)}")
    
    # Collect all variable names if not specified
    if variable_names is None:
        all_vars = set()
        for results_dict in results_dicts:
            if 'coefficients' in results_dict:
                if isinstance(results_dict['coefficients'], dict):
                    all_vars.update(results_dict['coefficients'].keys())
                elif isinstance(results_dict['coefficients'], np.ndarray):
                    # Try to get from param_names
                    if 'param_names' in results_dict:
                        all_vars.update(results_dict['param_names'])
                    else:
                        warnings.warn("Array coefficients without param_names, skipping")
        variable_names = sorted(list(all_vars))
    
    if not variable_names:
        raise ValueError("No variables found to include in comparison table")
    
    # Build coefficient table
    coef_data = {}
    se_data = {}
    pval_data = {}
    
    for model_name, results_dict in zip(model_names, results_dicts):
        coef_col = []
        se_col = []
        pval_col = []
        
        # Extract coefficients
        if 'coefficients' in results_dict:
            coefs = results_dict['coefficients']
            if isinstance(coefs, dict):
                coef_dict = coefs
            elif isinstance(coefs, np.ndarray):
                if 'param_names' in results_dict:
                    coef_dict = dict(zip(results_dict['param_names'], coefs))
                else:
                    raise ValueError("Array coefficients require 'param_names'")
            else:
                coef_dict = dict(coefs)
        else:
            coef_dict = {}
        
        # Extract standard errors
        if 'std_errors' in results_dict:
            ses = results_dict['std_errors']
            if isinstance(ses, dict):
                se_dict = ses
            elif isinstance(ses, np.ndarray):
                if 'param_names' in results_dict:
                    se_dict = dict(zip(results_dict['param_names'], ses))
                else:
                    raise ValueError("Array std_errors require 'param_names'")
            else:
                se_dict = dict(ses)
        else:
            se_dict = {}
        
        # Extract p-values
        if 'pvalues' in results_dict:
            pvals = results_dict['pvalues']
            if isinstance(pvals, dict):
                pval_dict = pvals
            elif isinstance(pvals, np.ndarray):
                if 'param_names' in results_dict:
                    pval_dict = dict(zip(results_dict['param_names'], pvals))
                else:
                    raise ValueError("Array pvalues require 'param_names'")
            else:
                pval_dict = dict(pvals)
        else:
            pval_dict = {}
        
        # Fill in values for each variable
        for var in variable_names:
            coef_col.append(coef_dict.get(var, np.nan))
            se_col.append(se_dict.get(var, np.nan))
            pval_col.append(pval_dict.get(var, np.nan))
        
        coef_data[model_name] = coef_col
        se_data[model_name] = se_col
        pval_data[model_name] = pval_col
    
    # Create DataFrames
    coef_df = pd.DataFrame(coef_data, index=variable_names)
    se_df = pd.DataFrame(se_data, index=variable_names)
    pval_df = pd.DataFrame(pval_data, index=variable_names)
    
    # Format coefficients with standard errors in parentheses and stars for significance
    formatted_data = {}
    for model_name in model_names:
        formatted_col = []
        for var in variable_names:
            coef = coef_df.loc[var, model_name]
            se = se_df.loc[var, model_name]
            pval = pval_df.loc[var, model_name]
            
            if pd.isna(coef):
                formatted_col.append("")
            else:
                # Format coefficient
                coef_str = f"{coef:.4f}"
                
                # Add stars for significance
                if not pd.isna(pval):
                    if pval < 0.01:
                        stars = "***"
                    elif pval < 0.05:
                        stars = "**"
                    elif pval < 0.10:
                        stars = "*"
                    else:
                        stars = ""
                else:
                    stars = ""
                
                # Format standard error in parentheses
                if not pd.isna(se):
                    se_str = f"({se:.4f})"
                else:
                    se_str = ""
                
                formatted_col.append(f"{coef_str}{stars}\n{se_str}" if se_str else f"{coef_str}{stars}")
        
        formatted_data[model_name] = formatted_col
    
    # Create main table
    table_df = pd.DataFrame(formatted_data, index=variable_names)
    
    # Add statistics at bottom
    stats_rows = {}
    for stat in stats_to_include:
        stat_row = []
        for model_name, results_dict in zip(model_names, results_dicts):
            value = results_dict.get(stat, np.nan)
            if pd.isna(value):
                stat_row.append("")
            else:
                if stat in ['rsquared', 'rsquared_within']:
                    stat_row.append(f"{value:.4f}")
                else:
                    stat_row.append(f"{int(value)}")
        stats_rows[stat] = stat_row
    
    # Append statistics rows
    if stats_rows:
        stats_df = pd.DataFrame(stats_rows, index=model_names).T
        table_df = pd.concat([table_df, stats_df])
    
    # Format output
    if format == 'dataframe':
        return table_df
    elif format == 'latex':
        return _format_latex(table_df, variable_names, stats_to_include)
    else:
        raise ValueError(f"format must be 'dataframe' or 'latex', got {format}")


def _format_latex(table_df: pd.DataFrame, variable_names: List[str], stats_to_include: List[str]) -> str:
    """Format DataFrame as LaTeX table.
    
    Args:
        table_df: DataFrame with formatted values
        variable_names: List of variable names (for labeling)
        stats_to_include: List of statistics included
        
    Returns:
        LaTeX table as string
    """
    lines = []
    lines.append("\\begin{table}[h]")
    lines.append("\\centering")
    lines.append("\\begin{tabular}{l" + "c" * len(table_df.columns) + "}")
    lines.append("\\hline")
    
    # Header
    header = "Variable & " + " & ".join(table_df.columns) + " \\\\"
    lines.append(header)
    lines.append("\\hline")
    
    # Rows
    for idx, row in table_df.iterrows():
        if idx in stats_to_include:
            # Statistics row
            stat_label = idx.replace('_', ' ').title()
            row_str = f"{stat_label} & " + " & ".join(row.astype(str)) + " \\\\"
        else:
            # Variable row
            row_str = f"{idx} & " + " & ".join(row.astype(str)) + " \\\\"
        lines.append(row_str)
    
    lines.append("\\hline")
    lines.append("\\end{tabular}")
    lines.append("\\caption{Comparison of model specifications}")
    lines.append("\\label{tab:comparison}")
    lines.append("\\end{table}")
    
    return "\n".join(lines)


__all__ = ['create_comparison_table']

