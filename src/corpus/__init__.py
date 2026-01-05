"""Corpus tools for accessing econometrics textbook content.

Simplified interface: Agent reads textbook files directly.
This module provides page citation utilities for Wooldridge.

Textbook locations:
- Wooldridge: docs/wooldridge_panel/
- Angrist/MHE: docs/angrist_mhe/
- Hansen practices: docs/hansen_practices/
"""

from src.corpus.wooldridge_page_index import (
    METHODOLOGY_PAGES,
    DIAGNOSTIC_THRESHOLDS,
    get_wooldridge_citation,
    get_page_range,
    get_diagnostic_threshold,
    list_topics,
)
from src.corpus.utils import get_default_paths

__all__ = [
    # Page index
    "METHODOLOGY_PAGES",
    "DIAGNOSTIC_THRESHOLDS",
    "get_wooldridge_citation",
    "get_page_range",
    "get_diagnostic_threshold",
    "list_topics",
    # Utilities
    "get_default_paths",
]
