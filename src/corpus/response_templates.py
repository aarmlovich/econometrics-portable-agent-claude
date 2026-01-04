"""Response templates for formatting agent responses with Wooldridge references."""

from typing import Dict, List, Optional, Any


def format_wooldridge_citation(perspective: Dict[str, Any]) -> str:
    """Format Wooldridge citation for agent response.
    
    Args:
        perspective: Perspective dictionary from get_wooldridge_perspective()
        
    Returns:
        Formatted citation string
    """
    methodology = perspective.get("methodology", "Unknown")
    sections = perspective.get("sections", [])
    wooldridge_perspective = perspective.get("wooldridge_perspective", [])
    
    lines = [f"**Wooldridge's Perspective on {methodology}:**"]
    
    # Get chapter reference if available
    chapter = _get_chapter_reference(methodology)
    if chapter:
        lines.append(f"\n**Reference**: Wooldridge {chapter}")
    
    # Add recommendations
    if wooldridge_perspective:
        lines.append("\n**Key Recommendations:**")
        for i, persp in enumerate(wooldridge_perspective[:3], 1):
            context = persp.get("context", "").strip()
            if len(context) > 200:
                context = context[:200] + "..."
            lines.append(f"{i}. {context}")
            
            section = persp.get("section")
            page = persp.get("page")
            if section or page:
                ref_parts = []
                if section:
                    ref_parts.append(f"Section: {section}")
                if page:
                    ref_parts.append(f"Page: {page}")
                lines.append(f"   ({', '.join(ref_parts)})")
    
    # Add section references
    if sections:
        lines.append(f"\n**Found in {len(sections)} sections:**")
        for section in sections[:5]:
            file_name = section.get("file_name", "N/A")
            section_title = section.get("section", "N/A")
            page = section.get("page", "")
            
            ref = f"- {file_name}"
            if section_title != "N/A":
                ref += f": {section_title}"
            if page:
                ref += f" (p. {page})"
            lines.append(ref)
    
    return "\n".join(lines)


def format_triangulation_response(comparison: Dict[str, Any]) -> str:
    """Format triangulation comparison for agent response.
    
    Args:
        comparison: Triangulation dictionary from triangulate()
        
    Returns:
        Formatted triangulation response string
    """
    methodology = comparison.get("methodology", "Unknown")
    agreement_level = comparison.get("agreement_level", "medium")
    synthesis = comparison.get("synthesis", "")
    
    wooldridge = comparison.get("wooldridge", {})
    hansen = comparison.get("hansen")
    angrist = comparison.get("angrist")
    
    lines = [f"**Triangulation: {methodology}**\n"]
    
    # Agreement level header
    if agreement_level == "high":
        lines.append("**High Agreement** - All three perspectives align:\n")
    elif agreement_level == "medium":
        lines.append("**Medium Agreement** - Perspectives can be synthesized:\n")
    else:
        lines.append("**Different Perspectives** - Synthesis required:\n")
    
    # Wooldridge
    lines.append("**Wooldridge:**")
    if wooldridge.get("sections"):
        lines.append(f"  Found {len(wooldridge['sections'])} relevant sections")
        chapter = _get_chapter_reference(methodology)
        if chapter:
            lines.append(f"  Reference: {chapter}")
        if wooldridge.get("wooldridge_perspective"):
            first = wooldridge["wooldridge_perspective"][0]
            context = first.get("context", "")[:150]
            lines.append(f"  Key point: {context}...")
    else:
        lines.append("  See Wooldridge corpus for details")
    
    # Hansen
    lines.append("\n**Hansen:**")
    if hansen:
        if hansen.get("file"):
            lines.append(f"  See: {hansen['file']}")
        if hansen.get("mentions"):
            lines.append(f"  Mentions: {len(hansen['mentions'])}")
            # Show first mention
            first_mention = hansen["mentions"][0]
            if first_mention.get("content"):
                content = first_mention["content"][:100]
                lines.append(f"  Example: {content}...")
    else:
        lines.append("  See HANSEN_EVALUATION.md")
    
    # Angrist
    lines.append("\n**Angrist/MHE:**")
    if angrist:
        if angrist.get("file"):
            lines.append(f"  See: {angrist['file']}")
        if angrist.get("mentions"):
            lines.append(f"  Mentions: {len(angrist['mentions'])}")
    else:
        lines.append("  See ANGRIST_EVALUATION.md")
    
    # Synthesis
    lines.append(f"\n**Our Synthesis:**")
    lines.append(synthesis)
    
    # Agent rules
    agent_rules = comparison.get("agent_rules", [])
    if agent_rules:
        lines.append("\n**Agent Rules:**")
        for rule in agent_rules:
            lines.append(f"  - {rule}")
    
    return "\n".join(lines)


def format_methodology_guidance(
    methodology: str, sources: Dict[str, Any]
) -> str:
    """Format comprehensive methodology guidance from all sources.
    
    Args:
        methodology: Methodology name
        sources: Dictionary with wooldridge, hansen, angrist perspectives
        
    Returns:
        Formatted guidance string
    """
    lines = [f"**Comprehensive Guidance: {methodology}**\n"]
    
    wooldridge = sources.get("wooldridge", {})
    hansen = sources.get("hansen")
    angrist = sources.get("angrist")
    
    # Wooldridge section
    if wooldridge:
        lines.append("**Wooldridge's Approach:**")
        wooldridge_perspective = wooldridge.get("wooldridge_perspective", [])
        if wooldridge_perspective:
            for persp in wooldridge_perspective[:2]:
                context = persp.get("context", "")[:200]
                lines.append(f"  - {context}...")
        else:
            sections = wooldridge.get("sections", [])
            if sections:
                lines.append(f"  Found {len(sections)} relevant sections")
                chapter = _get_chapter_reference(methodology)
                if chapter:
                    lines.append(f"  Reference: {chapter}")
    
    # Hansen section
    if hansen:
        lines.append("\n**Hansen's Approach:**")
        if isinstance(hansen, dict):
            if hansen.get("file"):
                lines.append(f"  See: {hansen['file']}")
            if hansen.get("mentions"):
                lines.append(f"  Key points found in evaluation document")
        else:
            lines.append(f"  {hansen}")
    
    # Angrist section
    if angrist:
        lines.append("\n**Angrist/MHE Approach:**")
        if isinstance(angrist, dict):
            if angrist.get("file"):
                lines.append(f"  See: {angrist['file']}")
            if angrist.get("mentions"):
                lines.append(f"  Key points found in evaluation document")
        else:
            lines.append(f"  {angrist}")
    
    # Synthesis
    synthesis = sources.get("synthesis")
    if synthesis:
        lines.append("\n**Synthesis:**")
        lines.append(synthesis)
    
    return "\n".join(lines)


def format_quick_reference(methodology: str, perspective: Dict[str, Any]) -> str:
    """Format quick reference for methodology.
    
    Args:
        methodology: Methodology name
        perspective: Perspective dictionary
        
    Returns:
        Quick reference string
    """
    chapter = _get_chapter_reference(methodology)
    sections = perspective.get("sections", [])
    wooldridge_perspective = perspective.get("wooldridge_perspective", [])
    
    lines = [f"**{methodology}**"]
    
    if chapter:
        lines.append(f"Wooldridge: {chapter}")
    
    if wooldridge_perspective:
        first = wooldridge_perspective[0]
        context = first.get("context", "")[:100]
        lines.append(f"Key point: {context}...")
    
    if sections:
        lines.append(f"Found in {len(sections)} sections")
    
    return " | ".join(lines)


def format_search_results(results: List[Dict[str, Any]], query: str) -> str:
    """Format semantic search results for agent response.
    
    Args:
        results: List of search result dictionaries
        query: Original search query
        
    Returns:
        Formatted search results string
    """
    if not results:
        return f"No results found for '{query}' in Wooldridge corpus."
    
    lines = [f"**Wooldridge Corpus Search: '{query}'**\n"]
    lines.append(f"Found {len(results)} results:\n")
    
    for i, result in enumerate(results, 1):
        relevance = result.get("relevance_score", 0)
        metadata = result.get("metadata", {})
        content = result.get("content", "")
        
        lines.append(f"**Result {i}** (relevance: {relevance:.3f}):")
        lines.append(f"  File: {metadata.get('file_name', 'N/A')}")
        
        if metadata.get("section_title"):
            lines.append(f"  Section: {metadata['section_title']}")
        
        if metadata.get("page"):
            lines.append(f"  Page: {metadata['page']}")
        
        if content:
            preview = content[:250].strip()
            if len(content) > 250:
                preview += "..."
            lines.append(f"  Content: {preview}")
        
        lines.append("")  # Blank line between results
    
    return "\n".join(lines)


def _get_chapter_reference(methodology: str) -> Optional[str]:
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



