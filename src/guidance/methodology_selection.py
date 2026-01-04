"""Methodology selection logic based on data structure and research question."""

from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
import warnings
import re


def analyze_data_structure(data: pd.DataFrame) -> Dict[str, Any]:
    """Analyze data structure to detect panel structure and key variables.
    
    Args:
        data: DataFrame to analyze
        
    Returns:
        Dictionary containing:
            - is_panel: Whether data appears to be panel data
            - entity_col: Detected entity identifier column (if any)
            - time_col: Detected time identifier column (if any)
            - has_treatment: Whether treatment-like variables detected
            - has_running: Whether running variable-like variables detected
            - has_instruments: Whether instrument-like variables detected
            - time_varying_vars: List of time-varying variables (if panel)
            - time_invariant_vars: List of time-invariant variables (if panel)
            - n_entities: Number of entities (if panel)
            - n_periods: Number of time periods (if panel)
            - suggested_entity_col: Suggested entity column name
            - suggested_time_col: Suggested time column name
    """
    result = {
        'is_panel': False,
        'entity_col': None,
        'time_col': None,
        'has_treatment': False,
        'has_running': False,
        'has_instruments': False,
        'time_varying_vars': [],
        'time_invariant_vars': [],
        'n_entities': None,
        'n_periods': None,
        'suggested_entity_col': None,
        'suggested_time_col': None
    }
    
    cols = data.columns.tolist()
    
    # Common entity identifier names (using word boundaries to prevent false positives)
    # Word boundaries (\b) prevent matching 'valid', 'android', 'identify', etc.
    entity_keywords = [r'\bid\b', r'\bentity\b', r'\bunit\b',
                      r'\bfirm\b', r'\bindividual\b', r'\bperson\b',
                      r'\bstate\b', r'\bcountry\b', r'\bcounty\b',
                      r'\bschool\b', r'\bstore\b', r'\bplant\b',
                      r'\bcompany\b']
    time_keywords = [r'\btime\b', r'\byear\b', r'\bperiod\b',
                    r'\bdate\b', r'\bmonth\b', r'\bquarter\b',
                    r'\bweek\b', r'\bday\b']

    # Look for entity identifier
    for col in cols:
        col_lower = col.lower()
        if any(re.search(keyword, col_lower) for keyword in entity_keywords):
            # Check if this looks like an identifier (many unique values, or repeated values)
            n_unique = data[col].nunique()
            if n_unique < len(data) * 0.9:  # Not too many unique values (likely an ID)
                result['suggested_entity_col'] = col
                if n_unique < len(data) / 2:  # Definitely panel-like
                    result['entity_col'] = col
                    result['is_panel'] = True
                break
    
    # Look for time identifier
    for col in cols:
        col_lower = col.lower()
        if any(re.search(keyword, col_lower) for keyword in time_keywords):
            # Check if numeric or datetime
            if pd.api.types.is_numeric_dtype(data[col]) or pd.api.types.is_datetime64_any_dtype(data[col]):
                result['suggested_time_col'] = col
                if result['entity_col']:
                    result['time_col'] = col
                    result['is_panel'] = True
                break
    
    # If we have both entity and time, analyze panel structure
    if result['entity_col'] and result['time_col']:
        entity_col = result['entity_col']
        time_col = result['time_col']
        
        # Count entities and periods
        result['n_entities'] = data[entity_col].nunique()
        result['n_periods'] = data[time_col].nunique()
        
        # Identify time-varying vs time-invariant variables
        # A variable is time-invariant if it's constant within each entity
        for col in cols:
            if col in [entity_col, time_col]:
                continue
            if data[col].dtype in ['object', 'category']:
                continue  # Skip categorical for now
            
            # Check if constant within entities
            entity_groups = data.groupby(entity_col)[col]
            n_varying = entity_groups.nunique().gt(1).sum()
            if n_varying == 0:
                result['time_invariant_vars'].append(col)
            else:
                result['time_varying_vars'].append(col)
    
    # Look for treatment-like variables (binary 0/1 variables)
    treatment_keywords = [r'\btreat\b', r'\btreatment\b', r'\bd\b',
                         r'\bdummy\b', r'\bindicator\b']
    for col in cols:
        if data[col].dtype in ['int64', 'float64']:
            unique_vals = data[col].dropna().unique()
            if len(unique_vals) == 2 and set(unique_vals).issubset({0, 1}):
                # Check if name suggests treatment
                col_lower = col.lower()
                if any(re.search(keyword, col_lower) for keyword in treatment_keywords):
                    result['has_treatment'] = True
                    break
    
    # Look for running variable-like variables (continuous, many unique values)
    running_keywords = [r'\bscore\b', r'\brunning\b', r'\bindex\b',
                       r'\bdistance\b', r'\bage\b']
    for col in cols:
        if pd.api.types.is_numeric_dtype(data[col]) and data[col].dtype != 'bool':
            n_unique = data[col].nunique()
            if n_unique > len(data) * 0.1:  # Many unique values
                col_lower = col.lower()
                if any(re.search(keyword, col_lower) for keyword in running_keywords):
                    result['has_running'] = True
                    break
    
    # Look for instrument-like variables (would need domain knowledge, just check for common patterns)
    # This is heuristic - real instruments need economic reasoning
    instrument_keywords = [r'\binstrument\b', r'\biv\b', r'\bz\b',
                          r'\bexcluded\b']
    for col in cols:
        col_lower = col.lower()
        if any(re.search(keyword, col_lower) for keyword in instrument_keywords):
            result['has_instruments'] = True
            break
    
    return result


def classify_research_question(question: str) -> Dict[str, Any]:
    """Classify research question to determine appropriate methods.
    
    Args:
        question: Research question text
        
    Returns:
        Dictionary containing:
            - question_type: 'causal', 'descriptive', 'predictive', 'unclear'
            - has_treatment: Whether question mentions treatment/intervention
            - has_time_variation: Whether question mentions time/temporal variation
            - keywords: Detected keywords
            - suggested_methods: List of suggested methods based on keywords
    """
    question_lower = question.lower()
    
    result = {
        'question_type': 'unclear',
        'has_treatment': False,
        'has_time_variation': False,
        'keywords': [],
        'suggested_methods': []
    }
    
    # Causal inference keywords (using word boundaries for precise matching)
    causal_keywords = [r'\beffect\b', r'\bimpact\b', r'\bcausal\b', r'\btreatment\b',
                      r'\bintervention\b', r'\bpolicy\b', r'\bcause\b', r'\binfluence\b',
                      r'\battributable\b', r'\bdue to\b', r'\bresult of\b']
    treatment_keywords = [r'\btreatment\b', r'\bintervention\b', r'\bpolicy\b',
                         r'\bprogram\b', r'\breform\b']
    time_keywords = [r'\bbefore\b', r'\bafter\b', r'\bchange\b', r'\bover time\b',
                    r'\btrend\b', r'\bperiod\b']

    # Check for causal language
    if any(re.search(keyword, question_lower) for keyword in causal_keywords):
        result['question_type'] = 'causal'
        result['keywords'].extend([k.strip(r'\b') for k in causal_keywords
                                  if re.search(k, question_lower)])

    # Check for treatment/intervention
    if any(re.search(keyword, question_lower) for keyword in treatment_keywords):
        result['has_treatment'] = True
        result['keywords'].extend([k.strip(r'\b') for k in treatment_keywords
                                  if re.search(k, question_lower)])

    # Check for time variation
    if any(re.search(keyword, question_lower) for keyword in time_keywords):
        result['has_time_variation'] = True
        result['keywords'].extend([k.strip(r'\b') for k in time_keywords
                                  if re.search(k, question_lower)])

    # Descriptive/predictive keywords
    descriptive_keywords = [r'\bdescribe\b', r'\bsummarize\b', r'\bdistribution\b',
                           r'\bpattern\b', r'\bcorrelation\b']
    predictive_keywords = [r'\bpredict\b', r'\bforecast\b', r'\boutcome\b', r'\bprobability\b']

    if any(re.search(keyword, question_lower) for keyword in descriptive_keywords):
        if result['question_type'] == 'unclear':
            result['question_type'] = 'descriptive'
    elif any(re.search(keyword, question_lower) for keyword in predictive_keywords):
        if result['question_type'] == 'unclear':
            result['question_type'] = 'predictive'
    
    # Suggest methods based on classification
    if result['question_type'] == 'causal':
        if result['has_treatment']:
            if result['has_time_variation']:
                result['suggested_methods'].append('did')
            result['suggested_methods'].extend(['matching', 'iv', 'rd'])
        else:
            result['suggested_methods'].append('ols')
    elif result['question_type'] == 'descriptive':
        result['suggested_methods'].append('ols')
    elif result['question_type'] == 'predictive':
        result['suggested_methods'].append('ols')
    
    return result


def recommend_methods(
    data_structure: Dict[str, Any],
    research_question: Dict[str, Any],
    available_variables: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """Recommend econometric methods based on data structure and research question.
    
    Args:
        data_structure: Output from analyze_data_structure()
        research_question: Output from classify_research_question()
        available_variables: Optional list of available variable names
        
    Returns:
        List of recommendation dictionaries, each containing:
            - method: Method name (e.g., 'did', 'iv', 'ols')
            - confidence: Confidence level ('high', 'medium', 'low')
            - rationale: Explanation for recommendation
            - required_variables: List of required variable types
            - suitability_score: Numerical score (0-1) for suitability
    """
    recommendations = []
    
    question_type = research_question.get('question_type', 'unclear')
    has_treatment = research_question.get('has_treatment', False)
    has_time_variation = research_question.get('has_time_variation', False)
    
    is_panel = data_structure.get('is_panel', False)
    has_treatment_var = data_structure.get('has_treatment', False)
    has_running_var = data_structure.get('has_running', False)
    has_instruments_var = data_structure.get('has_instruments', False)
    
    # Decision tree for method recommendation
    
    # 1. Difference-in-Differences
    if question_type == 'causal' and has_treatment and is_panel and has_time_variation:
        recommendations.append({
            'method': 'did',
            'confidence': 'high',
            'rationale': 'Causal question with treatment and panel data structure - ideal for DiD',
            'required_variables': ['outcome', 'treatment', 'entity', 'time'],
            'suitability_score': 0.9
        })
    
    # 2. Fixed Effects (panel)
    if is_panel and question_type in ['causal', 'descriptive']:
        recommendations.append({
            'method': 'fe',
            'confidence': 'high' if is_panel else 'medium',
            'rationale': 'Panel data structure - fixed effects control for unobserved heterogeneity',
            'required_variables': ['outcome', 'covariates', 'entity', 'time'],
            'suitability_score': 0.8 if is_panel else 0.5
        })
    
    # 3. Regression Discontinuity
    if question_type == 'causal' and has_running_var:
        recommendations.append({
            'method': 'rd',
            'confidence': 'high' if has_running_var else 'medium',
            'rationale': 'Causal question with running variable - suitable for RD design',
            'required_variables': ['outcome', 'running', 'cutoff'],
            'suitability_score': 0.85 if has_running_var else 0.6
        })
    
    # 4. Instrumental Variables
    if question_type == 'causal' and has_instruments_var:
        recommendations.append({
            'method': 'iv',
            'confidence': 'medium',
            'rationale': 'Causal question with potential instruments - IV can address endogeneity',
            'required_variables': ['outcome', 'treatment', 'instruments'],
            'suitability_score': 0.7
        })
    
    # 5. Matching
    if question_type == 'causal' and has_treatment:
        recommendations.append({
            'method': 'matching',
            'confidence': 'medium',
            'rationale': 'Causal question with treatment - matching can balance observables',
            'required_variables': ['outcome', 'treatment', 'covariates'],
            'suitability_score': 0.65
        })
    
    # 6. Panel IV
    if question_type == 'causal' and is_panel and has_instruments_var:
        recommendations.append({
            'method': 'panel_iv',
            'confidence': 'medium',
            'rationale': 'Panel data with instruments - panel IV combines FE with IV',
            'required_variables': ['outcome', 'treatment', 'instruments', 'entity', 'time'],
            'suitability_score': 0.75
        })
    
    # 7. Random Effects (panel)
    if is_panel:
        recommendations.append({
            'method': 're',
            'confidence': 'medium',
            'rationale': 'Panel data structure - random effects if unobserved heterogeneity is uncorrelated with regressors',
            'required_variables': ['outcome', 'covariates', 'entity', 'time'],
            'suitability_score': 0.6
        })
    
    # 8. OLS (fallback/default)
    recommendations.append({
        'method': 'ols',
        'confidence': 'low' if question_type == 'causal' else 'high',
        'rationale': 'Basic regression method - use when no specific identification strategy applies',
        'required_variables': ['outcome', 'covariates'],
        'suitability_score': 0.4 if question_type == 'causal' else 0.7
    })
    
    # Sort by suitability score (highest first)
    recommendations.sort(key=lambda x: x['suitability_score'], reverse=True)
    
    return recommendations


__all__ = ['analyze_data_structure', 'classify_research_question', 'recommend_methods']

