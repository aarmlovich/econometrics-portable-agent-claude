# Portability Guide: Using Econometrics Agent in New Cursor Projects

This guide explains how to copy this econometrics agent into a new Cursor project to assist with methodology selection and econometric analysis.

## Creating a Portable Package

**Quick Package Creation:**

Use the provided script to create a portable package:

```bash
# Create package (includes all essential files)
python scripts/create_portable_package.py

# Create package with evaluation documents (optional)
python scripts/create_portable_package.py --include-evaluations

# Specify custom output directory
python scripts/create_portable_package.py --output-dir /path/to/output
```

The script creates a `portable_package/` directory with all necessary files. Simply copy the entire contents to your new Cursor project.

**Manual Package Creation:**

Alternatively, follow the file structure below to manually copy files.

## Overview

The Econometrics Agent provides:
- **Methodology Selection**: Interactive guidance for choosing appropriate econometric methods
- **Economic Intuition**: Explanations of coefficient interpretations and causal reasoning
- **Statistical Explanations**: Clear explanations of assumptions, diagnostics, and standard errors
- **Educational Mode**: Toggle between concise (default) and detailed pedagogical explanations
- **Comprehensive Methods**: OLS, DiD, IV, RD, Matching, Fixed Effects, Random Effects, Panel IV

## Quick Start

### 1. Copy Required Files

Copy the following directories and files to your new Cursor project:

```
Your New Project/
├── .cursor/
│   └── rules/
│       ├── methodology-selection.mdc  (methodology guidance)
│       ├── causal-inference.mdc       (causal methods)
│       ├── panel-data.mdc             (panel methods)
│       ├── regression-core.mdc        (OLS and core regression)
│       ├── diagnostics.mdc            (diagnostic tests)
│       ├── data-handling.mdc          (data preparation)
│       ├── reporting.mdc              (reporting standards)
│       ├── visualization.mdc          (plotting standards)
│       ├── project-overview.mdc       (project overview)
│       ├── triangulation-guide.mdc    (perspective triangulation)
│       ├── wooldridge-references.mdc  (Wooldridge corpus reference guide)
│       ├── workflow-best-practices.mdc (recommended - workflow guidelines)
│       ├── code-standards.mdc         (recommended - code style guide)
│       └── [other rule files as needed]
│
├── src/
│   ├── guidance/                      (methodology selection system)
│   │   ├── __init__.py
│   │   ├── methodology_selection.py
│   │   ├── explanations.py
│   │   └── question_flow.py
│   │
│   ├── corpus/                        (Wooldridge corpus system)
│   │   ├── __init__.py
│   │   ├── agent_integration.py
│   │   ├── agent_helpers.py
│   │   ├── triangulation.py
│   │   ├── validation.py
│   │   ├── wooldridge_analyzer.py
│   │   ├── wooldridge_index.py
│   │   ├── wooldridge_embeddings.py
│   │   ├── wooldridge_retriever.py
│   │   └── [other corpus modules]
│   │
│   ├── models/                        (econometric models)
│   │   ├── regression/
│   │   ├── causal/
│   │   └── panel/
│   │
│   ├── diagnostics/                   (diagnostic tests)
│   │   └── joint_tests.py
│   │
│   ├── utils/                         (utility functions)
│   │   ├── comparison_tables.py
│   │   └── summary_stats.py
│   │
│   ├── data/                          (data loading)
│   └── [other modules as needed]
│
├── data/
│   ├── corpus/                        (Wooldridge corpus data - pre-built)
│   │   ├── wooldridge_embeddings/
│   │   │   └── embeddings.json
│   │   └── wooldridge_index/
│   │       ├── index.json
│   │       ├── cross_references.json
│   │       ├── analysis.json
│   │       └── methodology_map.json
│   ├── raw/                           (your data files)
│   ├── processed/
│   └── outputs/
│
├── docs/
│   └── wooldridge_extracts/           (Wooldridge source markdown files - for rebuilding)
│       ├── part1_introduction.md
│       ├── part2_iv_gmm.md
│       ├── part3_systems.md
│       ├── part4_nonlinear.md
│       ├── part5_nonlinear_models.md
│       ├── part6_panel_data.md
│       ├── part7_advanced.md
│       └── [page-level markdown files]
│
├── requirements.txt                   (Python dependencies)
├── setup.py                           (Package setup)
└── README.md                          (project documentation)
```

### 2. Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Required packages:**
- pandas >= 2.0.0
- numpy >= 1.24.0
- statsmodels >= 0.14.0
- scipy >= 1.10.0
- linearmodels >= 5.0.0
- scikit-learn >= 1.3.0
- sentence-transformers >= 2.2.0 (for Wooldridge corpus)

**Note**: The `sentence-transformers` package will download model files (~90 MB) on first use. This is normal and happens automatically.

### 3. Verify Installation

**Verify methodology selection:**
In Cursor chat, try:

```
"Help me choose an econometric method for my analysis"
```

The agent should respond using the methodology selection system.

**Verify Wooldridge corpus:**
Test that the corpus is working:

```python
from src.corpus import WooldridgeRetriever

# Initialize retriever (this loads the corpus)
retriever = WooldridgeRetriever()

# Test semantic search
results = retriever.semantic_search("fixed effects panel data", top_k=3)
print(f"✅ Corpus loaded successfully! Found {len(results)} results.")
```

If the corpus loads without errors, you're ready to go!

## Usage in Cursor Chat

### Getting Started (First Question)

When you first open the project in Cursor, the agent automatically loads:
- Project overview rules (always applied)
- Wooldridge corpus reference guide (always applied)
- Triangulation guide (always applied)

**For your first question, try:**
- "What method should I use for my analysis?"
- "Help me choose an econometric method"
- "I have panel data, what methods are appropriate?"

The agent will automatically use the methodology selection system, even if you haven't created any analysis files yet.

### Methodology Selection

**Ask for method recommendations:**
```
"I have panel data on firms. I want to estimate the effect of a policy. What method should I use?"
```

**Request explanations:**
```
"Why is DiD appropriate here?"
"Explain in more detail"  # Toggles to educational mode
```

**Provide your research question:**
```
"My research question is: What is the effect of treatment X on outcome Y?"
```

### Analysis Assistance

The agent can help with:
- Choosing appropriate methods based on your research question and data
- Understanding economic intuition for coefficients
- Explaining causal identification strategies
- Interpreting diagnostic tests
- Selecting standard error types
- Understanding statistical assumptions

### Wooldridge Corpus Usage

The agent can query Wooldridge's textbook perspective on methodologies:

**Ask about Wooldridge's perspective:**
```
"What does Wooldridge say about clustered standard errors in panel data?"
"How does Wooldridge recommend handling fixed effects?"
```

**Request triangulation (compare all three perspectives):**
```
"Compare Hansen, Angrist, and Wooldridge on fixed effects estimation"
"What's the consensus on panel data standard errors?"
```

**Semantic search:**
The agent can search Wooldridge's textbook for relevant content:
```
"Search Wooldridge for information on attrition in panel data"
"Find Wooldridge's guidance on survey weights"
```

The corpus enables the agent to provide methodology guidance that synthesizes perspectives from Hansen (modern practices), Angrist/MHE (identification focus), and Wooldridge (panel data expertise).

### Explanation Modes

**Default (Basic Mode):**
- Concise, practical explanations
- Quick decision-making guidance

**Educational Mode:**
- Request: "Explain in more detail" or "Use educational explanations"
- Detailed, pedagogical explanations
- Theoretical background and assumptions

## Key Features

### 1. Methodology Selection System

The guidance system (`src/guidance/`) provides:
- Data structure analysis (detects panel structure, treatment variables, etc.)
- Research question classification (causal, descriptive, predictive)
- Method recommendations with confidence levels and rationale
- Interactive Q&A flow

### 2. Explanation System

Comprehensive explanations covering:
- Method selection rationale
- Economic intuition
- Causal identification
- Statistical assumptions
- Standard error choices
- Diagnostic interpretations

### 3. Econometric Methods

Implemented methods:
- **OLS Regression**: Robust standard errors, diagnostics
- **Difference-in-Differences**: Parallel trends tests, event studies
- **Instrumental Variables**: First-stage diagnostics, overidentification tests
- **Regression Discontinuity**: Bandwidth selection, manipulation tests
- **Matching**: Propensity score matching, balance tests
- **Fixed Effects**: Panel data with clustered standard errors
- **Random Effects**: Hausman test, GLS estimation
- **Panel IV**: Panel data with instrumental variables

### 4. Utility Functions

- **Joint Hypothesis Testing**: Test joint significance of multiple coefficients
- **Comparison Tables**: Create side-by-side specification comparison tables
- **Summary Statistics**: Compute summary statistics by group (treatment/control, time periods)

## Example Workflows

### Workflow 1: Methodology Selection for New Analysis

```
User: "I have data on schools. Some received a program in 2020, others didn't. 
       I want to estimate the program's effect on test scores. What method should I use?"

Agent: [Analyzes question, suggests DiD]
       "I recommend Difference-in-Differences (DiD) because you have:
        - Panel data (schools over time)
        - Clear treatment (program in 2020)
        - Variation in treatment (some schools treated, others not)
        
        DiD compares changes in test scores between treated and control schools,
        before and after 2020.
        
        Required variables:
        - Outcome: test scores
        - Treatment: program indicator (school × post-2020)
        - Entity: school ID
        - Time: year
        
        Would you like me to explain the parallel trends assumption?"
```

### Workflow 2: Understanding a Method

```
User: "Why use fixed effects instead of random effects?"

Agent: [Provides explanation using explanation system]
       "Fixed effects (FE) and random effects (RE) differ in their assumptions about 
        unobserved heterogeneity...
        
        [Basic explanation]
        
        Would you like a more detailed explanation of the Hausman test?"
```

### Workflow 3: Data Structure Analysis

```
User: "I have this data file: data.csv. What methods are appropriate?"

Agent: [Loads data, analyzes structure]
       "I analyzed your data structure:
        - Panel data detected (entity: firm_id, time: year)
        - 500 firms, 10 years
        - Treatment variable detected: policy_dummy
        - Time-varying and time-invariant variables identified
        
        Recommended methods:
        1. Difference-in-Differences (high confidence) - if policy varies by state/time
        2. Fixed Effects (high confidence) - for panel analysis
        3. Random Effects (medium confidence) - if Hausman test suggests it
        
        What is your research question?"
```

## Customization

### Adding Custom Explanations

Edit `src/guidance/explanations.py` to add custom explanations:

```python
_EXPLANATION_DB['your_topic'] = {
    'basic': 'Concise explanation',
    'educational': 'Detailed explanation with theory and context'
}
```

### Extending Methodology Selection

Edit `src/guidance/methodology_selection.py` to:
- Add new data structure detection logic
- Extend research question classification
- Add custom method recommendations

### Modifying Rules

Edit `.cursor/rules/*.mdc` files to customize:
- Method requirements
- Diagnostic requirements
- Reporting standards
- Data handling procedures

## Troubleshooting

### Agent Not Using Methodology Selection

**Check:**
1. `.cursor/rules/methodology-selection.mdc` exists and is properly formatted
2. `src/guidance/` directory exists with all modules
3. Python dependencies installed (`pip install -r requirements.txt`)
4. Cursor has reloaded rules (restart Cursor or reload window)

### Import Errors

**Check:**
1. All required packages installed: `pip install -r requirements.txt`
2. Python path includes project root
3. Virtual environment activated (if using one)

### Explanations Not Working

**Check:**
1. `src/guidance/explanations.py` exists with `_EXPLANATION_DB`
2. Topic names match (check available topics in code)
3. Mode is 'basic' or 'educational'

### Corpus Not Loading

**Check:**
1. `data/corpus/` directory exists with subdirectories:
   - `data/corpus/wooldridge_embeddings/embeddings.json`
   - `data/corpus/wooldridge_index/index.json`
   - `data/corpus/wooldridge_index/cross_references.json`
2. Corpus files are not corrupted (try loading manually with `WooldridgeRetriever()`)
3. `sentence-transformers` package is installed: `pip install sentence-transformers`

**If corpus is missing or corrupted:**
Rebuild the corpus from source files:
```bash
python -m src.corpus.cli build
```
This requires the `docs/wooldridge_extracts/` directory with markdown source files.

### Corpus Search Returns No Results

**Possible causes:**
1. Corpus not loaded (see "Corpus Not Loading" above)
2. Query too specific - try broader terms
3. Corpus data outdated - rebuild if source files have changed

**Test corpus:**
```python
from src.corpus import WooldridgeRetriever
retriever = WooldridgeRetriever()
results = retriever.semantic_search("fixed effects", top_k=5)
print(f"Found {len(results)} results")
```

## File Structure Summary

### Required for Methodology Selection

**Essential:**
- `.cursor/rules/methodology-selection.mdc` - Rule file for Cursor agent
- `src/guidance/` - Methodology selection system (all files)

**Supporting (for full functionality):**
- `.cursor/rules/causal-inference.mdc` - Causal method rules
- `.cursor/rules/panel-data.mdc` - Panel method rules
- `.cursor/rules/regression-core.mdc` - OLS rules
- `.cursor/rules/diagnostics.mdc` - Diagnostic rules
- `.cursor/rules/wooldridge-references.mdc` - Wooldridge corpus reference guide
- `.cursor/rules/triangulation-guide.mdc` - Perspective triangulation guide
- `src/models/` - Econometric model implementations
- `src/utils/` - Utility functions

### Required for Wooldridge Corpus

**Essential:**
- `src/corpus/` - Complete corpus system (all Python files)
- `data/corpus/` - Built corpus data (embeddings, indices, cross-references)

**Recommended (for rebuilding if needed):**
- `docs/wooldridge_extracts/` - Source markdown files (16 MB, ~82 files)
  - Required only if you need to rebuild the corpus
  - Included for reference and future updates

### Optional (for specific features)

- `src/data/` - Data loading utilities (if using data loaders)
- `.cursor/rules/data-handling.mdc` - Data preparation rules
- `.cursor/rules/reporting.mdc` - Reporting standards
- `.cursor/rules/visualization.mdc` - Plotting standards
- `.cursor/rules/workflow-best-practices.mdc` - Workflow guidelines (recommended)
- `.cursor/rules/code-standards.mdc` - Code style guide (recommended)
- Evaluation documents (HANSEN_EVALUATION.md, ANGRIST_EVALUATION.md, WOOLDRIDGE_EVALUATION.md) - Referenced in rules but not required

## Rebuilding the Corpus (If Needed)

The corpus is pre-built and ready to use. You only need to rebuild if:
- Corpus data becomes corrupted
- You want to update the corpus with modified source files
- You need to rebuild after modifying `docs/wooldridge_extracts/` files

**To rebuild:**

1. Ensure source files exist: `docs/wooldridge_extracts/` directory with markdown files
2. Run the build command:
   ```bash
   python -m src.corpus.cli build
   ```
3. Wait for completion (takes a few minutes - analyzes ~82 files and generates embeddings)
4. Verify rebuild:
   ```python
   from src.corpus import WooldridgeRetriever
   retriever = WooldridgeRetriever()
   print("✅ Corpus rebuilt successfully!")
   ```

**Note**: Rebuilding requires the `sentence-transformers` package and downloads a model (~90 MB) on first use.

## Iteration Hygiene: Preventing Analysis Pollution

When modifying or re-running models mid-workflow, it's important to clean previous outputs to prevent confusion. The package includes a reset utility for this purpose.

### Reset Analysis Script

**Location**: `scripts/reset_analysis.py`

**Purpose**: Cleans previous analysis outputs before re-running modified models to prevent:
- Old figures being confused with new results
- Outdated result files being referenced
- Cache files causing unexpected behavior

**Usage**:

```bash
# Dry run (see what would be deleted)
python scripts/reset_analysis.py --dry-run

# Actually reset outputs
python scripts/reset_analysis.py
```

**What gets cleaned**:
- All files in `data/outputs/`
- Transient files in project root (`*.png`, `*.pdf`, `*results*.csv`, etc.)
- Cache directories (`__pycache__`, `.pytest_cache`)

**When to use**:
- Before re-running a modified model specification
- When changing identification strategy (e.g., switching from OLS to IV)
- When you want a clean slate for a new analysis

**Agent Integration**: The Cursor agent will automatically suggest running this script when it detects you're modifying or re-running models. You can also run it manually at any time.

### Data Directory Structure

The package includes the following data directories (created automatically):

- **`data/raw/`** - Place your original, unmodified data files here
- **`data/processed/`** - Store cleaned, transformed data here
- **`data/outputs/`** - All generated outputs (figures, tables, results) are saved here
  - This directory gets cleaned by `reset_analysis.py`
  - Organize outputs in subdirectories: `data/outputs/figures/`, `data/outputs/tables/`, `data/outputs/results/`

**Note**: These directories are created with `.gitkeep` files to preserve the structure in git. Your actual data files should be added to `.gitignore` or committed separately.

## Next Steps

1. **Load Your Data**: Place data files in `data/raw/` or `data/processed/`
2. **Ask for Guidance**: Start a conversation in Cursor chat about your research question
3. **Explore Methods**: Ask about different methods and their assumptions
4. **Query Wooldridge**: Ask the agent about Wooldridge's perspective on methodologies
5. **Run Analysis**: Use the recommended methods with your data
6. **Clean Between Iterations**: Use `python scripts/reset_analysis.py` when modifying models
7. **Get Explanations**: Request detailed explanations when needed

## Support

For issues or questions:
- Check rule files (`.cursor/rules/*.mdc`) for method requirements
- Review code documentation in `src/` modules
- Consult evaluation documents (HANSEN_EVALUATION.md, ANGRIST_EVALUATION.md, WOOLDRIDGE_EVALUATION.md) for methodological guidance

---

**Note:** This agent is designed to assist with methodology selection and provide explanations. It does not replace domain expertise or careful consideration of your specific research context. Always validate assumptions and interpret results in light of your research question and data.

