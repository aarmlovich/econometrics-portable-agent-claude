# Visualization Module

Publication-quality visualizations for econometric models using matplotlib and seaborn.

## Features

- **Colorblind-friendly palettes** - Uses seaborn's "colorblind" palette by default
- **Publication quality** - Default 300 DPI for raster outputs
- **Consistent styling** - Unified look across all plots
- **Easy integration** - Plot methods available directly on model classes

## Core Plotting Functions

### 1. Difference-in-Differences

#### `plot_parallel_trends(model, ax=None, figsize=(10, 6))`

Visualizes parallel trends assumption by showing mean outcomes over time for treated and control groups.

**Usage:**
```python
from src.models.causal.diff_in_diff import DifferenceInDifferences

did = DifferenceInDifferences(data, outcome='y', treatment='treat', time='period', unit='id')
did.estimate()

# Direct method call
fig = did.plot_parallel_trends()

# Or use standalone function
from src.visualization import plot_parallel_trends
fig = plot_parallel_trends(did)
```

#### `plot_event_study(coefficients, ci_lower, ci_upper, ax=None, figsize=(10, 6))`

Plots event study coefficients with confidence intervals showing dynamic treatment effects.

**Usage:**
```python
# Using model method (recommended)
fig = did.plot_event_study(leads=2, lags=3)

# Or manually with event study results
event_results = did.run_event_study(leads=2, lags=3)
from src.visualization import plot_event_study
fig = plot_event_study(
    event_results['coefficients'],
    event_results['ci_lower'],
    event_results['ci_upper']
)
```

### 2. Regression Discontinuity

#### `plot_rd(model, ax=None, figsize=(10, 6), n_bins=20)`

Shows RD design with binned scatter plot and fitted polynomial lines on each side of cutoff.

**Usage:**
```python
from src.models.causal.regression_discontinuity import RegressionDiscontinuity

rd = RegressionDiscontinuity(data, outcome='y', running='x', cutoff=0)
rd.estimate()

# Direct method call
fig = rd.plot(n_bins=30)

# Or use standalone function
from src.visualization import plot_rd
fig = plot_rd(rd, n_bins=30)
```

### 3. Propensity Score Matching

#### `plot_balance(pre_balance, post_balance, ax=None, figsize=(10, 6))`

Displays covariate balance before and after matching using standardized differences.

**Usage:**
```python
from src.models.causal.matching import Matching

matching = Matching(data, outcome='y', treatment='treat', covariates=['x1', 'x2'])
matching.estimate()

# Direct method call
fig = matching.plot_balance()

# Or use standalone function with custom balance stats
pre_balance = matching.test_balance_pre_matching()
post_balance = matching.test_balance_post_matching()
from src.visualization import plot_balance
fig = plot_balance(pre_balance, post_balance)
```

**Interpretation:**
- Standardized differences < 0.1 indicate good balance
- Standardized differences < 0.25 indicate acceptable balance
- Larger differences suggest poor balance and potential bias

### 4. OLS Regression

#### `plot_residuals(model, ax=None, figsize=(12, 5))`

Creates diagnostic plots for OLS regression:
1. **Residuals vs Fitted**: Check for heteroskedasticity and non-linear patterns
2. **Normal Q-Q Plot**: Check for normality of residuals

**Usage:**
```python
from src.models.regression.ols import OLSRegression

ols = OLSRegression(data, outcome='y', covariates=['x1', 'x2'])
ols.estimate()

# Direct method call
fig = ols.plot_residuals()

# Or use standalone function
from src.visualization import plot_residuals
fig = plot_residuals(ols)
```

**Interpretation:**
- **Residuals vs Fitted**: Random scatter around zero suggests homoskedasticity
- **Q-Q Plot**: Points close to diagonal line suggest normality

## Utility Functions

### `save_figure(fig, path, dpi=300, format='png')`

Save figures with publication quality settings.

**Usage:**
```python
from src.visualization import save_figure

# Create your plot
fig = model.plot()

# Save as PNG (default)
save_figure(fig, 'figures/my_plot', dpi=300, format='png')

# Save as PDF
save_figure(fig, 'figures/my_plot', dpi=300, format='pdf')

# Save as SVG (vector format)
save_figure(fig, 'figures/my_plot', dpi=300, format='svg')

# Or include extension in path
save_figure(fig, 'figures/my_plot.pdf', dpi=300)
```

**Parameters:**
- `fig`: Matplotlib figure object
- `path`: File path (with or without extension)
- `dpi`: Dots per inch for raster formats (default: 300)
- `format`: File format ('png', 'pdf', 'svg') - used if path has no extension (default: 'png')

## Customization

### Using Custom Axes

All plotting functions accept an optional `ax` parameter for custom layouts:

```python
import matplotlib.pyplot as plt

# Create custom subplot layout
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Use custom axes
did.plot_parallel_trends(ax=axes[0, 0])
did.plot_event_study(ax=axes[0, 1])
rd.plot(ax=axes[1, 0])
ols.plot_residuals(ax=[axes[1, 0], axes[1, 1]])  # Note: list of 2 axes for residuals

plt.tight_layout()
```

### Custom Figure Sizes

```python
# Larger figure for presentation
fig = did.plot_parallel_trends(figsize=(14, 8))

# Smaller figure for paper
fig = rd.plot(figsize=(6, 4))
```

### Styling

The module uses seaborn's "whitegrid" style and "colorblind" palette by default. You can override this:

```python
import seaborn as sns

# Change style before plotting
sns.set_style("darkgrid")
sns.set_palette("Set2")

fig = model.plot()
```

## Examples

### Complete DiD Workflow

```python
from src.models.causal.diff_in_diff import DifferenceInDifferences
from src.visualization import save_figure

# Estimate model
did = DifferenceInDifferences(
    data=df,
    outcome='earnings',
    treatment='policy',
    time='year',
    unit='state'
)
results = did.estimate()

# Create visualizations
fig1 = did.plot_parallel_trends()
save_figure(fig1, 'output/parallel_trends.png', dpi=300)
save_figure(fig1, 'output/parallel_trends.pdf', dpi=300)

fig2 = did.plot_event_study(leads=3, lags=5)
save_figure(fig2, 'output/event_study.png', dpi=300)
save_figure(fig2, 'output/event_study.pdf', dpi=300)
```

### Complete OLS Diagnostic Workflow

```python
from src.models.regression.ols import OLSRegression

# Estimate model
ols = OLSRegression(
    data=df,
    outcome='wage',
    covariates=['education', 'experience', 'age']
)
results = ols.estimate()

# Check diagnostics
fig = ols.plot_residuals()
save_figure(fig, 'output/ols_diagnostics')

# Print summary
print(ols.summary())
```

## Design Principles

1. **Simplicity**: Focus on essential information, avoid clutter
2. **Accessibility**: Colorblind-friendly by default
3. **Publication-ready**: High DPI, clean styling, proper labels
4. **Integration**: Seamless integration with model classes
5. **Flexibility**: Support for custom axes and layouts

## Dependencies

- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- statsmodels >= 0.14.0 (for lowess smoother in residual plots)
