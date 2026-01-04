"""Helper functions for agent to quickly access Wooldridge corpus."""

from typing import Dict, List, Optional
from src.corpus.agent_integration import (
    get_wooldridge_perspective,
    semantic_search_wooldridge,
    lookup_topic_wooldridge,
    get_methodology_guidance,
)


def quick_lookup(methodology: str) -> str:
    """Fast perspective lookup with formatted response.
    
    Args:
        methodology: Methodology name
        
    Returns:
        Formatted string with Wooldridge's perspective
    """
    perspective = get_wooldridge_perspective(methodology)
    
    # Quick summary format
    sections = perspective.get("sections", [])
    wooldridge_perspective = perspective.get("wooldridge_perspective", [])
    
    if not sections and not wooldridge_perspective:
        return f"No Wooldridge perspective found for '{methodology}'."
    
    summary = f"**Wooldridge on {methodology}:**\n"
    
    if wooldridge_perspective:
        summary += f"Found {len(wooldridge_perspective)} recommendations.\n"
        # Include first recommendation context
        first = wooldridge_perspective[0]
        context = first.get("context", "")[:150]
        summary += f"Key point: {context}...\n"
    
    if sections:
        summary += f"Found in {len(sections)} sections.\n"
        # List first few files
        files = set(s.get("file_name", "") for s in sections[:3])
        summary += f"Files: {', '.join(files)}\n"
    
    return summary


def get_standard_error_guidance(context: str) -> Dict:
    """Get standard error guidance based on context.
    
    Args:
        context: Context string (e.g., "panel_data", "limited_dependent_variable", "time_series")
        
    Returns:
        Dictionary with SE guidance from Wooldridge
    """
    context_lower = context.lower()
    
    if "panel" in context_lower or "fixed effects" in context_lower:
        return get_methodology_guidance("clustered standard errors")
    elif "limited" in context_lower or "ldv" in context_lower or "binary" in context_lower:
        return get_methodology_guidance("HC3")
    elif "time series" in context_lower or "autocorrelation" in context_lower:
        return get_methodology_guidance("HAC standard errors")
    elif "cross section" in context_lower or "ols" in context_lower:
        return get_methodology_guidance("robust standard errors")
    else:
        # Default to general SE guidance
        return get_methodology_guidance("standard errors")


def get_panel_data_guidance() -> Dict:
    """Get comprehensive panel data guidance from Wooldridge.
    
    Returns:
        Dictionary with panel data guidance
    """
    # Get multiple perspectives
    fixed_effects = get_methodology_guidance("fixed effects")
    clustered_se = get_methodology_guidance("clustered standard errors")
    attrition = get_methodology_guidance("attrition")
    
    return {
        "fixed_effects": fixed_effects,
        "clustered_standard_errors": clustered_se,
        "attrition": attrition,
        "summary": "Panel data methods from Wooldridge (Chapter 23-26)",
    }


def compare_approaches(methodology: str) -> str:
    """Get formatted comparison of approaches.
    
    Args:
        methodology: Methodology name
        
    Returns:
        Formatted string comparing Wooldridge, Hansen, and Angrist
    """
    guidance = get_methodology_guidance(methodology, include_triangulation=True)
    
    wooldridge = guidance["wooldridge"]
    triangulation = guidance.get("triangulation", {})
    
    lines = [f"**Comparison: {methodology}**\n"]
    
    # Wooldridge
    lines.append("**Wooldridge:**")
    if wooldridge.get("wooldridge_perspective"):
        persp = wooldridge["wooldridge_perspective"][0]
        context = persp.get("context", "")[:200]
        lines.append(f"  {context}...")
    else:
        lines.append("  See Wooldridge corpus for details.")
    
    # Hansen
    if triangulation.get("hansen"):
        hansen = triangulation["hansen"]
        lines.append("\n**Hansen:**")
        if hansen.get("mentions"):
            lines.append(f"  Found in: {hansen.get('file', 'N/A')}")
            lines.append(f"  Mentions: {len(hansen.get('mentions', []))}")
        else:
            lines.append("  See HANSEN_EVALUATION.md")
    
    # Angrist
    if triangulation.get("angrist"):
        angrist = triangulation["angrist"]
        lines.append("\n**Angrist/MHE:**")
        if angrist.get("mentions"):
            lines.append(f"  Found in: {angrist.get('file', 'N/A')}")
            lines.append(f"  Mentions: {len(angrist.get('mentions', []))}")
        else:
            lines.append("  See ANGRIST_EVALUATION.md")
    
    # Synthesis
    if triangulation.get("agent_rules"):
        lines.append("\n**Agent Rules:**")
        for rule in triangulation["agent_rules"]:
            lines.append(f"  - {rule}")
    
    return "\n".join(lines)


def search_wooldridge_content(query: str, max_results: int = 3) -> str:
    """Search Wooldridge corpus and return formatted results.
    
    Args:
        query: Search query
        max_results: Maximum number of results to return
        
    Returns:
        Formatted string with search results
    """
    results = semantic_search_wooldridge(query, top_k=max_results)
    
    if not results:
        return f"No results found for '{query}' in Wooldridge corpus."
    
    lines = [f"**Wooldridge Corpus Search: '{query}'**\n"]
    lines.append(f"Found {len(results)} results:\n")
    
    for i, result in enumerate(results, 1):
        lines.append(f"**Result {i}** (relevance: {result['relevance_score']:.3f}):")
        metadata = result.get("metadata", {})
        lines.append(f"  File: {metadata.get('file_name', 'N/A')}")
        if metadata.get("section_title"):
            lines.append(f"  Section: {metadata['section_title']}")
        if metadata.get("page"):
            lines.append(f"  Page: {metadata['page']}")
        
        content = result.get("content", "")[:200]
        lines.append(f"  Content: {content}...\n")
    
    return "\n".join(lines)


def get_chapter_reference(methodology: str) -> Optional[str]:
    """Get Wooldridge chapter reference for a methodology.
    
    Args:
        methodology: Methodology name
        
    Returns:
        Chapter reference string or None
    """
    # Chapter mappings from wooldridge-references.mdc
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



