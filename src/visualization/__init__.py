"""Visualization module for econometric models.

Publication-quality plots using matplotlib and seaborn with colorblind-friendly palettes.
"""

from src.visualization.plots import (
    plot_parallel_trends,
    plot_event_study,
    plot_rd,
    plot_balance,
    plot_residuals,
    save_figure,
)

__all__ = [
    'plot_parallel_trends',
    'plot_event_study',
    'plot_rd',
    'plot_balance',
    'plot_residuals',
    'save_figure',
]
