"""Interactive question flow for methodology selection."""

from typing import Dict, Any, Optional
import pandas as pd

from .methodology_selection import (
    analyze_data_structure,
    classify_research_question,
    recommend_methods
)
from .explanations import get_explanation, _GLOBAL_EXPLANATION_MODE


def conduct_methodology_selection(
    data: Optional[pd.DataFrame] = None,
    research_question: Optional[str] = None
) -> Dict[str, Any]:
    """Conduct interactive methodology selection process.
    
    This function provides a structured framework for methodology selection.
    In Cursor chat, the agent would use this logic to guide the conversation.
    
    Args:
        data: Optional DataFrame to analyze for data structure
        research_question: Optional research question text
        
    Returns:
        Dictionary containing:
            - data_structure: Output from analyze_data_structure()
            - research_question_classification: Output from classify_research_question()
            - recommendations: List of recommended methods from recommend_methods()
            - suggested_next_steps: Suggested next steps for user
            - questions_to_ask: List of questions to ask user for clarification
    """
    result = {
        'data_structure': None,
        'research_question_classification': None,
        'recommendations': [],
        'suggested_next_steps': [],
        'questions_to_ask': []
    }
    
    # Analyze data structure if data provided
    if data is not None:
        result['data_structure'] = analyze_data_structure(data)
    else:
        result['data_structure'] = {
            'is_panel': None,
            'entity_col': None,
            'time_col': None,
            'has_treatment': None,
            'has_running': None,
            'has_instruments': None
        }
    
    # Classify research question if provided
    if research_question is not None:
        result['research_question_classification'] = classify_research_question(research_question)
    else:
        result['research_question_classification'] = {
            'question_type': 'unclear',
            'has_treatment': None,
            'has_time_variation': None,
            'suggested_methods': []
        }
    
    # Generate recommendations
    if result['data_structure'] and result['research_question_classification']:
        result['recommendations'] = recommend_methods(
            result['data_structure'],
            result['research_question_classification']
        )
    else:
        result['recommendations'] = []
    
    # Generate questions to ask user
    questions = []
    
    if research_question is None:
        questions.append("What is your research question? What are you trying to estimate?")
    
    if data is None:
        questions.append("What data do you have? Is it panel data (multiple observations per unit over time) or cross-sectional?")
    else:
        data_struct = result['data_structure']
        if data_struct.get('is_panel') is None or not data_struct.get('is_panel'):
            questions.append("Is your data panel data (multiple observations per unit over time)?")
        
        if not data_struct.get('has_treatment'):
            questions.append("Do you have a treatment or intervention variable?")
        
        if not data_struct.get('has_running') and result['research_question_classification'].get('question_type') == 'causal':
            questions.append("Do you have a running variable (e.g., test score, age) that determines treatment eligibility?")
        
        if not data_struct.get('has_instruments') and result['research_question_classification'].get('question_type') == 'causal':
            questions.append("Do you have potential instruments (variables that affect treatment but not outcome directly)?")
    
    result['questions_to_ask'] = questions
    
    # Generate suggested next steps
    next_steps = []
    
    if result['recommendations']:
        top_method = result['recommendations'][0]
        next_steps.append(f"Consider using {top_method['method'].upper()} method (confidence: {top_method['confidence']})")
        next_steps.append(f"Review the rationale: {top_method['rationale']}")
        
        if top_method['required_variables']:
            next_steps.append(f"Ensure you have these variables: {', '.join(top_method['required_variables'])}")
    
    if data is None:
        next_steps.append("Load your data and run data structure analysis")
    
    if research_question is None:
        next_steps.append("Clarify your research question to get more targeted recommendations")
    
    result['suggested_next_steps'] = next_steps
    
    return result


__all__ = ['conduct_methodology_selection']

