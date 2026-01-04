"""Corpus tools for analyzing and retrieving Wooldridge textbook content.

Includes page-indexed textbook search, topic mappings, and query interface.
Reference: Wooldridge, J.M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
"""

from src.corpus.wooldridge_analyzer import WooldridgeAnalyzer
from src.corpus.wooldridge_index import WooldridgeIndexer
from src.corpus.wooldridge_search import WooldridgeSearch, search_wooldridge, get_chapter, get_methodology_guidance
from src.corpus.wooldridge_page_index import (
    METHODOLOGY_PAGES,
    DIAGNOSTIC_THRESHOLDS,
    get_wooldridge_citation as get_page_citation,
    get_page_range,
    get_diagnostic_threshold,
    list_topics,
)
from src.corpus.ask_wooldridge import (
    ask_wooldridge,
    get_methodology_recommendation,
    list_available_topics,
    WOOLDRIDGE_GUIDANCE,
)
from src.corpus.agent_integration import (
    get_wooldridge_perspective,
    triangulate_methodology,
    format_perspective_response,
    semantic_search_wooldridge,
    lookup_topic_wooldridge,
    get_methodology_guidance as get_methodology_guidance_full,
)
from src.corpus.agent_helpers import (
    quick_lookup,
    get_standard_error_guidance,
    get_panel_data_guidance,
    compare_approaches,
    search_wooldridge_content,
    get_chapter_reference,
)
from src.corpus.triangulation import (
    triangulate,
    compare_standard_errors,
    compare_panel_methods,
    synthesize_recommendation,
)
from src.corpus.response_templates import (
    format_wooldridge_citation,
    format_triangulation_response,
    format_methodology_guidance,
    format_quick_reference,
    format_search_results,
)
from src.corpus.validation import Validation
from src.corpus.rule_validator import RuleValidator
from src.corpus.model_validator import ModelValidator
from src.corpus.validation_report import ValidationReport

__all__ = [
    "WooldridgeAnalyzer",
    "WooldridgeIndexer",
    "WooldridgeSearch",
    "search_wooldridge",
    "get_chapter",
    # Page index
    "METHODOLOGY_PAGES",
    "DIAGNOSTIC_THRESHOLDS",
    "get_page_citation",
    "get_page_range",
    "get_diagnostic_threshold",
    "list_topics",
    # Ask Wooldridge
    "ask_wooldridge",
    "get_methodology_recommendation",
    "list_available_topics",
    "WOOLDRIDGE_GUIDANCE",
    # Agent integration
    "get_wooldridge_perspective",
    "triangulate_methodology",
    "format_perspective_response",
    "semantic_search_wooldridge",
    "lookup_topic_wooldridge",
    "get_methodology_guidance",
    "get_methodology_guidance_full",
    # Agent helpers
    "quick_lookup",
    "get_standard_error_guidance",
    "get_panel_data_guidance",
    "compare_approaches",
    "search_wooldridge_content",
    "get_chapter_reference",
    # Triangulation
    "triangulate",
    "compare_standard_errors",
    "compare_panel_methods",
    "synthesize_recommendation",
    # Response templates
    "format_wooldridge_citation",
    "format_triangulation_response",
    "format_methodology_guidance",
    "format_quick_reference",
    "format_search_results",
    # Validation
    "Validation",
    "RuleValidator",
    "ModelValidator",
    "ValidationReport",
]

