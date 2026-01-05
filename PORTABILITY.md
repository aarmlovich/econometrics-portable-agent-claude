# Portability Guide: Using Econometrics Agent in New Cursor Projects

This guide explains how to copy this econometrics agent into a new Cursor project.

## Quick Start

### 1. Copy Required Files

Copy the following directories and files to your new Cursor project:

```
Your New Project/
├── .cursor/
│   └── rules/                   # Cursor agent rules (copy all .mdc files)
│
├── src/
│   ├── guidance/                # Methodology selection system
│   ├── corpus/                  # Simplified corpus tools
│   │   ├── __init__.py
│   │   ├── wooldridge_page_index.py
│   │   └── utils.py
│   ├── models/                  # Econometric models
│   ├── diagnostics/             # Diagnostic tests
│   └── utils/                   # Utility functions
│
├── docs/
│   ├── wooldridge_panel/        # Wooldridge textbook by section
│   ├── angrist_mhe/             # Angrist/MHE by section
│   └── hansen_practices/        # Hansen code practices
│
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

### 2. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Required packages:**
- pandas >= 2.0.0
- numpy >= 1.24.0
- statsmodels >= 0.14.0
- scipy >= 1.10.0
- linearmodels >= 5.0.0
- scikit-learn >= 1.3.0

### 3. Verify Installation

In Cursor chat, try:
```
"Help me choose an econometric method for my analysis"
```

## Textbook Corpus

The agent has access to three textbook sources:

| Source | Path | Focus |
|--------|------|-------|
| Wooldridge | `docs/wooldridge_panel/` | Panel data, standard errors, IV |
| Angrist/MHE | `docs/angrist_mhe/` | Causal inference, DiD, RD, IV |
| Hansen | `docs/hansen_practices/` | Modern code practices |

### File Organization

Each textbook directory contains:
- `_index.md` - Table of contents with page mappings
- Section files named by chapter (e.g., `ch10_3_fixed_effects.md`)
- Page markers `{123}---` preserved for citations

### Using Textbooks

**Find content:**
```bash
# Search for topics
grep -r "fixed effects" docs/wooldridge_panel/

# Read the index
cat docs/wooldridge_panel/_index.md
```

**Get page citations:**
```python
from src.corpus import get_wooldridge_citation

citation = get_wooldridge_citation("fixed_effects")
# Returns: "Wooldridge, Chapter 10, pp. 291-310"
```

## Usage in Cursor Chat

### Methodology Selection

Ask for method recommendations:
```
"I have panel data on firms. I want to estimate the effect of a policy. What method should I use?"
```

### Triangulation

Request comparison across sources:
```
"Compare Hansen, Angrist, and Wooldridge on clustered standard errors"
```

### Specific Guidance

Ask about methodology:
```
"What does Wooldridge say about fixed effects vs random effects?"
"How should I handle weak instruments?"
```

## Key Features

### Methodology Selection System

The guidance system (`src/guidance/`) provides:
- Data structure analysis
- Research question classification
- Method recommendations with confidence levels
- Interactive Q&A flow

### Triangulation Framework

Compare perspectives from:
- **Hansen**: Modern code practices (robust SE, diagnostics)
- **Angrist/MHE**: Identification focus (DiD, RD, IV)
- **Wooldridge**: Panel data expertise (FE, RE, clustered SE)

### Econometric Methods

- **OLS Regression**: Robust standard errors, diagnostics
- **Difference-in-Differences**: Parallel trends tests, event studies
- **Instrumental Variables**: First-stage diagnostics, weak instrument tests
- **Regression Discontinuity**: Bandwidth selection, manipulation tests
- **Matching**: Propensity score matching, balance tests
- **Fixed Effects**: Panel data with clustered standard errors
- **Random Effects**: Hausman test, GLS estimation
- **Panel IV**: Panel data with instrumental variables

## File Structure Summary

### Required for Methodology Selection

- `.cursor/rules/*.mdc` - Cursor agent rules
- `src/guidance/` - Methodology selection system

### Required for Textbook Corpus

- `docs/wooldridge_panel/` - Wooldridge textbook
- `docs/angrist_mhe/` - Angrist/MHE textbook
- `docs/hansen_practices/` - Hansen practices
- `src/corpus/` - Page citation utilities

### Optional

- `src/models/` - Econometric model implementations
- `src/diagnostics/` - Diagnostic tests
- `src/utils/` - Utility functions

## Troubleshooting

### Agent Not Using Rules

1. Check `.cursor/rules/` directory exists with `.mdc` files
2. Restart Cursor to reload rules
3. Verify Python dependencies installed

### Import Errors

1. Activate virtual environment
2. Install requirements: `pip install -r requirements.txt`
3. Verify Python 3.10+ installed

### Textbook Not Found

1. Check `docs/wooldridge_panel/` directory exists
2. Verify `_index.md` file present
3. Use grep to search for content

## Environment Notes

- **Python**: Always use `python3` (not `python`)
- **Virtual environment**: Recommended for isolation
- **Cursor**: Restart to reload rules after changes

---

**Note:** This agent assists with methodology selection and provides explanations. It does not replace domain expertise or careful consideration of your specific research context.
