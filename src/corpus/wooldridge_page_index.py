"""Wooldridge textbook page index for precise citations.

Maps econometric methodologies to specific page ranges in:
Wooldridge, J.M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
MIT Press.
"""

from typing import Dict, Optional, Tuple


# Methodology to page mappings (Wooldridge 2nd edition)
METHODOLOGY_PAGES: Dict[str, Dict] = {
    # Panel Data - Chapter 10
    "fixed_effects": {
        "pages": (263, 297),
        "chapter": 10,
        "section": "10.5",
        "title": "Fixed Effects Estimation"
    },
    "random_effects": {
        "pages": (257, 265),
        "chapter": 10,
        "section": "10.4",
        "title": "Random Effects Methods"
    },
    "hausman_test": {
        "pages": (291, 300),
        "chapter": 10,
        "section": "10.7.3",
        "title": "Hausman Test"
    },
    "first_difference": {
        "pages": (279, 284),
        "chapter": 10,
        "section": "10.6",
        "title": "First-Differencing Estimation"
    },
    "clustered_se": {
        "pages": (274, 276),
        "chapter": 10,
        "section": "10.5.4",
        "title": "Clustered Standard Errors"
    },
    "panel_data": {
        "pages": (247, 297),
        "chapter": 10,
        "section": "10",
        "title": "Basic Linear Unobserved Effects Panel Data Models"
    },

    # Dynamic Panel - Chapter 11
    "dynamic_panel": {
        "pages": (299, 337),
        "chapter": 11,
        "section": "11",
        "title": "More Topics in Linear Unobserved Effects Models"
    },
    "hausman_taylor": {
        "pages": (325, 330),
        "chapter": 11,
        "section": "11.3.4",
        "title": "Hausman-Taylor Estimator"
    },

    # Instrumental Variables - Chapter 5
    "instrumental_variables": {
        "pages": (83, 113),
        "chapter": 5,
        "section": "5",
        "title": "Instrumental Variables Estimation of Single-Equation Linear Models"
    },
    "2sls": {
        "pages": (90, 100),
        "chapter": 5,
        "section": "5.1.2",
        "title": "Two-Stage Least Squares"
    },
    "weak_instruments": {
        "pages": (101, 103),
        "chapter": 5,
        "section": "5.2.6",
        "title": "Weak Instruments (Staiger-Stock rule: F > 10)"
    },
    "iv_asymptotics": {
        "pages": (103, 108),
        "chapter": 5,
        "section": "5.2",
        "title": "Asymptotic Properties of IV"
    },

    # Specification Tests - Chapter 6
    "overidentification": {
        "pages": (122, 124),
        "chapter": 6,
        "section": "6.2.2",
        "title": "Overidentification Test (Sargan/Hansen J)"
    },
    "endogeneity_test": {
        "pages": (118, 122),
        "chapter": 6,
        "section": "6.2.1",
        "title": "Testing for Endogeneity"
    },
    "reset_test": {
        "pages": (124, 125),
        "chapter": 6,
        "section": "6.2.3",
        "title": "RESET Test for Functional Form"
    },

    # GMM - Chapter 8
    "gmm": {
        "pages": (195, 240),
        "chapter": 8,
        "section": "8",
        "title": "Generalized Method of Moments"
    },
    "gmm_estimation": {
        "pages": (195, 210),
        "chapter": 8,
        "section": "8.2",
        "title": "GMM Estimation"
    },

    # Robust Inference - Chapter 4
    "heteroskedasticity_robust": {
        "pages": (55, 58),
        "chapter": 4,
        "section": "4.2.3",
        "title": "Heteroskedasticity-Robust Inference"
    },
    "robust_se": {
        "pages": (55, 58),
        "chapter": 4,
        "section": "4.2.3",
        "title": "Robust Standard Errors (White/Huber/Eicker)"
    },
    "hc_variants": {
        "pages": (57, 58),
        "chapter": 4,
        "section": "4.2.3",
        "title": "HC0, HC1, HC2, HC3 Variants"
    },

    # Discrete Response - Chapter 15
    "probit": {
        "pages": (453, 490),
        "chapter": 15,
        "section": "15",
        "title": "Discrete Response Models"
    },
    "logit": {
        "pages": (453, 490),
        "chapter": 15,
        "section": "15",
        "title": "Logit Models"
    },
    "propensity_score": {
        "pages": (485, 490),
        "chapter": 15,
        "section": "15.7",
        "title": "Propensity Score Methods"
    },
    "marginal_effects": {
        "pages": (467, 475),
        "chapter": 15,
        "section": "15.5",
        "title": "Marginal Effects in Nonlinear Models"
    },

    # Limited Dependent Variables - Chapter 16
    "tobit": {
        "pages": (525, 540),
        "chapter": 16,
        "section": "16.2",
        "title": "Tobit Model"
    },
    "censored_regression": {
        "pages": (525, 545),
        "chapter": 16,
        "section": "16",
        "title": "Censored and Truncated Regression"
    },

    # Treatment Effects - Chapter 21
    "treatment_effects": {
        "pages": (697, 741),
        "chapter": 21,
        "section": "21",
        "title": "Estimating Average Treatment Effects"
    },
    "matching": {
        "pages": (704, 710),
        "chapter": 21,
        "section": "21.3",
        "title": "Matching Estimators"
    },
    "diff_in_diff": {
        "pages": (713, 720),
        "chapter": 21,
        "section": "21.4",
        "title": "Difference-in-Differences"
    },
    "regression_discontinuity": {
        "pages": (720, 725),
        "chapter": 21,
        "section": "21.5",
        "title": "Regression Discontinuity"
    },
}

# Common diagnostic thresholds from Wooldridge
DIAGNOSTIC_THRESHOLDS: Dict[str, Dict] = {
    "first_stage_f": {
        "threshold": 10,
        "page": 101,
        "citation": "Staiger and Stock (1997), as discussed in Wooldridge p.101-103",
        "interpretation": "F < 10 indicates weak instruments; consider LIML"
    },
    "sargan_p": {
        "threshold": 0.05,
        "page": 122,
        "citation": "Wooldridge, Ch. 6, p.122-124",
        "interpretation": "p < 0.05 rejects validity of overidentifying restrictions"
    },
    "hausman_p": {
        "threshold": 0.05,
        "page": 291,
        "citation": "Wooldridge, Ch. 10, Section 10.7.3, p.291-300",
        "interpretation": "p < 0.05 rejects RE consistency; use FE instead"
    },
    "vif": {
        "threshold": 10,
        "page": 57,
        "citation": "Wooldridge, Ch. 4",
        "interpretation": "VIF > 10 indicates concerning multicollinearity"
    },
    "hc3_small_sample": {
        "threshold": 100,  # n/k ratio
        "page": 57,
        "citation": "Wooldridge, Ch. 4, p.57-58",
        "interpretation": "Use HC3 when n/k < 100 for better small-sample properties"
    },
}


def get_wooldridge_citation(topic: str) -> str:
    """Return formatted citation for a topic.

    Args:
        topic: Methodology name (e.g., "fixed_effects", "hausman_test")

    Returns:
        Formatted citation string (e.g., "Wooldridge, Ch. 10, p.291-300")
    """
    topic_key = topic.lower().replace(' ', '_').replace('-', '_')

    if topic_key in METHODOLOGY_PAGES:
        info = METHODOLOGY_PAGES[topic_key]
        pages = info['pages']
        chapter = info['chapter']
        section = info.get('section', '')

        if section:
            return f"Wooldridge, Ch. {chapter}, Section {section}, p.{pages[0]}-{pages[1]}"
        return f"Wooldridge, Ch. {chapter}, p.{pages[0]}-{pages[1]}"

    return f"Wooldridge (2010)"


def get_page_range(topic: str) -> Optional[Tuple[int, int]]:
    """Get page range for a methodology.

    Args:
        topic: Methodology name

    Returns:
        Tuple of (start_page, end_page) or None if not found
    """
    topic_key = topic.lower().replace(' ', '_').replace('-', '_')

    if topic_key in METHODOLOGY_PAGES:
        return METHODOLOGY_PAGES[topic_key]['pages']
    return None


def get_diagnostic_threshold(diagnostic: str) -> Optional[Dict]:
    """Get threshold information for a diagnostic test.

    Args:
        diagnostic: Diagnostic name (e.g., "first_stage_f", "hausman_p")

    Returns:
        Dictionary with threshold, page, citation, and interpretation
    """
    diag_key = diagnostic.lower().replace(' ', '_').replace('-', '_')

    if diag_key in DIAGNOSTIC_THRESHOLDS:
        return DIAGNOSTIC_THRESHOLDS[diag_key]
    return None


def list_topics() -> Dict[str, str]:
    """List all available topics with their titles.

    Returns:
        Dictionary mapping topic keys to titles
    """
    return {k: v['title'] for k, v in METHODOLOGY_PAGES.items()}
