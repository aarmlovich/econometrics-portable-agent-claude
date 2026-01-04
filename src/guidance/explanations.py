"""Explanation system with basic and educational modes.

Includes authoritative citations from:
Wooldridge, J.M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
MIT Press.
"""

from typing import Dict, Any, Optional, Literal
import warnings


# Global explanation mode
_GLOBAL_EXPLANATION_MODE: Literal['basic', 'educational'] = 'basic'


# Wooldridge page citations for explanations
WOOLDRIDGE_CITATIONS: Dict[str, str] = {
    # Method Selection
    'method_selection_did': 'Wooldridge, Ch. 21, Section 21.4, p.713-720',
    'method_selection_iv': 'Wooldridge, Ch. 5, p.83-113',
    'method_selection_rd': 'Wooldridge, Ch. 21, Section 21.5, p.720-725',
    'method_selection_matching': 'Wooldridge, Ch. 21, Section 21.3, p.704-710',
    'method_selection_fe': 'Wooldridge, Ch. 10, Section 10.5, p.263-297',

    # Standard Errors
    'standard_error_robust': 'Wooldridge, Ch. 4, Section 4.2.3, p.55-58',
    'standard_error_clustered': 'Wooldridge, Ch. 10, Section 10.5.4, p.274-276',

    # Diagnostics
    'diagnostic_first_stage_f': 'Wooldridge, Ch. 5, p.101-103 (Staiger-Stock rule)',
    'diagnostic_overidentification': 'Wooldridge, Ch. 6, Section 6.2.2, p.122-124',
    'diagnostic_hausman': 'Wooldridge, Ch. 10, Section 10.7.3, p.291-300',
    'diagnostic_parallel_trends': 'Wooldridge, Ch. 21, Section 21.4, p.713-720',

    # Statistical Assumptions
    'statistical_assumptions_ols': 'Wooldridge, Ch. 4, p.49-80',

    # Economic Intuition
    'economic_intuition_coefficient': 'Wooldridge, Ch. 4, Section 4.1, p.49-55',

    # Causal Identification
    'causal_identification_did': 'Wooldridge, Ch. 21, Section 21.4, p.713-720',
}


def toggle_explanation_mode(
    global_mode: Optional[Literal['basic', 'educational']] = None
) -> str:
    """Toggle global explanation mode or set to specific mode.
    
    Args:
        global_mode: 'basic' or 'educational'. If None, toggles between modes.
        
    Returns:
        Current explanation mode after toggle
    """
    global _GLOBAL_EXPLANATION_MODE
    
    if global_mode is None:
        # Toggle
        _GLOBAL_EXPLANATION_MODE = 'educational' if _GLOBAL_EXPLANATION_MODE == 'basic' else 'basic'
    else:
        _GLOBAL_EXPLANATION_MODE = global_mode
    
    return _GLOBAL_EXPLANATION_MODE


def get_explanation(
    topic: str,
    context: Optional[Dict[str, Any]] = None,
    mode: Optional[Literal['basic', 'educational']] = None,
    include_citation: bool = False
) -> str:
    """Get explanation for a topic in basic or educational mode.

    Args:
        topic: Topic identifier (e.g., 'method_selection_did', 'economic_intuition_coefficient')
        context: Optional context dictionary for context-aware explanations
        mode: 'basic' or 'educational'. If None, uses global mode.
        include_citation: If True, append Wooldridge citation when available.

    Returns:
        Explanation text (with optional citation)
    """
    if mode is None:
        mode = _GLOBAL_EXPLANATION_MODE

    if context is None:
        context = {}

    # Get explanation from database
    explanation = _EXPLANATION_DB.get(topic, {})

    if not explanation:
        return f"Explanation not available for topic: {topic}"

    # Get explanation text for requested mode
    if mode == 'educational' and 'educational' in explanation:
        text = explanation['educational']
    elif 'basic' in explanation:
        text = explanation['basic']
    else:
        # Fallback to whatever is available
        text = list(explanation.values())[0]

    # Apply context substitutions if needed
    if context:
        try:
            text = text.format(**context)
        except KeyError:
            # Missing context variables - return as-is
            pass

    # Append Wooldridge citation if requested
    if include_citation and topic in WOOLDRIDGE_CITATIONS:
        text = f"{text}\n\n[Reference: {WOOLDRIDGE_CITATIONS[topic]}]"

    return text


def get_wooldridge_citation(topic: str) -> Optional[str]:
    """Get Wooldridge citation for a topic.

    Args:
        topic: Topic identifier

    Returns:
        Citation string or None if not available
    """
    return WOOLDRIDGE_CITATIONS.get(topic)


# Explanation database
_EXPLANATION_DB: Dict[str, Dict[str, str]] = {
    # Method Selection Explanations
    'method_selection_did': {
        'basic': 'Difference-in-differences (DiD) compares changes over time between treated and control groups, using the assumption that trends would be parallel in the absence of treatment.',
        'educational': (
            'Difference-in-differences (DiD) is a causal inference method that exploits variation in treatment '
            'timing across groups. The key identifying assumption is the "parallel trends" assumption: in the '
            'absence of treatment, the treated and control groups would have followed parallel trends. DiD '
            'estimates the treatment effect as the difference between (1) the change in the treated group and '
            '(2) the change in the control group. This "difference of differences" removes time-invariant '
            'confounders and common time trends. DiD is ideal when you have panel data with a clear treatment '
            'event, variation in treatment timing, and can verify parallel pre-treatment trends.'
        )
    },
    
    'method_selection_iv': {
        'basic': 'Instrumental Variables (IV) uses an instrument that affects the treatment but not the outcome directly, allowing causal inference when treatment is endogenous.',
        'educational': (
            'Instrumental Variables (IV) estimation addresses endogeneity by using an "instrument" - a variable '
            'that is correlated with the endogenous treatment but affects the outcome only through the treatment '
            '(exclusion restriction). The IV estimator is the ratio of (1) the reduced-form effect (instrument '
            'on outcome) to (2) the first-stage effect (instrument on treatment). This "two-stage" approach '
            'isolates the exogenous variation in treatment. IV requires a valid instrument (relevant and exogenous), '
            'and the estimate has a "local" interpretation (Local Average Treatment Effect, LATE) for compliers. '
            'Weak instruments (first-stage F < 10) are problematic and can lead to biased estimates.'
        )
    },
    
    'method_selection_rd': {
        'basic': 'Regression Discontinuity (RD) exploits a cutoff in a running variable to identify causal effects, comparing observations just above and below the cutoff.',
        'educational': (
            'Regression Discontinuity (RD) design identifies causal effects by exploiting a discontinuity at a '
            'known cutoff in a "running variable." The key assumption is that units just above and below the '
            'cutoff are similar except for treatment status (continuity assumption). Sharp RD uses a deterministic '
            'cutoff (treatment = 1 if running ≥ cutoff), while fuzzy RD allows some non-compliance. The RD estimate '
            'is the difference in outcome at the cutoff. Bandwidth selection is critical - too wide includes '
            'observations far from cutoff (bias), too narrow loses precision. Optimal bandwidth balances bias and '
            'variance. Manipulation testing (McCrary test) checks whether units can precisely control the running '
            'variable, which would violate the design.'
        )
    },
    
    'method_selection_matching': {
        'basic': 'Matching methods balance observables between treated and control groups using propensity scores, estimating treatment effects on comparable units.',
        'educational': (
            'Propensity score matching addresses selection bias by matching treated and control units with similar '
            'propensity scores (probability of treatment given observables). The key assumption is "unconfoundedness" '
            'or "selection on observables" - all confounders are observed. Matching constructs a balanced sample by '
            'pairing or weighting observations. Common support trimming (typically 0.1-0.9) removes observations '
            'with extreme propensity scores where overlap is poor. Balance tests verify that matched groups have '
            'similar covariate distributions. Matching provides the Average Treatment Effect on the Treated (ATT) '
            'and requires strong overlap in propensity score distributions between groups.'
        )
    },
    
    'method_selection_fe': {
        'basic': 'Fixed effects models control for unobserved time-invariant heterogeneity by including entity-specific intercepts.',
        'educational': (
            'Fixed effects (FE) estimation removes unobserved time-invariant confounders by including entity-specific '
            'intercepts (or by "within transformation" - demeaning within entities). FE exploits only within-entity '
            'variation over time, so time-invariant variables are not identified. Two-way FE includes both entity and '
            'time fixed effects, controlling for entity-invariant time trends. FE is preferred over random effects (RE) '
            'when unobserved heterogeneity is correlated with regressors (Hausman test). Standard errors should be '
            'clustered at the entity level to account for serial correlation. FE is ideal for panel data with many '
            'entities and few time periods.'
        )
    },
    
    # Economic Intuition Explanations
    'economic_intuition_coefficient': {
        'basic': 'The coefficient represents the change in the outcome associated with a one-unit change in the variable, holding other factors constant.',
        'educational': (
            'In regression analysis, coefficients have a "ceteris paribus" (holding other things constant) interpretation. '
            'For a continuous variable X, the coefficient β represents the expected change in the outcome Y when X increases '
            'by one unit, conditional on the values of all other variables in the model. For a binary variable (dummy), '
            'the coefficient represents the difference in mean outcomes between the two groups. Economic interpretation '
            'requires considering: (1) the units of measurement, (2) whether the relationship is causal or correlational, '
            'and (3) the economic mechanism. For example, a coefficient of 0.05 on years of education in a log-wage regression '
            'means that one additional year of education is associated with a 5% increase in wages, holding other factors constant.'
        )
    },
    
    # Causal Identification Explanations
    'causal_identification_did': {
        'basic': 'DiD identifies causal effects by assuming parallel trends - treated and control groups would have followed similar trends without treatment.',
        'educational': (
            'Difference-in-differences identification relies on the parallel trends assumption: in the absence of treatment, '
            'the average change in the outcome for the treated group would equal the average change for the control group. '
            'This assumption allows us to use the control group\'s change as a counterfactual for what would have happened '
            'to the treated group. The DiD estimator removes: (1) time-invariant differences between groups (via differencing), '
            'and (2) common time trends (via comparison to control). Violations occur if groups have differential trends '
            'independent of treatment (pre-treatment trends test), or if there are spillovers or anticipation effects. '
            'Event studies can test for pre-treatment effects and dynamic treatment effects.'
        )
    },
    
    # Statistical Assumptions Explanations
    'statistical_assumptions_ols': {
        'basic': 'OLS requires linearity, exogeneity (no omitted variables), homoskedasticity (constant variance), and no perfect multicollinearity.',
        'educational': (
            'Ordinary Least Squares (OLS) requires several assumptions for unbiased and efficient estimation: '
            '(1) Linearity: the relationship is linear in parameters, (2) Exogeneity: E[ε|X] = 0 (errors uncorrelated '
            'with regressors - no omitted variable bias), (3) Homoskedasticity: Var(ε|X) = σ² (constant error variance), '
            '(4) No perfect multicollinearity: regressors are not perfectly correlated, (5) No autocorrelation (for '
            'cross-sectional data). Violations: endogeneity (bias), heteroskedasticity (inefficient but correctable with '
            'robust SE), multicollinearity (high variance). Robust standard errors (HC1, HC2, HC3) relax the homoskedasticity '
            'assumption and provide valid inference even with heteroskedastic errors.'
        )
    },
    
    # Standard Error Explanations
    'standard_error_robust': {
        'basic': 'Robust standard errors (HC1) allow for heteroskedasticity (non-constant error variance) and provide valid inference without assuming homoskedasticity.',
        'educational': (
            'Robust standard errors (heteroskedasticity-consistent, HC) relax the homoskedasticity assumption of classical '
            'OLS. HC1 (Stata default) scales the standard OLS variance estimator by n/(n-k) and uses squared residuals. '
            'HC2 adjusts for leverage (hat values), and HC3 (jackknife) is preferred for small samples. Robust SE are '
            'consistent even when errors are heteroskedastic, providing valid inference. However, they do not address '
            'endogeneity - if the exogeneity assumption fails, coefficients are still biased. For panel data, clustered '
            'standard errors account for both heteroskedasticity and within-cluster correlation (e.g., serial correlation '
            'within entities).'
        )
    },
    
    'standard_error_clustered': {
        'basic': 'Clustered standard errors account for correlation within groups (e.g., multiple observations per entity in panel data) and provide valid inference.',
        'educational': (
            'Clustered standard errors allow errors to be correlated within clusters (e.g., within entities in panel data) '
            'while maintaining independence across clusters. This addresses both heteroskedasticity and within-cluster '
            'correlation (e.g., serial correlation). The cluster-robust variance estimator uses the sum of outer products '
            'of residuals within each cluster. Clustering is essential for panel data (cluster at entity level) and '
            'grouped data (cluster at group level). The number of clusters matters - with few clusters (< 50), inference '
            'may be unreliable. Two-way clustering (entity and time) accounts for both dimensions of correlation in panel data.'
        )
    },
    
    # Diagnostic Interpretations
    'diagnostic_first_stage_f': {
        'basic': 'First-stage F-statistic tests instrument relevance. F > 10 indicates strong instruments; F < 10 suggests weak instruments and potential bias.',
        'educational': (
            'The first-stage F-statistic tests the joint significance of instruments in the first-stage regression. '
            'A rule of thumb is F > 10 indicates "strong" instruments, while F < 10 suggests "weak" instruments. '
            'Weak instruments cause several problems: (1) IV estimates are biased toward OLS, (2) confidence intervals '
            'are unreliable (too narrow), (3) tests have incorrect size. The F-statistic should exclude covariates - '
            'it tests the incremental explanatory power of instruments. Stock-Yogo critical values provide formal weak '
            'instrument tests for multiple instruments. With weak instruments, consider: (1) LIML (Limited Information '
            'Maximum Likelihood), (2) Anderson-Rubin confidence intervals, (3) stronger instruments.'
        )
    },
    
    'diagnostic_overidentification': {
        'basic': 'Overidentification tests (Sargan, Hansen J) check instrument validity when you have more instruments than endogenous variables.',
        'educational': (
            'Overidentification tests (Sargan test, Hansen J-test) test the validity of over-identifying restrictions. '
            'When you have more instruments than endogenous variables, the extra instruments provide a test of the '
            'exclusion restriction. The test checks whether instruments are uncorrelated with the error term (validity). '
            'Rejection (p < 0.05) suggests that at least one instrument is invalid (violates exclusion restriction). '
            'However, the test has low power and failure to reject does not prove validity. The test is typically '
            'non-robust (assumes homoskedasticity), though robust versions exist. Overidentification tests are only '
            'available when over-identified (more instruments than endogenous variables).'
        )
    },
    
    'diagnostic_parallel_trends': {
        'basic': 'Parallel trends test checks whether treated and control groups had similar pre-treatment trends, validating the DiD identifying assumption.',
        'educational': (
            'The parallel trends assumption is the key identifying assumption for difference-in-differences. Pre-treatment '
            'trends tests examine whether the treated and control groups had similar trends before treatment. This is typically '
            'done by: (1) event study (interacting treatment with leads of time), (2) comparing pre-treatment coefficients, '
            'or (3) placebo tests with fake treatment dates. If pre-treatment coefficients are jointly insignificant, this '
            'supports the parallel trends assumption. However, pre-treatment trends tests have low power, and failure to reject '
            'does not guarantee parallel trends. Visual inspection of trends is also important. Violations suggest that DiD '
            'may not be appropriate, or that controls/alternative specifications are needed.'
        )
    },
    
    'diagnostic_hausman': {
        'basic': 'Hausman test compares fixed effects and random effects to determine whether unobserved heterogeneity is correlated with regressors.',
        'educational': (
            'The Hausman test compares fixed effects (FE) and random effects (RE) estimates to test whether unobserved '
            'heterogeneity is correlated with regressors. The null hypothesis is that RE is appropriate (unobserved effects '
            'are uncorrelated with regressors). Under H0, both FE and RE are consistent, but RE is more efficient. Under H1 '
            '(correlation exists), FE is consistent but RE is biased. The test statistic is (β_FE - β_RE)\' * Var(β_FE - β_RE)^(-1) '
            '* (β_FE - β_RE) ~ χ²(k). Rejection (p < 0.05) suggests using FE. The test requires that FE and RE estimate the '
            'same parameters (time-invariant variables are not identified in FE). If the test rejects, use FE; if it fails to '
            'reject, RE may be more efficient.'
        )
    }
}


__all__ = ['get_explanation', 'toggle_explanation_mode', 'get_wooldridge_citation', 'WOOLDRIDGE_CITATIONS']

