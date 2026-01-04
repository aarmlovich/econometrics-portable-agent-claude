"""Regression discontinuity design estimation."""

from typing import Optional, List, Dict, Any, Literal
import numpy as np
import pandas as pd
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
from scipy import stats
from scipy.stats import gaussian_kde
import warnings


class RegressionDiscontinuity:
    """Regression discontinuity design estimator with bandwidth selection.
    
    Estimates treatment effects using regression discontinuity design
    with local polynomial estimation, optimal bandwidth selection,
    and manipulation testing.
    
    Specification: Y_i = α + βTreat_i + f(Running_i) + ε_i
    Where Treat_i = 1 if Running_i >= cutoff, and f(·) is polynomial.
    """
    
    def __init__(
        self,
        data: pd.DataFrame,
        outcome: str,
        running: str,
        cutoff: float,
        bandwidth: Optional[float] = None,
        polynomial: int = 1,
        kernel: str = 'triangular',
        covariates: Optional[List[str]] = None
    ):
        """Initialize regression discontinuity model.
        
        Args:
            data: DataFrame containing outcome, running variable, and covariates
            outcome: Name of outcome variable
            running: Name of running variable (assignment variable)
            cutoff: Cutoff value for treatment assignment
            bandwidth: Bandwidth for local polynomial (if None, will be selected)
            polynomial: Polynomial order (1=linear, 2=quadratic)
            kernel: Kernel function ('triangular', 'uniform', 'epanechnikov')
            covariates: Optional list of covariate variable names
        """
        self.data = data.copy()  # Preserve original data
        self.outcome = outcome
        self.running = running
        self.cutoff = cutoff
        self.bandwidth = bandwidth
        self.polynomial = polynomial
        self.kernel = kernel
        self.covariates = covariates if covariates else []
        self.optimal_bandwidth = None
        self.results = None
        self.robustness_results = None
        
        # Validate required columns
        required_cols = [outcome, running] + self.covariates
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        
        # Create treatment indicator
        self.data['treated'] = (self.data[running] >= cutoff).astype(int)
        self.data['running_centered'] = self.data[running] - cutoff
        
        # Validate kernel
        valid_kernels = ['triangular', 'uniform', 'epanechnikov']
        if kernel not in valid_kernels:
            raise ValueError(f"Kernel must be one of {valid_kernels}, got {kernel}")
    
    def _kernel_weight(self, x: np.ndarray, bandwidth: float) -> np.ndarray:
        """Calculate kernel weights.
        
        Args:
            x: Distances from cutoff (centered running variable)
            bandwidth: Bandwidth parameter
            
        Returns:
            Array of kernel weights
        """
        u = np.abs(x / bandwidth)
        
        if self.kernel == 'triangular':
            weights = (1 - u) * (u <= 1).astype(float)
        elif self.kernel == 'uniform':
            weights = (u <= 1).astype(float)
        elif self.kernel == 'epanechnikov':
            weights = (1 - u**2) * (u <= 1).astype(float) * 0.75
        else:
            weights = (1 - u) * (u <= 1).astype(float)  # Default to triangular
        
        return weights
    
    def select_optimal_bandwidth(self, bandwidth_range: Optional[List[float]] = None) -> float:
        """Select optimal bandwidth using cross-validation (MSE minimization).
        
        Args:
            bandwidth_range: Optional list of bandwidth values to test.
                           If None, uses default range.
        
        Returns:
            Optimal bandwidth value
        """
        # Prepare data
        data_clean = self.data[[self.outcome, self.running, 'running_centered', 'treated'] + self.covariates].dropna()
        
        # Default bandwidth range if not provided
        if bandwidth_range is None:
            running_range = data_clean[self.running].max() - data_clean[self.running].min()
            bandwidth_range = np.linspace(running_range * 0.1, running_range * 0.5, 20)
        
        best_bandwidth = None
        best_mse = np.inf
        
        # Cross-validation: leave-one-out
        for bw in bandwidth_range:
            mse_list = []
            
            # Use smaller sample for speed (could use full sample)
            sample_size = min(200, len(data_clean))
            sample_indices = np.random.choice(len(data_clean), sample_size, replace=False)
            sample_data = data_clean.iloc[sample_indices]
            
            for idx in range(len(sample_data)):
                # Leave-one-out
                train_data = sample_data.drop(sample_data.index[idx])
                test_obs = sample_data.iloc[idx]
                
                # Estimate local polynomial on training data
                x_train = train_data['running_centered'].values
                weights_train = self._kernel_weight(x_train, bw)
                
                # Only use observations with positive weights
                mask = weights_train > 0
                if mask.sum() < 10:  # Need sufficient observations
                    continue
                
                x_train_masked = x_train[mask]
                y_train = train_data[self.outcome].values[mask]
                weights_train_masked = weights_train[mask]
                
                # Create polynomial terms
                X_train = np.column_stack([np.ones(len(x_train_masked)), x_train_masked])
                for p in range(2, self.polynomial + 1):
                    X_train = np.column_stack([X_train, x_train_masked**p])
                
                # Separate treated and control
                treated_mask = train_data['treated'].values[mask]
                X_train_treated = X_train[treated_mask == 1]
                X_train_control = X_train[treated_mask == 0]
                y_train_treated = y_train[treated_mask == 1]
                y_train_control = y_train[treated_mask == 0]
                w_treated = weights_train_masked[treated_mask == 1]
                w_control = weights_train_masked[treated_mask == 0]
                
                if len(X_train_treated) < 5 or len(X_train_control) < 5:
                    continue
                
                # Weighted regression on each side
                try:
                    # Control side
                    W_control = np.diag(np.sqrt(w_control))
                    X_control_weighted = W_control @ X_train_control
                    y_control_weighted = W_control @ y_train_control
                    beta_control = np.linalg.lstsq(X_control_weighted, y_control_weighted, rcond=None)[0]
                    
                    # Treated side
                    W_treated = np.diag(np.sqrt(w_treated))
                    X_treated_weighted = W_treated @ X_train_treated
                    y_treated_weighted = W_treated @ y_train_treated
                    beta_treated = np.linalg.lstsq(X_treated_weighted, y_treated_weighted, rcond=None)[0]
                    
                    # Predict test observation
                    x_test = test_obs['running_centered']
                    X_test = np.array([1, x_test])
                    for p in range(2, self.polynomial + 1):
                        X_test = np.append(X_test, x_test**p)
                    
                    if test_obs['treated'] == 1:
                        y_pred = X_test @ beta_treated
                    else:
                        y_pred = X_test @ beta_control
                    
                    mse = (test_obs[self.outcome] - y_pred)**2
                    mse_list.append(mse)
                    
                except (np.linalg.LinAlgError, ValueError):
                    continue
            
            if len(mse_list) > 0:
                avg_mse = np.mean(mse_list)
                if avg_mse < best_mse:
                    best_mse = avg_mse
                    best_bandwidth = bw
        
        if best_bandwidth is None:
            # Fallback: use rule of thumb
            running_range = data_clean[self.running].max() - data_clean[self.running].min()
            best_bandwidth = running_range * 0.25
        
        self.optimal_bandwidth = best_bandwidth
        self.bandwidth = best_bandwidth
        return best_bandwidth
    
    def estimate(self) -> Dict[str, float]:
        """Estimate regression discontinuity treatment effect.
        
        Returns:
            Dictionary containing RD estimates and statistics
        """
        # Select bandwidth if not provided
        if self.bandwidth is None:
            self.select_optimal_bandwidth()
        
        # Prepare data
        data_clean = self.data[[self.outcome, 'running_centered', 'treated'] + self.covariates].dropna()
        
        # Apply bandwidth (kernel weights)
        x_centered = data_clean['running_centered'].values
        weights = self._kernel_weight(x_centered, self.bandwidth)
        
        # Only use observations within bandwidth
        mask = weights > 0
        data_used = data_clean[mask].copy()
        weights_used = weights[mask]
        x_used = data_used['running_centered'].values
        
        if len(data_used) < 20:
            raise ValueError(f"Insufficient observations within bandwidth: {len(data_used)}")
        
        # Create polynomial terms
        X_poly = np.column_stack([np.ones(len(x_used)), x_used])
        for p in range(2, self.polynomial + 1):
            X_poly = np.column_stack([X_poly, x_used**p])
        
        # Add treatment indicator and interactions
        treated = data_used['treated'].values
        X = np.column_stack([X_poly, treated, treated * x_used])
        for p in range(2, self.polynomial + 1):
            X = np.column_stack([X, treated * (x_used**p)])
        
        # Add covariates if present
        if self.covariates:
            X = np.column_stack([X, data_used[self.covariates].values])
        
        y = data_used[self.outcome].values
        
        # Weighted least squares
        W = np.diag(np.sqrt(weights_used))
        X_weighted = W @ X
        y_weighted = W @ y
        
        # Estimate
        try:
            beta = np.linalg.lstsq(X_weighted, y_weighted, rcond=None)[0]
            residuals = y_weighted - X_weighted @ beta
            
            # Standard errors (robust, using residuals)
            n = len(y)
            k = X.shape[1]
            sigma_sq = np.sum(residuals**2) / (n - k)
            var_beta = sigma_sq * np.linalg.inv(X_weighted.T @ X_weighted)
            se_beta = np.sqrt(np.diag(var_beta))
            
            # Treatment effect is coefficient on 'treated'
            rd_coef = beta[self.polynomial + 1]  # After polynomial terms
            rd_se = se_beta[self.polynomial + 1]
            rd_tstat = rd_coef / rd_se if rd_se > 0 else np.nan
            rd_pval = 2 * (1 - stats.norm.cdf(np.abs(rd_tstat))) if not np.isnan(rd_tstat) else np.nan
            
            # Confidence interval
            ci_lower = rd_coef - 1.96 * rd_se
            ci_upper = rd_coef + 1.96 * rd_se
            
        except (np.linalg.LinAlgError, ValueError) as e:
            raise ValueError(f"Estimation failed: {e}")
        
        self.results = {
            'coefficient': float(rd_coef),
            'std_error': float(rd_se),
            'pvalue': float(rd_pval),
            'ci_lower': float(ci_lower),
            'ci_upper': float(ci_upper),
            'bandwidth': float(self.bandwidth),
            'nobs': int(n),
            'polynomial': self.polynomial
        }
        
        return self.results
    
    def test_manipulation(self) -> Dict[str, float]:
        """Test for manipulation at cutoff (McCrary density test).
        
        Tests for discontinuity in density of running variable at cutoff.
        Suggests manipulation if significant discontinuity detected.
        
        Returns:
            Dictionary containing manipulation test results
        """
        # Prepare data
        data_clean = self.data[[self.running]].dropna()
        running_values = data_clean[self.running].values
        
        # Use bandwidth if available, otherwise use rule of thumb
        if self.bandwidth is None:
            running_range = running_values.max() - running_values.min()
            bandwidth_test = running_range * 0.25
        else:
            bandwidth_test = self.bandwidth
        
        # Estimate density on each side of cutoff
        running_left = running_values[running_values < self.cutoff]
        running_right = running_values[running_values >= self.cutoff]
        
        if len(running_left) < 10 or len(running_right) < 10:
            warnings.warn("Insufficient observations for manipulation test", UserWarning)
            return {
                'test_statistic': np.nan,
                'pvalue': np.nan,
                'interpretation': 'Insufficient data for test'
            }
        
        # Estimate density using kernel density estimation
        try:
            kde_left = gaussian_kde(running_left)
            kde_right = gaussian_kde(running_right)
            
            # Evaluate densities at cutoff (from left and right)
            density_left = kde_left(self.cutoff)[0]
            density_right = kde_right(self.cutoff)[0]
            
            # Log difference (McCrary test statistic)
            log_diff = np.log(density_right + 1e-10) - np.log(density_left + 1e-10)
            
            # Standard error (simplified approximation)
            se_log_diff = np.sqrt(1 / len(running_left) + 1 / len(running_right))
            t_stat = log_diff / se_log_diff if se_log_diff > 0 else np.nan
            pvalue = 2 * (1 - stats.norm.cdf(np.abs(t_stat))) if not np.isnan(t_stat) else np.nan
            
            interpretation = (
                "No significant manipulation detected (p >= 0.05)" if pvalue >= 0.05
                else "Potential manipulation detected (p < 0.05)"
            )
            
        except Exception as e:
            warnings.warn(f"Manipulation test failed: {e}", UserWarning)
            return {
                'test_statistic': np.nan,
                'pvalue': np.nan,
                'interpretation': f'Test failed: {e}'
            }
        
        return {
            'test_statistic': float(t_stat),
            'pvalue': float(pvalue),
            'log_density_diff': float(log_diff),
            'density_left': float(density_left),
            'density_right': float(density_right),
            'interpretation': interpretation
        }
    
    def estimate_robustness_bandwidths(self) -> Dict[str, Dict]:
        """Estimate RD for multiple bandwidths (robustness check).
        
        Estimates treatment effect for 0.5x, 1.0x, and 1.5x optimal bandwidth.
        
        Returns:
            Dictionary containing estimates for each bandwidth
        """
        if self.bandwidth is None:
            self.select_optimal_bandwidth()
        
        base_bandwidth = self.bandwidth
        robustness_results = {}
        
        for mult in [0.5, 1.0, 1.5]:
            bw = base_bandwidth * mult
            self.bandwidth = bw
            
            try:
                results = self.estimate()
                robustness_results[f'{mult}x'] = results
            except (ValueError, np.linalg.LinAlgError) as e:
                robustness_results[f'{mult}x'] = {'error': str(e)}
        
        # Restore original bandwidth
        self.bandwidth = base_bandwidth
        self.robustness_results = robustness_results
        
        return robustness_results
    
    def summary(self) -> str:
        """Generate summary of RD estimation results.
        
        Returns:
            Formatted summary string
        """
        if self.results is None:
            raise ValueError("Model not estimated. Call estimate() first.")
        
        summary_lines = []
        summary_lines.append("=" * 80)
        summary_lines.append("Regression Discontinuity Design Estimation Results")
        summary_lines.append("=" * 80)
        summary_lines.append("")
        
        summary_lines.append(f"Cutoff: {self.cutoff}")
        summary_lines.append(f"Bandwidth: {self.results['bandwidth']:.4f}")
        summary_lines.append(f"Polynomial order: {self.results['polynomial']}")
        summary_lines.append(f"Kernel: {self.kernel}")
        summary_lines.append("")
        
        summary_lines.append("Treatment Effect Estimate:")
        summary_lines.append(f"  Coefficient: {self.results['coefficient']:.4f}")
        summary_lines.append(f"  Std. Error: {self.results['std_error']:.4f}")
        summary_lines.append(f"  P-value: {self.results['pvalue']:.4f}")
        summary_lines.append(f"  95% CI: [{self.results['ci_lower']:.4f}, {self.results['ci_upper']:.4f}]")
        summary_lines.append(f"  Observations: {self.results['nobs']}")
        
        return "\n".join(summary_lines)

