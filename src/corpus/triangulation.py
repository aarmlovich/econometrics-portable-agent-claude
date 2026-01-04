"""Triangulation system for comparing Wooldridge, Hansen, and Angrist perspectives."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from src.corpus.agent_integration import get_wooldridge_perspective, triangulate_methodology


def triangulate(methodology: str) -> Dict[str, Any]:
    """Full triangulation query comparing all three perspectives.

    Args:
        methodology: Methodology name

    Returns:
        Dictionary with:
            - methodology: Methodology name
            - wooldridge: Wooldridge's perspective
            - hansen: Hansen's perspective
            - angrist: Angrist's perspective
            - agreement_level: "high", "medium", or "low"
            - synthesis: Recommended approach
    """
    # Get cross-reference (includes all three)
    cross_ref = triangulate_methodology(methodology)

    # Determine agreement level
    agreement_level = _determine_agreement_level(cross_ref)

    # Generate synthesis
    synthesis = _generate_synthesis(cross_ref, agreement_level)

    return {
        "methodology": methodology,
        "wooldridge": cross_ref.get("wooldridge", {}),
        "hansen": cross_ref.get("hansen"),
        "angrist": cross_ref.get("angrist"),
        "agreement_level": agreement_level,
        "synthesis": synthesis,
        "agent_rules": cross_ref.get("agent_rules", []),
    }


def compare_standard_errors(context: str) -> Dict[str, Any]:
    """Compare standard error approaches across all three perspectives.
    
    Args:
        context: Context string (e.g., "panel_data", "limited_dependent_variable", "time_series", "cross_sectional")
        
    Returns:
        Dictionary with SE comparison
    """
    context_lower = context.lower()
    
    # Determine which SE type to compare
    if "panel" in context_lower or "fixed effects" in context_lower:
        se_type = "clustered standard errors"
    elif "limited" in context_lower or "ldv" in context_lower or "binary" in context_lower:
        se_type = "HC3"
    elif "time series" in context_lower or "autocorrelation" in context_lower:
        se_type = "HAC standard errors"
    else:
        se_type = "robust standard errors"
    
    # Get triangulation
    result = triangulate(se_type)
    
    # Add context-specific guidance
    result["context"] = context
    result["se_type"] = se_type
    result["recommendation"] = _get_se_recommendation(context, result)
    
    return result


def compare_panel_methods() -> Dict[str, Any]:
    """Compare panel data methods across all three perspectives.
    
    Returns:
        Dictionary with panel methods comparison
    """
    methods = ["fixed effects", "clustered standard errors", "attrition"]
    
    comparisons = {}
    for method in methods:
        comparisons[method] = triangulate(method)
    
    # Overall synthesis
    synthesis = _synthesize_panel_methods(comparisons)
    
    return {
        "methods": comparisons,
        "synthesis": synthesis,
        "agreement_level": "high",  # Panel data has high agreement
    }


def synthesize_recommendation(triangulation: Dict[str, Any]) -> str:
    """Generate synthesis recommendation from triangulation.
    
    Args:
        triangulation: Triangulation dictionary from triangulate()
        
    Returns:
        Formatted synthesis recommendation string
    """
    methodology = triangulation.get("methodology", "Unknown")
    agreement_level = triangulation.get("agreement_level", "medium")
    synthesis = triangulation.get("synthesis", "")
    
    lines = [f"**Synthesis for {methodology}:**\n"]
    
    if agreement_level == "high":
        lines.append("**High Agreement** - All three perspectives align:")
    elif agreement_level == "medium":
        lines.append("**Medium Agreement** - Perspectives can be synthesized:")
    else:
        lines.append("**Different Perspectives** - Synthesis required:")
    
    lines.append(f"\n{synthesis}")
    
    # Add perspective summaries
    wooldridge = triangulation.get("wooldridge", {})
    hansen = triangulation.get("hansen")
    angrist = triangulation.get("angrist")
    
    if wooldridge:
        lines.append("\n**Wooldridge:**")
        sections = wooldridge.get("sections", [])
        if sections:
            lines.append(f"  Found {len(sections)} relevant sections")
            # Get chapter reference if available
            chapter = _get_chapter_for_methodology(methodology)
            if chapter:
                lines.append(f"  Reference: {chapter}")
    
    if hansen:
        lines.append("\n**Hansen:**")
        if hansen.get("file"):
            lines.append(f"  See: {hansen['file']}")
        if hansen.get("mentions"):
            lines.append(f"  Mentions: {len(hansen['mentions'])}")
    
    if angrist:
        lines.append("\n**Angrist/MHE:**")
        if angrist.get("file"):
            lines.append(f"  See: {angrist['file']}")
        if angrist.get("mentions"):
            lines.append(f"  Mentions: {len(angrist['mentions'])}")
    
    return "\n".join(lines)


def _determine_agreement_level(cross_ref: Dict[str, Any]) -> str:
    """Determine agreement level from cross-reference.
    
    Args:
        cross_ref: Cross-reference dictionary
        
    Returns:
        "high", "medium", or "low"
    """
    # Check if all three have perspectives
    has_wooldridge = bool(cross_ref.get("wooldridge", {}).get("sections"))
    has_hansen = bool(cross_ref.get("hansen"))
    has_angrist = bool(cross_ref.get("angrist"))
    
    # High agreement: All three have perspectives and align
    # For now, we'll use a simple heuristic
    # In practice, this would analyze the actual content
    
    # Known high agreement areas
    high_agreement_methods = [
        "clustered standard errors",
        "fixed effects",
        "robustness checks",
        "reproducibility",
    ]
    
    methodology = cross_ref.get("methodology", "").lower()
    if any(method in methodology for method in high_agreement_methods):
        return "high"
    
    # Medium if at least two have perspectives
    if (has_wooldridge and has_hansen) or (has_wooldridge and has_angrist):
        return "medium"
    
    return "low"


def _generate_synthesis(cross_ref: Dict[str, Any], agreement_level: str) -> str:
    """Generate synthesis recommendation.
    
    Args:
        cross_ref: Cross-reference dictionary
        agreement_level: Agreement level
        
    Returns:
        Synthesis recommendation string
    """
    methodology = cross_ref.get("methodology", "")
    
    # Known syntheses from evaluation documents
    known_syntheses = {
        "fixed effects": (
            "Use Wooldridge's approach (clustered SE with small-sample correction), "
            "validated by Hansen's modern practices, and applied to identification problems (Angrist)."
        ),
        "clustered standard errors": (
            "All three agree on clustering for panel data. We use Wooldridge's approach "
            "(clustered with small-sample correction) as default, validated by Hansen's modern practices."
        ),
        "robust standard errors": (
            "We use robust SE (HC1) as default (Hansen's modern practice), with context-specific options: "
            "HC3 for limited dependent variables (Wooldridge), clustered for panel data (all three), "
            "and HAC for time series (Wooldridge)."
        ),
        "treatment effects": (
            "We use Angrist's identification strategies (DiD, RD, Matching, IV) with Hansen's rigorous methods "
            "and diagnostics, and Wooldridge's panel expertise for panel treatment effects."
        ),
    }
    
    # Check for known synthesis
    methodology_lower = methodology.lower()
    for key, synthesis in known_syntheses.items():
        if key in methodology_lower:
            return synthesis
    
    # Default synthesis based on agreement level
    if agreement_level == "high":
        return (
            f"All three perspectives agree on the approach for {methodology}. "
            "We follow this consensus, which provides high confidence in our methodology."
        )
    elif agreement_level == "medium":
        return (
            f"For {methodology}, we synthesize insights from all three perspectives: "
            "Wooldridge's expertise, Hansen's modern practices, and Angrist's identification focus."
        )
    else:
        return (
            f"For {methodology}, perspectives differ. We use a synthesis that combines "
            "Wooldridge's context-appropriate methods, Hansen's modern practices, and Angrist's identification focus."
        )


def _get_se_recommendation(context: str, comparison: Dict[str, Any]) -> str:
    """Get standard error recommendation for specific context.
    
    Args:
        context: Context string
        comparison: SE comparison dictionary
        
    Returns:
        Recommendation string
    """
    context_lower = context.lower()
    se_type = comparison.get("se_type", "")
    
    if "panel" in context_lower:
        return (
            "For panel data, use clustered standard errors with small-sample correction "
            "(Wooldridge's approach, validated by all three perspectives)."
        )
    elif "limited" in context_lower or "ldv" in context_lower:
        return (
            "For limited dependent variables, use HC3 (jackknife) standard errors "
            "(Wooldridge's recommendation for these models)."
        )
    elif "time series" in context_lower:
        return (
            "For time series, use HAC (heteroskedasticity and autocorrelation consistent) "
            "standard errors (Wooldridge's approach for time-ordered data)."
        )
    else:
        return (
            "For cross-sectional data, use robust (HC1) standard errors as default "
            "(Hansen's modern practice), with context-specific options available."
        )


def _synthesize_panel_methods(comparisons: Dict[str, Dict]) -> str:
    """Synthesize panel methods from multiple comparisons.
    
    Args:
        comparisons: Dictionary of method comparisons
        
    Returns:
        Synthesis string
    """
    return (
        "For panel data methods, we use Wooldridge's comprehensive approach (clustered SE with "
        "small-sample correction, understanding of mechanics, attrition handling) validated by "
        "Hansen's modern practices (robust SE, explicit diagnostics) and applied to identification "
        "problems (Angrist's focus). All three perspectives agree on the importance of clustering "
        "and proper inference in panel data."
    )


def _get_chapter_for_methodology(methodology: str) -> Optional[str]:
    """Get Wooldridge chapter reference for methodology.
    
    Args:
        methodology: Methodology name
        
    Returns:
        Chapter reference or None
    """
    chapter_mappings = {
        "fixed effects": "Chapter 23",
        "random effects": "Chapter 23",
        "panel data": "Chapter 23",
        "panel iv": "Chapter 24",
        "instrumental variables": "Chapter 4-5",
        "treatment effects": "Chapter 21",
        "difference-in-differences": "Chapter 21, 28",
        "matching": "Chapter 21",
        "regression discontinuity": "Chapter 21",
        "clustered standard errors": "Chapter 23",
        "attrition": "Chapter 26",
        "survey weights": "Chapter 20",
        "HAC standard errors": "Chapter 12",
        "HC3": "Chapter 17",
    }
    
    methodology_lower = methodology.lower()
    for key, chapter in chapter_mappings.items():
        if key in methodology_lower:
            return chapter
    
    return None



