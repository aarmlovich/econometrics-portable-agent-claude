"""Agent integration layer for querying Wooldridge corpus."""

from pathlib import Path
from typing import Dict, List, Optional, Any
from src.corpus.wooldridge_retriever import WooldridgeRetriever

# Global retriever instance (lazy-loaded)
_retriever: Optional[WooldridgeRetriever] = None


def _get_retriever() -> WooldridgeRetriever:
    """Get or create global retriever instance."""
    global _retriever
    if _retriever is None:
        _retriever = WooldridgeRetriever()
    return _retriever


def get_wooldridge_perspective(methodology: str) -> Dict[str, Any]:
    """Get Wooldridge's perspective on a methodology.
    
    Args:
        methodology: Name of methodology (e.g., "fixed effects", "clustered standard errors")
        
    Returns:
        Dictionary with:
            - methodology: Methodology name
            - wooldridge_perspective: List of perspectives/recommendations
            - sections: List of relevant sections
            - cross_references: Cross-references to evaluations
    """
    retriever = _get_retriever()
    return retriever.find_perspective(methodology)


def triangulate_methodology(methodology: str) -> Dict[str, Any]:
    """Compare Wooldridge, Hansen, and Angrist perspectives on a methodology.
    
    Args:
        methodology: Name of methodology
        
    Returns:
        Dictionary with:
            - methodology: Methodology name
            - wooldridge: Wooldridge's perspective
            - hansen: Hansen's perspective (from evaluation doc)
            - angrist: Angrist's perspective (from evaluation doc)
            - agreement_level: "high", "medium", or "low"
            - synthesis: Recommended approach
    """
    retriever = _get_retriever()
    return retriever.cross_reference(methodology)


def format_perspective_response(perspective: Dict[str, Any]) -> str:
    """Format perspective dictionary into readable text for agent.
    
    Args:
        perspective: Perspective dictionary from get_wooldridge_perspective()
        
    Returns:
        Formatted string for agent response
    """
    methodology = perspective.get("methodology", "Unknown")
    sections = perspective.get("sections", [])
    wooldridge_perspective = perspective.get("wooldridge_perspective", [])
    
    lines = [f"**Wooldridge's Perspective on {methodology}:**"]
    
    if wooldridge_perspective:
        lines.append("\n**Recommendations:**")
        for i, persp in enumerate(wooldridge_perspective[:3], 1):
            context = persp.get("context", "")[:200]
            section = persp.get("section", "N/A")
            page = persp.get("page", "")
            lines.append(f"{i}. {context}...")
            if section != "N/A":
                lines.append(f"   Section: {section}")
            if page:
                lines.append(f"   Page: {page}")
    
    if sections:
        lines.append(f"\n**Found {len(sections)} relevant sections:**")
        for section in sections[:5]:
            file_name = section.get("file_name", "N/A")
            section_title = section.get("section", "N/A")
            page = section.get("page", "")
            lines.append(f"- {file_name}: {section_title}")
            if page:
                lines.append(f"  Page: {page}")
    
    cross_refs = perspective.get("cross_references", {})
    if cross_refs:
        lines.append("\n**Cross-References:**")
        if cross_refs.get("hansen_evaluation"):
            lines.append(f"- Hansen: {cross_refs['hansen_evaluation'].get('file', 'N/A')}")
        if cross_refs.get("angrist_evaluation"):
            lines.append(f"- Angrist: {cross_refs['angrist_evaluation'].get('file', 'N/A')}")
        if cross_refs.get("agent_rules"):
            lines.append(f"- Agent Rules: {', '.join(cross_refs['agent_rules'])}")
    
    return "\n".join(lines)


def should_reference_wooldridge(context: str) -> bool:
    """Determine if Wooldridge should be referenced based on context.
    
    Args:
        context: Context string (user question, methodology name, etc.)
        
    Returns:
        True if Wooldridge should be referenced
    """
    context_lower = context.lower()
    
    # Always reference for panel data
    panel_keywords = [
        "panel data", "fixed effects", "random effects", "within transformation",
        "clustered standard errors", "attrition", "survey weights",
        "entity effects", "time effects", "first-difference"
    ]
    
    # Reference for standard errors in specific contexts
    se_keywords = [
        "hc3", "hac", "small-sample correction", "limited dependent variable"
    ]
    
    # Reference for treatment effects in panel context
    treatment_keywords = [
        "panel treatment effects", "two-way fe did"
    ]
    
    all_keywords = panel_keywords + se_keywords + treatment_keywords
    
    return any(keyword in context_lower for keyword in all_keywords)


def semantic_search_wooldridge(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """Perform semantic search in Wooldridge corpus.
    
    Args:
        query: Search query
        top_k: Number of results to return
        
    Returns:
        List of result dictionaries with content and metadata
    """
    retriever = _get_retriever()
    return retriever.semantic_search(query, top_k=top_k)


def lookup_topic_wooldridge(topic: str) -> Dict[str, Any]:
    """Lookup topic in Wooldridge corpus.
    
    Args:
        topic: Topic name (methodology, category, or priority area)
        
    Returns:
        Dictionary with topic information
    """
    retriever = _get_retriever()
    return retriever.lookup_topic(topic)


def get_methodology_guidance(methodology: str, include_triangulation: bool = True) -> Dict[str, Any]:
    """Get comprehensive guidance on a methodology.
    
    Args:
        methodology: Methodology name
        include_triangulation: Whether to include triangulation with Hansen/Angrist
        
    Returns:
        Dictionary with comprehensive guidance:
            - wooldridge: Wooldridge's perspective
            - triangulation: Triangulation results (if requested)
            - formatted_response: Formatted text for agent
    """
    wooldridge = get_wooldridge_perspective(methodology)
    
    result = {
        "methodology": methodology,
        "wooldridge": wooldridge,
        "formatted_response": format_perspective_response(wooldridge),
    }
    
    if include_triangulation:
        triangulation = triangulate_methodology(methodology)
        result["triangulation"] = triangulation
    
    return result


class AgentIntegration:
    """Wrapper class for agent integration functions."""
    
    def __init__(self, project_root: Optional[Path] = None):
        """Initialize agent integration.
        
        Args:
            project_root: Path to project root directory
        """
        self.project_root = project_root
        self._retriever = None
    
    def get_wooldridge_perspective(self, methodology: str) -> Dict[str, Any]:
        """Get Wooldridge's perspective on a methodology."""
        return get_wooldridge_perspective(methodology)
    
    def semantic_search_wooldridge(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Perform semantic search in Wooldridge corpus."""
        return semantic_search_wooldridge(query, top_k)
    
    def lookup_wooldridge_topic(self, topic: str) -> Dict[str, Any]:
        """Lookup topic in Wooldridge corpus."""
        return lookup_topic_wooldridge(topic)

