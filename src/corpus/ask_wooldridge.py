"""Ask Wooldridge: Natural language query interface for econometric guidance.

Enables natural language queries to Wooldridge's textbook for authoritative
methodological guidance. Uses keyword-based search (no embeddings/RAG).

Reference:
Wooldridge, J.M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
MIT Press.
"""

from typing import Dict, List, Optional, Any
from .wooldridge_search import WooldridgeSearch
from .wooldridge_page_index import (
    METHODOLOGY_PAGES,
    DIAGNOSTIC_THRESHOLDS,
    get_wooldridge_citation,
    get_page_range
)


# Pre-defined guidance for common questions
WOOLDRIDGE_GUIDANCE: Dict[str, Dict[str, Any]] = {
    # Model Selection
    'fe_vs_re': {
        'question_patterns': [
            'fixed effects vs random effects',
            'fe or re',
            'when to use fixed effects',
            'when to use random effects',
            'hausman test interpretation'
        ],
        'pages': (291, 300),
        'chapter': 10,
        'recommendation': (
            "Use the Hausman test to decide between FE and RE. "
            "H0: Random effects is consistent (uncorrelated with regressors). "
            "If p < 0.05, reject H0 and use Fixed Effects. "
            "If p >= 0.05, RE is more efficient but FE is still consistent."
        ),
        'citation': 'Wooldridge, Ch. 10, Section 10.7.3, p.291-300'
    },

    'weak_instruments': {
        'question_patterns': [
            'weak instruments',
            'first stage f statistic',
            'f < 10',
            'staiger stock',
            'what if f statistic is low'
        ],
        'pages': (101, 103),
        'chapter': 5,
        'recommendation': (
            "The Staiger-Stock rule of thumb: F-statistic > 10 indicates strong instruments. "
            "For F < 10: (1) Consider LIML instead of 2SLS, (2) Use Anderson-Rubin "
            "confidence intervals, (3) Look for stronger instruments. "
            "Weak instruments bias IV toward OLS and cause unreliable inference."
        ),
        'citation': 'Wooldridge, Ch. 5, p.101-103 (Staiger-Stock rule)'
    },

    'overidentification': {
        'question_patterns': [
            'overidentification test',
            'sargan test',
            'hansen j test',
            'too many instruments',
            'instrument validity'
        ],
        'pages': (122, 124),
        'chapter': 6,
        'recommendation': (
            "The Sargan/Hansen J test tests overidentifying restrictions. "
            "H0: All instruments are valid (uncorrelated with errors). "
            "If p < 0.05, reject H0 - at least one instrument is invalid. "
            "Note: This test has low power. Failure to reject does NOT prove validity."
        ),
        'citation': 'Wooldridge, Ch. 6, Section 6.2.2, p.122-124'
    },

    'clustered_se': {
        'question_patterns': [
            'clustered standard errors',
            'when to cluster',
            'cluster at what level',
            'serial correlation panel'
        ],
        'pages': (274, 276),
        'chapter': 10,
        'recommendation': (
            "Cluster standard errors at the level where errors are correlated. "
            "For panel data, cluster at the entity level to account for serial correlation. "
            "The number of clusters matters: with < 50 clusters, inference may be unreliable. "
            "Consider wild bootstrap or bias-corrected standard errors for few clusters."
        ),
        'citation': 'Wooldridge, Ch. 10, Section 10.5.4, p.274-276'
    },

    'parallel_trends': {
        'question_patterns': [
            'parallel trends',
            'difference in differences assumption',
            'did assumption',
            'pre-treatment trends'
        ],
        'pages': (713, 720),
        'chapter': 21,
        'recommendation': (
            "The parallel trends assumption is key for DiD: absent treatment, "
            "treated and control groups would follow parallel trends. "
            "Test using: (1) Event study with pre-treatment leads, "
            "(2) Placebo tests with fake treatment dates. "
            "Pre-treatment coefficients should be jointly insignificant."
        ),
        'citation': 'Wooldridge, Ch. 21, Section 21.4, p.713-720'
    },

    'robust_se': {
        'question_patterns': [
            'robust standard errors',
            'heteroskedasticity',
            'hc1 hc2 hc3',
            'white standard errors'
        ],
        'pages': (55, 58),
        'chapter': 4,
        'recommendation': (
            "Robust (heteroskedasticity-consistent) standard errors: "
            "HC1 = (n/(n-k)) * robust, HC2 adjusts for leverage, "
            "HC3 (jackknife) is preferred for small samples. "
            "Use HC3 when n/k < 100. Robust SEs address heteroskedasticity "
            "but not endogeneity - coefficients may still be biased."
        ),
        'citation': 'Wooldridge, Ch. 4, Section 4.2.3, p.55-58'
    },

    'endogeneity': {
        'question_patterns': [
            'endogeneity test',
            'is my variable endogenous',
            'durbin wu hausman',
            'test for endogeneity'
        ],
        'pages': (118, 122),
        'chapter': 6,
        'recommendation': (
            "The Durbin-Wu-Hausman test for endogeneity: "
            "Regress endogenous variable on instruments + controls (first stage). "
            "Add first-stage residuals to the main equation. "
            "If coefficient on residuals is significant (p < 0.05), "
            "reject exogeneity and use IV."
        ),
        'citation': 'Wooldridge, Ch. 6, Section 6.2.1, p.118-122'
    },

    'propensity_score': {
        'question_patterns': [
            'propensity score',
            'matching estimator',
            'selection on observables',
            'overlap assumption'
        ],
        'pages': (704, 710),
        'chapter': 21,
        'recommendation': (
            "Propensity score matching requires: "
            "(1) Unconfoundedness: all confounders observed, "
            "(2) Overlap: common support in propensity scores. "
            "Trim observations with extreme scores (typically 0.1-0.9). "
            "Matching provides ATT. Check covariate balance after matching."
        ),
        'citation': 'Wooldridge, Ch. 21, Section 21.3, p.704-710'
    },

    'first_differencing': {
        'question_patterns': [
            'first differencing',
            'first difference vs fixed effects',
            'fd or fe'
        ],
        'pages': (279, 284),
        'chapter': 10,
        'recommendation': (
            "First differencing (FD) and Fixed Effects (FE) both remove entity fixed effects. "
            "FD is more efficient if errors are random walk. "
            "FE is more efficient if errors are serially uncorrelated. "
            "In practice, FE is more commonly used. "
            "If T is large and errors are persistent, consider FD."
        ),
        'citation': 'Wooldridge, Ch. 10, Section 10.6, p.279-284'
    }
}


def ask_wooldridge(
    question: str,
    context: Optional[Dict[str, Any]] = None,
    top_k: int = 3
) -> Dict[str, Any]:
    """Query Wooldridge corpus for authoritative econometric guidance.

    Uses keyword matching to find relevant guidance. Falls back to
    corpus search if no pre-defined guidance matches.

    Args:
        question: Natural language question (e.g., "When should I use FE vs RE?")
        context: Optional model context (e.g., {'method': 'panel_iv', 'f_stat': 8.5})
        top_k: Number of corpus search results if pre-defined guidance not found

    Returns:
        Dictionary with:
            - answer: Synthesized guidance
            - citations: List of page references
            - source: 'predefined' or 'corpus_search'
            - confidence: 'high', 'medium', or 'low'
            - related_topics: List of related methodology names
    """
    question_lower = question.lower()

    # Step 1: Check pre-defined guidance
    for topic_key, guidance in WOOLDRIDGE_GUIDANCE.items():
        for pattern in guidance['question_patterns']:
            if pattern in question_lower:
                return {
                    'answer': guidance['recommendation'],
                    'citations': [guidance['citation']],
                    'source': 'predefined',
                    'confidence': 'high',
                    'topic': topic_key,
                    'pages': guidance['pages'],
                    'chapter': guidance['chapter'],
                    'related_topics': _get_related_topics(topic_key)
                }

    # Step 2: Fall back to corpus search
    searcher = WooldridgeSearch()
    results = searcher.search_wooldridge(question, top_k=top_k)

    if not results:
        return {
            'answer': (
                f"No specific guidance found for: '{question}'. "
                "Try rephrasing or searching for specific topics like "
                "'fixed effects', 'instrumental variables', or 'propensity score'."
            ),
            'citations': [],
            'source': 'not_found',
            'confidence': 'low',
            'related_topics': []
        }

    # Build answer from search results
    answer_parts = [f"From Wooldridge on '{question}':\n"]
    citations = []

    for i, result in enumerate(results, 1):
        title = result['title']
        content = result['content'][:300]
        citation = result.get('citation', result['file_name'])

        answer_parts.append(f"\n{i}. **{title}**")
        answer_parts.append(f"   {content}...")

        if 'citation' in result:
            citations.append(result['citation'])

    return {
        'answer': '\n'.join(answer_parts),
        'citations': citations if citations else [f"Search results from {results[0]['file_name']}"],
        'source': 'corpus_search',
        'confidence': 'medium' if len(results) >= 2 else 'low',
        'related_topics': []
    }


def get_methodology_recommendation(
    method: str,
    diagnostics: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Get Wooldridge's recommendation for a specific methodology.

    Provides context-aware guidance based on diagnostic results.

    Args:
        method: Method name (e.g., 'fixed_effects', 'iv', 'matching')
        diagnostics: Optional diagnostic results (e.g., {'f_stat': 8.5, 'hausman_p': 0.03})

    Returns:
        Dictionary with methodology-specific guidance
    """
    # Normalize method name
    method_key = method.lower().replace(' ', '_').replace('-', '_')

    # Get page reference
    citation = get_wooldridge_citation(method_key)
    pages = get_page_range(method_key)

    # Build base recommendation
    result = {
        'method': method,
        'citation': citation,
        'pages': pages,
        'warnings': [],
        'recommendations': []
    }

    # Add diagnostic-specific recommendations
    if diagnostics:
        # Weak instruments warning
        if 'f_stat' in diagnostics or 'first_stage_f' in diagnostics:
            f_stat = diagnostics.get('f_stat', diagnostics.get('first_stage_f'))
            if f_stat < 10:
                result['warnings'].append(
                    f"Weak instruments detected (F = {f_stat:.2f} < 10). "
                    "Consider LIML instead of 2SLS. (Wooldridge, p.101-103)"
                )

        # Hausman test result
        if 'hausman_p' in diagnostics:
            p = diagnostics['hausman_p']
            if p < 0.05:
                result['recommendations'].append(
                    f"Hausman test rejects RE (p = {p:.3f}). Use Fixed Effects. "
                    "(Wooldridge, p.291-300)"
                )
            else:
                result['recommendations'].append(
                    f"Hausman test does not reject RE (p = {p:.3f}). RE is more efficient. "
                    "(Wooldridge, p.291-300)"
                )

        # Overidentification test
        if 'sargan_p' in diagnostics or 'overid_p' in diagnostics:
            p = diagnostics.get('sargan_p', diagnostics.get('overid_p'))
            if p < 0.05:
                result['warnings'].append(
                    f"Overidentification test rejects (p = {p:.3f}). "
                    "At least one instrument may be invalid. (Wooldridge, p.122-124)"
                )

    # Get additional context from corpus
    searcher = WooldridgeSearch()
    guidance = searcher.get_methodology_guidance(method)
    result['textbook_guidance'] = guidance

    return result


def _get_related_topics(topic: str) -> List[str]:
    """Get related topics for a given topic."""
    related = {
        'fe_vs_re': ['hausman_test', 'fixed_effects', 'random_effects', 'clustered_se'],
        'weak_instruments': ['2sls', 'instrumental_variables', 'overidentification'],
        'overidentification': ['instrumental_variables', '2sls', 'weak_instruments'],
        'clustered_se': ['fixed_effects', 'panel_data', 'robust_se'],
        'parallel_trends': ['diff_in_diff', 'treatment_effects'],
        'robust_se': ['heteroskedasticity_robust', 'clustered_se', 'hc_variants'],
        'endogeneity': ['instrumental_variables', '2sls', 'weak_instruments'],
        'propensity_score': ['matching', 'treatment_effects'],
        'first_differencing': ['fixed_effects', 'panel_data']
    }
    return related.get(topic, [])


def list_available_topics() -> List[str]:
    """List all topics with pre-defined guidance."""
    return list(WOOLDRIDGE_GUIDANCE.keys())


__all__ = [
    'ask_wooldridge',
    'get_methodology_recommendation',
    'list_available_topics',
    'WOOLDRIDGE_GUIDANCE'
]
