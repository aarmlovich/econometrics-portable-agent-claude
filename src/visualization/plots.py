"""Core plotting functions for econometric models.

Publication-quality visualizations using matplotlib and seaborn.
All plots use colorblind-friendly palettes and sensible defaults.
"""

from typing import Optional, List, Dict, Any, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# Set default style and palette
sns.set_style("whitegrid")
sns.set_palette("colorblind")


def save_figure(
    fig: plt.Figure,
    path: str,
    dpi: int = 300,
    format: str = 'png'
) -> None:
    """Save figure with publication quality settings.

    Args:
        fig: Matplotlib figure to save
        path: File path including extension (e.g., 'figures/plot.png')
                Or base path without extension if you want to use format parameter
        dpi: Dots per inch for raster formats (default: 300)
        format: File format ('png', 'pdf', 'svg') - only used if path has no extension
    """
    # Determine output path and format
    if '.' not in path.split('/')[-1]:
        # No extension in path, use format parameter
        output_path = f"{path}.{format}"
    else:
        # Extension already in path
        output_path = path

    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')


def plot_parallel_trends(
    model: Any,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 6)
) -> plt.Figure:
    """Plot parallel trends for difference-in-differences.

    Shows mean outcome over time for treated and control groups,
    with vertical line at treatment period.

    Args:
        model: DifferenceInDifferences model instance (must have data, outcome,
               treatment, time, unit, treatment_period attributes)
        ax: Optional matplotlib axes to plot on (creates new figure if None)
        figsize: Figure size in inches (width, height)

    Returns:
        Matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    # Get data from model
    data = model.data
    outcome = model.outcome
    treatment = model.treatment
    time_var = model.time
    treatment_period = model.treatment_period

    # Calculate mean outcome by group and time
    treated_data = data[data[treatment] == 1].groupby(time_var)[outcome].mean()
    control_data = data[data[treatment] == 0].groupby(time_var)[outcome].mean()

    # Get colorblind-friendly palette
    colors = sns.color_palette("colorblind")

    # Plot trends
    ax.plot(treated_data.index, treated_data.values,
            marker='o', linewidth=2, markersize=8,
            label='Treated', color=colors[0])
    ax.plot(control_data.index, control_data.values,
            marker='s', linewidth=2, markersize=8,
            label='Control', color=colors[1])

    # Add vertical line at treatment period
    ax.axvline(x=treatment_period, color='gray', linestyle='--',
               linewidth=2, alpha=0.7, label='Treatment starts')

    # Labels and formatting
    ax.set_xlabel('Time Period', fontsize=12)
    ax.set_ylabel(f'Mean {outcome}', fontsize=12)
    ax.set_title('Parallel Trends: Treatment vs Control', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, frameon=True)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig


def plot_event_study(
    coefficients: Dict[int, float],
    ci_lower: Dict[int, float],
    ci_upper: Dict[int, float],
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 6)
) -> plt.Figure:
    """Plot event study coefficients with confidence intervals.

    Shows treatment effects over time relative to treatment period,
    with time=-1 typically normalized to zero.

    Args:
        coefficients: Dictionary mapping relative time to coefficient
        ci_lower: Dictionary mapping relative time to lower CI
        ci_upper: Dictionary mapping relative time to upper CI
        ax: Optional matplotlib axes to plot on
        figsize: Figure size in inches

    Returns:
        Matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    # Sort by time period
    periods = sorted(coefficients.keys())
    coefs = [coefficients[p] for p in periods]
    ci_low = [ci_lower[p] for p in periods]
    ci_high = [ci_upper[p] for p in periods]

    # Get colorblind-friendly color
    colors = sns.color_palette("colorblind")

    # Plot coefficients with error bars
    ax.errorbar(periods, coefs,
                yerr=[np.array(coefs) - np.array(ci_low),
                      np.array(ci_high) - np.array(coefs)],
                fmt='o', markersize=8, linewidth=2, capsize=5,
                color=colors[0], ecolor=colors[0], alpha=0.8)

    # Add horizontal line at zero
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)

    # Add vertical line at time=0 (treatment period)
    ax.axvline(x=0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)

    # Shading for pre/post periods
    ax.axvspan(min(periods), 0, alpha=0.1, color='blue', label='Pre-treatment')
    ax.axvspan(0, max(periods), alpha=0.1, color='red', label='Post-treatment')

    # Labels and formatting
    ax.set_xlabel('Time Relative to Treatment', fontsize=12)
    ax.set_ylabel('Treatment Effect', fontsize=12)
    ax.set_title('Event Study: Dynamic Treatment Effects', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, frameon=True)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig


def plot_rd(
    model: Any,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 6),
    n_bins: int = 20
) -> plt.Figure:
    """Plot regression discontinuity design with binned means and fitted lines.

    Shows outcome vs running variable with discontinuity at cutoff.

    Args:
        model: RegressionDiscontinuity model instance (must be estimated)
        ax: Optional matplotlib axes to plot on
        figsize: Figure size in inches
        n_bins: Number of bins for binned scatter plot

    Returns:
        Matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    # Check model is estimated
    if not model._estimated:
        raise ValueError("Model must be estimated before plotting. Call estimate() first.")

    # Get data from model
    data = model.data
    outcome = model.outcome
    running = model.running
    cutoff = model.cutoff
    bandwidth = model.bandwidth

    # Filter to observations within bandwidth
    data_plot = data[
        (data[running] >= cutoff - bandwidth) &
        (data[running] <= cutoff + bandwidth)
    ].copy()

    if len(data_plot) == 0:
        raise ValueError("No observations within bandwidth for plotting")

    # Separate treated and control
    treated = data_plot[data_plot[running] >= cutoff]
    control = data_plot[data_plot[running] < cutoff]

    # Get colorblind-friendly palette
    colors = sns.color_palette("colorblind")

    # Create binned scatter plot
    # Control side (left of cutoff)
    if len(control) > 0:
        control_bins = pd.cut(control[running], bins=n_bins//2)
        control_binned = control.groupby(control_bins, observed=True).agg({
            running: 'mean',
            outcome: 'mean'
        })
        ax.scatter(control_binned[running], control_binned[outcome],
                  s=100, alpha=0.6, color=colors[1], label='Control (binned)', marker='o')

    # Treated side (right of cutoff)
    if len(treated) > 0:
        treated_bins = pd.cut(treated[running], bins=n_bins//2)
        treated_binned = treated.groupby(treated_bins, observed=True).agg({
            running: 'mean',
            outcome: 'mean'
        })
        ax.scatter(treated_binned[running], treated_binned[outcome],
                  s=100, alpha=0.6, color=colors[0], label='Treated (binned)', marker='s')

    # Fit polynomial lines for visualization
    if len(control) > 0:
        x_control = control[running].values
        y_control = control[outcome].values

        # Sort for smooth line
        sort_idx = np.argsort(x_control)
        x_control_sorted = x_control[sort_idx]

        # Fit polynomial
        poly_control = np.polyfit(x_control, y_control, model.polynomial)
        y_control_fit = np.polyval(poly_control, x_control_sorted)

        ax.plot(x_control_sorted, y_control_fit,
                color=colors[1], linewidth=2.5, alpha=0.8, linestyle='-')

    if len(treated) > 0:
        x_treated = treated[running].values
        y_treated = treated[outcome].values

        # Sort for smooth line
        sort_idx = np.argsort(x_treated)
        x_treated_sorted = x_treated[sort_idx]

        # Fit polynomial
        poly_treated = np.polyfit(x_treated, y_treated, model.polynomial)
        y_treated_fit = np.polyval(poly_treated, x_treated_sorted)

        ax.plot(x_treated_sorted, y_treated_fit,
                color=colors[0], linewidth=2.5, alpha=0.8, linestyle='-')

    # Add vertical line at cutoff
    ax.axvline(x=cutoff, color='gray', linestyle='--',
               linewidth=2, alpha=0.7, label='Cutoff')

    # Labels and formatting
    ax.set_xlabel(f'{running}', fontsize=12)
    ax.set_ylabel(f'{outcome}', fontsize=12)
    ax.set_title('Regression Discontinuity Design', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, frameon=True)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig


def plot_balance(
    pre_balance: Dict[str, Any],
    post_balance: Dict[str, Any],
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (10, 6)
) -> plt.Figure:
    """Plot covariate balance before and after matching.

    Shows standardized differences for each covariate before/after matching.
    Good balance is indicated by standardized differences close to zero.

    Args:
        pre_balance: Pre-matching balance dict from test_balance_pre_matching()
        post_balance: Post-matching balance dict from test_balance_post_matching()
        ax: Optional matplotlib axes to plot on
        figsize: Figure size in inches

    Returns:
        Matplotlib figure
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    # Extract standardized differences
    pre_std_diff = pre_balance['standardized_differences']
    post_std_diff = post_balance['standardized_differences']

    # Get covariate names
    covariates = list(pre_std_diff.keys())

    # Create positions for bars
    x = np.arange(len(covariates))
    width = 0.35

    # Get colorblind-friendly palette
    colors = sns.color_palette("colorblind")

    # Plot bars
    ax.barh(x - width/2, [abs(pre_std_diff[c]) for c in covariates],
            width, label='Before Matching', color=colors[1], alpha=0.7)
    ax.barh(x + width/2, [abs(post_std_diff[c]) for c in covariates],
            width, label='After Matching', color=colors[0], alpha=0.7)

    # Add reference lines for good balance thresholds
    ax.axvline(x=0.1, color='orange', linestyle='--', linewidth=1.5,
               alpha=0.7, label='|Std diff| = 0.1')
    ax.axvline(x=0.25, color='red', linestyle='--', linewidth=1.5,
               alpha=0.7, label='|Std diff| = 0.25')

    # Labels and formatting
    ax.set_yticks(x)
    ax.set_yticklabels(covariates)
    ax.set_xlabel('Absolute Standardized Difference', fontsize=12)
    ax.set_ylabel('Covariate', fontsize=12)
    ax.set_title('Covariate Balance: Before vs After Matching', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, frameon=True)
    ax.grid(True, alpha=0.3, axis='x')

    # Invert y-axis so first covariate is at top
    ax.invert_yaxis()

    fig.tight_layout()
    return fig


def plot_residuals(
    model: Any,
    ax: Optional[plt.Axes] = None,
    figsize: Tuple[float, float] = (12, 5)
) -> plt.Figure:
    """Plot OLS diagnostics: residuals vs fitted and Q-Q plot.

    Args:
        model: OLSRegression model instance (must be estimated)
        ax: Optional matplotlib axes array (must be length 2) to plot on
        figsize: Figure size in inches

    Returns:
        Matplotlib figure with two subplots
    """
    if ax is None:
        fig, axes = plt.subplots(1, 2, figsize=figsize)
    else:
        if not isinstance(ax, (list, np.ndarray)) or len(ax) != 2:
            raise ValueError("ax must be array of 2 axes for residual plots")
        axes = ax
        fig = axes[0].get_figure()

    # Check model is estimated
    if not model._estimated:
        raise ValueError("Model must be estimated before plotting. Call estimate() first.")

    # Get residuals and fitted values
    residuals = model.get_residuals()
    fitted = model.get_fitted_values()

    # Get colorblind-friendly palette
    colors = sns.color_palette("colorblind")

    # Plot 1: Residuals vs Fitted
    axes[0].scatter(fitted, residuals, alpha=0.6, s=50, color=colors[0])
    axes[0].axhline(y=0, color='gray', linestyle='--', linewidth=2, alpha=0.7)

    # Add lowess smoother to check for patterns
    from statsmodels.nonparametric.smoothers_lowess import lowess
    try:
        lowess_result = lowess(residuals, fitted, frac=0.3)
        axes[0].plot(lowess_result[:, 0], lowess_result[:, 1],
                    color=colors[1], linewidth=2.5, alpha=0.8, label='Lowess smooth')
        axes[0].legend(fontsize=10)
    except:
        pass  # Skip lowess if it fails

    axes[0].set_xlabel('Fitted Values', fontsize=11)
    axes[0].set_ylabel('Residuals', fontsize=11)
    axes[0].set_title('Residuals vs Fitted', fontsize=12, fontweight='bold')
    axes[0].grid(True, alpha=0.3)

    # Plot 2: Q-Q plot (normal probability plot)
    standardized_residuals = (residuals - residuals.mean()) / residuals.std()

    # Calculate theoretical quantiles
    n = len(standardized_residuals)
    theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, n))
    sample_quantiles = np.sort(standardized_residuals)

    # Plot Q-Q
    axes[1].scatter(theoretical_quantiles, sample_quantiles,
                   alpha=0.6, s=50, color=colors[0])

    # Add 45-degree reference line
    min_val = min(theoretical_quantiles.min(), sample_quantiles.min())
    max_val = max(theoretical_quantiles.max(), sample_quantiles.max())
    axes[1].plot([min_val, max_val], [min_val, max_val],
                color='gray', linestyle='--', linewidth=2, alpha=0.7, label='Normal')

    axes[1].set_xlabel('Theoretical Quantiles', fontsize=11)
    axes[1].set_ylabel('Sample Quantiles', fontsize=11)
    axes[1].set_title('Normal Q-Q Plot', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    return fig
