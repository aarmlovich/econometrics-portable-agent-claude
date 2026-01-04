"""Propensity score matching for causal inference."""

from typing import Optional, List, Dict, Any, Literal
import numpy as np
import pandas as pd
from statsmodels.discrete.discrete_model import Logit
from statsmodels.tools.tools import add_constant
from sklearn.neighbors import NearestNeighbors
import warnings
import matplotlib.pyplot as plt

from src.models.base import BaseEconometricModel, EstimationResult, create_estimation_result


class Matching(BaseEconometricModel):
    """Propensity score matching estimator with balance diagnostics.
    
    Estimates average treatment effect (ATE) using propensity score matching.
    Includes pre/post-matching balance tests, common support trimming,
    and multiple matching algorithms.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        treatment: str,
        covariates: List[str],
        matching_method: Literal['nearest_neighbor', 'kernel', 'radius'] = 'nearest_neighbor',
        caliper: Optional[float] = None,
        trim_support: bool = True,
        trim_threshold_low: float = 0.1,
        trim_threshold_high: float = 0.9,
        replacement: bool = False,
        n_neighbors: int = 1
    ):
        """Initialize matching model.

        Args:
            data: DataFrame containing outcome, treatment, and covariates
            outcome: Name of outcome variable
            treatment: Name of treatment indicator (1 if treated, 0 if control)
            covariates: List of covariate variable names
            matching_method: Matching algorithm ('nearest_neighbor', 'kernel', 'radius')
            caliper: Maximum distance for matching (default: 0.2 × SD of logit pscore)
            trim_support: If True, trim observations outside common support
            trim_threshold_low: Lower bound for common support (default: 0.1)
            trim_threshold_high: Upper bound for common support (default: 0.9)
            replacement: If True, allow control units to be matched multiple times
            n_neighbors: Number of neighbors for nearest neighbor matching (default: 1)
        """
        super().__init__(data=data, outcome=outcome)
        self.treatment = treatment
        self.covariates = covariates
        self.matching_method = matching_method
        self.caliper = caliper
        self.trim_support = trim_support
        self.trim_threshold_low = trim_threshold_low
        self.trim_threshold_high = trim_threshold_high
        self.replacement = replacement
        self.n_neighbors = n_neighbors

        self.propensity_scores = None
        self.matched_data = None
        self.match_indices = None
        self.trimmed_indices = None

        # Validate required columns
        required_cols = [outcome, treatment] + covariates
        self._validate_columns(required_cols)

        # Validate treatment is binary
        treatment_values = data[treatment].unique()
        if not set(treatment_values).issubset({0, 1}):
            raise ValueError(f"Treatment variable must be binary (0/1), got {treatment_values}")
    
    def estimate_propensity_scores(self) -> pd.Series:
        """Estimate propensity scores using logistic regression.
        
        Returns:
            Series of propensity scores (indexed by original data index)
        """
        # Prepare data
        y_pscore = self.data[self.treatment].dropna()
        X_pscore = self.data[self.covariates].dropna()
        
        # Align indices
        common_idx = y_pscore.index.intersection(X_pscore.index)
        y_pscore = y_pscore.loc[common_idx]
        X_pscore = X_pscore.loc[common_idx]
        X_pscore = add_constant(X_pscore)
        
        # Estimate propensity score model (logit)
        model_pscore = Logit(y_pscore, X_pscore)
        results_pscore = model_pscore.fit(disp=0)
        
        # Get predicted probabilities (propensity scores)
        propensity_scores = results_pscore.predict(X_pscore)
        self.propensity_scores = pd.Series(propensity_scores, index=common_idx)
        
        return self.propensity_scores
    
    def test_balance_pre_matching(self) -> Dict[str, Any]:
        """Test covariate balance before matching.
        
        Returns:
            Dictionary containing:
                - standardized_differences: Standardized mean differences for each covariate
                - variance_ratios: Variance ratios (treated/control) for each covariate
                - balance_table: Summary table with means, std, and standardized differences
        """
        if self.propensity_scores is None:
            self.estimate_propensity_scores()
        
        # Use data before trimming (if trimming will be applied)
        data_used = self.data.loc[self.propensity_scores.index]
        
        treated = data_used[data_used[self.treatment] == 1]
        control = data_used[data_used[self.treatment] == 0]
        
        balance_table = {}
        standardized_differences = {}
        variance_ratios = {}
        
        for covar in self.covariates:
            treated_mean = treated[covar].mean()
            control_mean = control[covar].mean()
            treated_std = treated[covar].std()
            control_std = control[covar].std()
            pooled_std = np.sqrt((treated_std**2 + control_std**2) / 2)
            
            # Standardized difference: (mean_t - mean_c) / pooled_std
            std_diff = (treated_mean - control_mean) / pooled_std if pooled_std > 0 else 0.0
            
            # Variance ratio: var_t / var_c
            var_ratio = (treated_std / control_std)**2 if control_std > 0 else np.nan
            
            balance_table[covar] = {
                'treated_mean': float(treated_mean),
                'treated_std': float(treated_std),
                'control_mean': float(control_mean),
                'control_std': float(control_std),
                'std_diff': float(std_diff)
            }
            standardized_differences[covar] = float(std_diff)
            variance_ratios[covar] = float(var_ratio) if not np.isnan(var_ratio) else None
        
        return {
            'standardized_differences': standardized_differences,
            'variance_ratios': variance_ratios,
            'balance_table': balance_table
        }
    
    def test_balance_post_matching(self) -> Dict[str, Any]:
        """Test covariate balance after matching.
        
        Returns:
            Dictionary containing balance statistics for matched sample
        """
        if self.matched_data is None:
            raise ValueError("Must run matching first. Call estimate().")
        
        matched_treated = self.matched_data[self.matched_data[self.treatment] == 1]
        matched_control = self.matched_data[self.matched_data[self.treatment] == 0]
        
        balance_table = {}
        standardized_differences = {}
        variance_ratios = {}
        
        for covar in self.covariates:
            treated_mean = matched_treated[covar].mean()
            control_mean = matched_control[covar].mean()
            treated_std = matched_treated[covar].std()
            control_std = matched_control[covar].std()
            pooled_std = np.sqrt((treated_std**2 + control_std**2) / 2)
            
            std_diff = (treated_mean - control_mean) / pooled_std if pooled_std > 0 else 0.0
            var_ratio = (treated_std / control_std)**2 if control_std > 0 else np.nan
            
            balance_table[covar] = {
                'treated_mean': float(treated_mean),
                'treated_std': float(treated_std),
                'control_mean': float(control_mean),
                'control_std': float(control_std),
                'std_diff': float(std_diff)
            }
            standardized_differences[covar] = float(std_diff)
            variance_ratios[covar] = float(var_ratio) if not np.isnan(var_ratio) else None
        
        return {
            'standardized_differences': standardized_differences,
            'variance_ratios': variance_ratios,
            'balance_table': balance_table
        }
    
    def estimate(self) -> EstimationResult:
        """Estimate average treatment effect (ATE) using matching.

        Returns:
            EstimationResult with:
                - coefficients: {'ate': treatment effect}
                - std_errors: {'ate': standard error}
                - pvalues: {'ate': p-value}
                - ci_lower/ci_upper: Confidence intervals
                - nobs: Number of matched observations
                - fit_stats: n_treated, n_control, n_matched, n_trimmed
                - diagnostics: matching_method, caliper, trim_support
        """
        # Estimate propensity scores if not done
        if self.propensity_scores is None:
            self.estimate_propensity_scores()

        # Apply common support trimming if requested
        data_used = self.data.loc[self.propensity_scores.index].copy()
        data_used['propensity_score'] = self.propensity_scores

        if self.trim_support:
            trimmed_mask = (
                (data_used['propensity_score'] >= self.trim_threshold_low) &
                (data_used['propensity_score'] <= self.trim_threshold_high)
            )
            self.trimmed_indices = data_used[~trimmed_mask].index
            data_used = data_used[trimmed_mask].copy()
        else:
            self.trimmed_indices = pd.Index([])

        # Separate treated and control
        treated = data_used[data_used[self.treatment] == 1].copy()
        control = data_used[data_used[self.treatment] == 0].copy()

        if len(treated) == 0 or len(control) == 0:
            raise ValueError("No treated or control units after trimming")

        # Calculate caliper if not provided
        if self.caliper is None:
            logit_pscore = np.log(self.propensity_scores / (1 - self.propensity_scores + 1e-10))
            self.caliper = 0.2 * logit_pscore.std()

        # Perform matching
        if self.matching_method == 'nearest_neighbor':
            self._match_nearest_neighbor(treated, control)
        elif self.matching_method == 'kernel':
            self._match_kernel(treated, control)
        elif self.matching_method == 'radius':
            self._match_radius(treated, control)
        else:
            raise ValueError(f"Unknown matching method: {self.matching_method}")

        self._estimated = True

        # Calculate ATE
        treated_outcomes = self.matched_data[self.matched_data[self.treatment] == 1][self.outcome]
        control_outcomes = self.matched_data[self.matched_data[self.treatment] == 0][self.outcome]

        # Simple ATE: mean difference
        ate = float(treated_outcomes.mean() - control_outcomes.mean())

        # Simple standard error (conservative)
        n_treated_matched = len(treated_outcomes)
        n_control_matched = len(control_outcomes)
        var_treated = treated_outcomes.var()
        var_control = control_outcomes.var()
        std_error = float(np.sqrt(var_treated / n_treated_matched + var_control / n_control_matched))

        # Calculate p-value and CI
        from scipy import stats
        t_stat = ate / std_error if std_error > 0 else 0.0
        pvalue = float(2 * (1 - stats.norm.cdf(np.abs(t_stat))))
        ci_lower = ate - 1.96 * std_error
        ci_upper = ate + 1.96 * std_error

        result = create_estimation_result(
            coefficients={'ate': ate},
            std_errors={'ate': std_error},
            pvalues={'ate': pvalue},
            tvalues={'ate': t_stat},
            ci_lower={'ate': ci_lower},
            ci_upper={'ate': ci_upper},
            nobs=int(len(self.matched_data)),
            model_type='matching',
            fit_stats={
                'n_treated': int(len(treated)),
                'n_control': int(len(control)),
                'n_matched': int(len(self.matched_data)),
                'n_trimmed': int(len(self.trimmed_indices)),
            },
            diagnostics={
                'matching_method': self.matching_method,
                'caliper': float(self.caliper),
                'trim_support': self.trim_support,
            }
        )

        # Store for summary() access
        self.results = {
            'ate': ate,
            'std_error': std_error,
            'n_treated': int(len(treated)),
            'n_control': int(len(control)),
            'n_matched': int(len(self.matched_data)),
            'n_trimmed': int(len(self.trimmed_indices)),
        }

        return result
    
    def _match_nearest_neighbor(self, treated: pd.DataFrame, control: pd.DataFrame):
        """Perform nearest neighbor matching."""
        # Use logit of propensity score for matching
        treated_pscore = np.log(treated['propensity_score'] / (1 - treated['propensity_score'] + 1e-10))

        # Track which control units have been used (for matching without replacement)
        used_control_indices = set()

        matched_treated = []
        matched_control = []
        match_pairs = []

        # Process each treated unit
        for i in range(len(treated)):
            # Get available control units
            if self.replacement:
                available_control = control
            else:
                available_mask = ~control.index.isin(used_control_indices)
                available_control = control[available_mask]

            if len(available_control) == 0:
                break

            # Calculate control propensity scores for available units
            control_pscore = np.log(
                available_control['propensity_score'] /
                (1 - available_control['propensity_score'] + 1e-10)
            )

            # Fit NN on available controls
            control_pscore_2d = control_pscore.values.reshape(-1, 1)
            nn = NearestNeighbors(n_neighbors=min(self.n_neighbors, len(available_control)), metric='manhattan')
            nn.fit(control_pscore_2d)

            # Find nearest neighbor for this treated unit
            treated_ps = treated_pscore.iloc[i]
            dist, idx = nn.kneighbors([[treated_ps]])

            # Apply caliper check
            if dist[0][0] <= self.caliper:
                treated_idx = treated.iloc[i].name
                # idx is relative to available_control, so use iloc
                control_row = available_control.iloc[idx[0][0]]
                control_idx = control_row.name

                matched_treated.append(treated.iloc[i])
                matched_control.append(control_row)
                match_pairs.append((treated_idx, control_idx))

                # Mark control as used (for matching without replacement)
                if not self.replacement:
                    used_control_indices.add(control_idx)

        # Combine matched data
        if matched_treated:
            matched_treated_df = pd.DataFrame(matched_treated)
            matched_control_df = pd.DataFrame(matched_control)
            self.matched_data = pd.concat([matched_treated_df, matched_control_df], ignore_index=False)
        else:
            # No matches found - create empty DataFrame with correct columns
            self.matched_data = pd.DataFrame(columns=treated.columns)
        self.match_indices = match_pairs
    
    def _match_kernel(self, treated: pd.DataFrame, control: pd.DataFrame):
        """Perform kernel matching (simplified version - uses nearest neighbor as approximation)."""
        # For simplicity, use nearest neighbor with larger n_neighbors
        # Full kernel matching would weight by distance
        warnings.warn(
            "Kernel matching not fully implemented, using nearest neighbor approximation",
            UserWarning
        )
        self._match_nearest_neighbor(treated, control)
    
    def _match_radius(self, treated: pd.DataFrame, control: pd.DataFrame):
        """Perform radius matching."""
        # Use radius = caliper
        treated_pscore = np.log(treated['propensity_score'] / (1 - treated['propensity_score'] + 1e-10))
        control_pscore = np.log(control['propensity_score'] / (1 - control['propensity_score'] + 1e-10))
        
        matched_treated = []
        matched_control = []
        match_pairs = []
        
        for i, treated_ps in enumerate(treated_pscore):
            # Find all control units within caliper
            within_caliper = np.abs(control_pscore - treated_ps) <= self.caliper
            
            if within_caliper.sum() > 0:
                treated_idx = treated.iloc[i].name
                # Use first match (could weight by distance for better implementation)
                control_match_idx = control_pscore[within_caliper].index[0]
                matched_treated.append(treated.iloc[i])
                matched_control.append(control.loc[control_match_idx])
                match_pairs.append((treated_idx, control_match_idx))
        
        # Combine matched data
        matched_treated_df = pd.DataFrame(matched_treated)
        matched_control_df = pd.DataFrame(matched_control)
        self.matched_data = pd.concat([matched_treated_df, matched_control_df], ignore_index=False)
        self.match_indices = match_pairs
    
    def summary(self) -> str:
        """Generate summary of matching results.

        Returns:
            Formatted summary string
        """
        self._check_estimated()

        summary_lines = []
        summary_lines.append("=" * 80)
        summary_lines.append("Propensity Score Matching Results")
        summary_lines.append("=" * 80)
        summary_lines.append("")

        summary_lines.append(f"Matching Method: {self.matching_method}")
        summary_lines.append(f"Caliper: {self.caliper:.4f}")
        summary_lines.append(f"Common Support Trimming: {self.trim_support}")
        if self.trim_support:
            summary_lines.append(f"  Trim thresholds: [{self.trim_threshold_low}, {self.trim_threshold_high}]")
        summary_lines.append("")

        summary_lines.append("Treatment Effect Estimate:")
        summary_lines.append(f"  ATE: {self.results['ate']:.4f}")
        summary_lines.append(f"  Std. Error: {self.results['std_error']:.4f}")
        summary_lines.append("")

        summary_lines.append("Sample Sizes:")
        summary_lines.append(f"  Treated: {self.results['n_treated']}")
        summary_lines.append(f"  Control: {self.results['n_control']}")
        summary_lines.append(f"  Matched: {self.results['n_matched']}")
        if self.trim_support:
            summary_lines.append(f"  Trimmed: {self.results['n_trimmed']}")

        return "\n".join(summary_lines)

    def plot_balance(
        self,
        ax: Optional[plt.Axes] = None,
        figsize: tuple = (10, 6)
    ) -> plt.Figure:
        """Plot covariate balance before and after matching.

        Shows standardized differences for each covariate to assess
        whether matching successfully balanced the covariates.

        Args:
            ax: Optional matplotlib axes to plot on
            figsize: Figure size in inches

        Returns:
            Matplotlib figure
        """
        # Get balance statistics
        pre_balance = self.test_balance_pre_matching()
        post_balance = self.test_balance_post_matching()

        # Plot
        from src.visualization.plots import plot_balance
        return plot_balance(pre_balance, post_balance, ax=ax, figsize=figsize)

