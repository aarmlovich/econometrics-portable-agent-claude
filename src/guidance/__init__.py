"""Guidance system for methodology selection and explanations."""

from .methodology_selection import (
    analyze_data_structure,
    classify_research_question,
    recommend_methods
)
from .explanations import (
    get_explanation,
    toggle_explanation_mode
)
from .question_flow import conduct_methodology_selection

__all__ = [
    'analyze_data_structure',
    'classify_research_question',
    'recommend_methods',
    'get_explanation',
    'toggle_explanation_mode',
    'conduct_methodology_selection'
]

