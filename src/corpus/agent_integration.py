"""Agent integration layer for querying Wooldridge corpus."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from src.corpus.wooldridge_search import WooldridgeSearch
from src.corpus.utils import get_default_paths

# Global search instance (lazy-loaded)
_searcher: Optional[WooldridgeSearch] = None


def _get_searcher() -> WooldridgeSearch:
    """Get or create global search instance."""
    global _searcher
    if _searcher is None:
        _searcher = WooldridgeSearch()
    return _searcher


def _load_index_data(project_root: Optional[Path] = None) -> Dict:
    """Load index and cross-reference data if available."""
    paths = get_default_paths(project_root)
    data = {
        'index': None,
        'cross_refs': None,
    }

    if paths["index_file"].exists():
        with open(paths["index_file"], 'r', encoding='utf-8') as f:
            data['index'] = json.load(f)

    if paths["cross_refs_file"].exists():
        with open(paths["cross_refs_file"], 'r', encoding='utf-8') as f:
            data['cross_refs'] = json.load(f)

    return data


def get_wooldridge_perspective(methodology: str) -> Dict[str, Any]:
    """Get Wooldridge's perspective on a methodology.

    Args:
        methodology: Name of methodology (e.g., "fixed effects", "clustered standard errors")

    Returns:
        Dictionary with:
            - methodology: Methodology name
            - guidance: Methodology-specific guidance text
            - sections: List of relevant sections from search
            - cross_references: Cross-references to evaluations (if available)
    """
    searcher = _get_searcher()
    index_data = _load_index_data()

    # Get guidance via search
    guidance = searcher.get_methodology_guidance(methodology)

    # Get search results as sections
    results = searcher.search_wooldridge(methodology, top_k=5)

    # Format as sections
    sections = [
        {
            'title': r['title'],
            'file_name': r['file_name'],
            'content': r['content'],
        }
        for r in results
    ]

    result = {
        'methodology': methodology,
        'guidance': guidance,
        'sections': sections,
        'cross_references': {},
    }

    # Add cross-references if available
    if index_data['cross_refs'] and methodology in index_data['cross_refs']:
        result['cross_references'] = index_data['cross_refs'][methodology]

    return result


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
            - agent_rules: List of agent rules (if available)
    """
    index_data = _load_index_data()

    # Get Wooldridge perspective
    wooldridge = get_wooldridge_perspective(methodology)

    result = {
        'methodology': methodology,
        'wooldridge': wooldridge,
        'hansen': None,
        'angrist': None,
        'agent_rules': [],
    }

    # Add cross-reference data if available
    if index_data['cross_refs'] and methodology in index_data['cross_refs']:
        cross_ref = index_data['cross_refs'][methodology]

        if cross_ref.get('hansen_evaluation'):
            result['hansen'] = cross_ref['hansen_evaluation']

        if cross_ref.get('angrist_evaluation'):
            result['angrist'] = cross_ref['angrist_evaluation']

        if cross_ref.get('agent_rules'):
            result['agent_rules'] = cross_ref['agent_rules']

    return result


def format_perspective_response(perspective: Dict[str, Any]) -> str:
    """Format perspective dictionary into readable text for agent.

    Args:
        perspective: Perspective dictionary from get_wooldridge_perspective()

    Returns:
        Formatted string for agent response
    """
    methodology = perspective.get("methodology", "Unknown")
    sections = perspective.get("sections", [])
    guidance = perspective.get("guidance", "")

    lines = [f"**Wooldridge's Perspective on {methodology}:**"]

    if guidance:
        lines.append("\n**Guidance:**")
        lines.append(guidance)

    if sections:
        lines.append(f"\n**Found {len(sections)} relevant sections:**")
        for section in sections[:5]:
            file_name = section.get("file_name", "N/A")
            section_title = section.get("title", "N/A")
            lines.append(f"- {file_name}: {section_title}")

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
    """Perform keyword search in Wooldridge corpus.

    Args:
        query: Search query
        top_k: Number of results to return

    Returns:
        List of result dictionaries with content and metadata
    """
    searcher = _get_searcher()
    return searcher.search_wooldridge(query, top_k=top_k)


def lookup_topic_wooldridge(topic: str) -> Dict[str, Any]:
    """Lookup topic in Wooldridge corpus.

    Args:
        topic: Topic name (methodology, category, or priority area)

    Returns:
        Dictionary with topic information
    """
    searcher = _get_searcher()
    index_data = _load_index_data()

    # Get chapter content
    chapter_content = searcher.get_chapter(topic)

    # Search for related sections
    results = searcher.search_wooldridge(topic, top_k=5)

    result = {
        'topic': topic,
        'chapter_content': chapter_content,
        'sections': results,
    }

    # Add index data if available
    if index_data['index']:
        topic_lower = topic.lower()
        if topic_lower in index_data['index'].get('by_methodology', {}):
            result['methodologies'] = index_data['index']['by_methodology'][topic_lower]
        if topic_lower in index_data['index'].get('by_topic', {}):
            result['topic_sections'] = index_data['index']['by_topic'][topic_lower]

    return result


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
        self._searcher = None

    def get_wooldridge_perspective(self, methodology: str) -> Dict[str, Any]:
        """Get Wooldridge's perspective on a methodology."""
        return get_wooldridge_perspective(methodology)

    def semantic_search_wooldridge(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Perform keyword search in Wooldridge corpus."""
        return semantic_search_wooldridge(query, top_k)

    def lookup_wooldridge_topic(self, topic: str) -> Dict[str, Any]:
        """Lookup topic in Wooldridge corpus."""
        return lookup_topic_wooldridge(topic)

