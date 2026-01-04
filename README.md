# Econometrics Agent for Cursor

An AI-powered econometrics agent for applied microeconometrics research, designed to work seamlessly with Cursor IDE. This agent automates complex econometric analyses with a focus on causal inference and panel data methods.

## Overview

The Econometrics Agent provides a hybrid architecture supporting three usage modes:
- **Library**: Importable Python package with functions and classes
- **CLI**: Command-line interface for batch processing
- **Cursor Integration**: Interactive agent for conversational analysis via Cursor chat

## Focus Areas

### Priority #1: Causal Inference
- Difference-in-differences (DiD) with parallel trends testing
- Regression discontinuity (RD) with bandwidth selection
- Matching methods (propensity score, nearest neighbor)
- Instrumental variables (IV) with first-stage diagnostics

### Priority #2: Panel Data Methods
- Fixed effects models (entity and time)
- Random effects with Hausman test
- Panel IV estimation
- Panel-specific diagnostics (serial correlation, heteroskedasticity)

### Additional Capabilities
- Core regression (OLS with robust/clustered standard errors)
- Diagnostic testing and visualization
- Basic time series methods (for robustness checks)

### Wooldridge Thought Integration
- **Portable Wooldridge Textbook**: 73 page-range markdown files embedded in `docs/wooldridge_textbook/`
- **Page-Level Citations**: All search results include Wooldridge page references
- **Ask Wooldridge**: Natural language query interface for econometric guidance
- **Specification Tests**: RESET test for functional form, VIF for multicollinearity
- **Authoritative Thresholds**: All diagnostic thresholds cite Wooldridge (F < 10 for weak instruments, etc.)

## Installation

### Prerequisites

- Python 3.10 or higher (Python 3.11+ recommended)
- pip (Python package installer)

### Recommended: Automated Setup

**The easiest way to get started:**

**macOS/Linux:**
```bash
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

This script will:
- ✓ Check Python version (requires 3.10+)
- ✓ Create virtual environment in `venv/`
- ✓ Activate the virtual environment
- ✓ Install all dependencies from requirements.txt
- ✓ Install the package in editable mode
- ✓ Install test dependencies (pytest, pytest-cov)

**After setup completes:**
```bash
# Activate venv (do this each time you work on the project)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Verify installation
python -c "import src; print('Package imported successfully!')"

# Run tests
pytest tests/

# When done working
deactivate
```

### Manual Setup (Alternative)

If you prefer manual setup or need more control:

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/econometrics-agent.git
cd econometrics-agent
```

2. **Create virtual environment (REQUIRED):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Why virtual environment is required:**
- Isolates dependencies from other Python projects
- Ensures reproducibility across different machines
- Prevents version conflicts (this project needs pandas>=2.0.0, statsmodels>=0.14.0)
- Easy to reset if something goes wrong (just delete `venv/` and recreate)

3. **Upgrade pip:**
```bash
pip install --upgrade pip
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Install package in editable mode:**
```bash
pip install -e .
```

6. **Install test dependencies:**
```bash
pip install pytest pytest-cov
```

### Verify Installation

**Check Python version:**
```bash
python3 scripts/check_python_compatibility.py
```

**Run basic import test:**
```bash
python -c "import src; print('✓ Package imported successfully')"
```

**Run test suite:**
```bash
pytest tests/ -v
```

For detailed requirements and compatibility information, see [REQUIREMENTS.md](REQUIREMENTS.md).

## Methodology Selection (Cursor Chat)

The agent provides interactive methodology selection guidance in Cursor chat:

**Ask for method recommendations:**
```
"I have panel data on firms. I want to estimate the effect of a policy. What method should I use?"
```

**Get explanations:**
```
"Why is DiD appropriate here?"
"Explain in more detail"  # Toggles to educational mode
```

The methodology selection system:
- Analyzes your data structure (panel vs. cross-section, treatment variables, etc.)
- Classifies your research question (causal, descriptive, predictive)
- Recommends appropriate methods with confidence levels and rationale
- Provides economic intuition, causal identification, and statistical explanations
- Offers basic (concise) or educational (detailed) explanation modes

See [PORTABILITY.md](PORTABILITY.md) for details on using the agent in new Cursor projects.

## Quick Start

### Using as a Library

```python
import pandas as pd
from src.models.causal.diff_in_diff import DifferenceInDifferences
from src.models.regression.ols import OLSRegression

# Load your data
data = pd.read_csv("your_data.csv")

# Run difference-in-differences analysis
did = DifferenceInDifferences(
    data=data,
    outcome="outcome_var",
    treatment="treatment_var",
    time="time_var",
    unit="unit_var"
)
results = did.estimate()
```

### Using the CLI

```bash
# Run a regression analysis
econ-agent run-analysis --method ols --data data.csv --outcome Y --covariates X1 X2

# Run difference-in-differences
econ-agent run-analysis --method did --data data.csv --outcome Y --treatment T --time year --unit id

# Run regression discontinuity
econ-agent run-analysis --method rd --data data.csv --outcome Y --running score --cutoff 50

# Run matching
econ-agent run-analysis --method matching --data data.csv --outcome Y --treatment T --covariates X1 X2

# Run instrumental variables
econ-agent run-analysis --method iv --data data.csv --outcome Y --treatment X --instruments Z1 Z2

# Run fixed effects panel regression
econ-agent run-analysis --method fe --data data.csv --outcome Y --entity id --time year --covariates X1 X2

# Run random effects panel regression
econ-agent run-analysis --method re --data data.csv --outcome Y --entity id --time year --covariates X1 X2

# Run panel IV
econ-agent run-analysis --method panel_iv --data data.csv --outcome Y --treatment X --instruments Z --entity id --time year

# Validate data structure
econ-agent validate-data --data data.csv --panel unit time

# Generate analysis report
econ-agent generate-report --results results.json --output report.html
```

### Using with Cursor

The agent integrates with Cursor through `.cursor/rules/` configuration files. Simply open your project in Cursor and the agent will use the rules to guide econometric analyses.

Ask questions like:
- "Help me set up a difference-in-differences analysis"
- "Run a fixed effects regression with clustered standard errors"
- "Test for parallel trends in my panel data"

## Wooldridge Corpus Integration

The agent integrates Wooldridge's "Econometric Analysis of Cross Section and Panel Data" (2nd ed.) textbook as a searchable, page-indexed corpus for authoritative econometric guidance.

### Key Features

- **73 Page-Range Files**: Embedded in `docs/wooldridge_textbook/` for portability
- **Page-Level Citations**: All search results include precise Wooldridge page references
- **Ask Wooldridge**: Natural language query interface for econometric guidance
- **No External Dependencies**: Fully self-contained with relative paths

### Using the Wooldridge Corpus

#### Ask Wooldridge for Guidance

```python
from src.corpus import ask_wooldridge

# Ask for methodological advice
result = ask_wooldridge("When should I use fixed effects vs random effects?")
print(result['answer'])  # Wooldridge's guidance
print(result['citations'])  # Page references
```

#### Search with Page Citations

```python
from src.corpus import search_wooldridge

# Search for topics with page references
results = search_wooldridge("hausman test", top_k=3)
for r in results:
    print(f"{r['title']} ({r['citation']})")
    print(r['content'][:300])
```

#### Get Methodology Recommendations

```python
from src.corpus import get_methodology_recommendation

# Get Wooldridge guidance for a specific method
rec = get_methodology_recommendation('iv',
    diagnostics={'f_stat': 8.5, 'sargan_p': 0.02})

# View warnings based on diagnostics
print(rec['warnings'])  # Includes Wooldridge citations
```

#### Specification Testing

```python
from src.diagnostics import reset_test, variance_inflation_factors

# Test functional form (Wooldridge, Ch. 6, p.124-125)
reset = reset_test(y, X)
print(reset['interpretation'])

# Test multicollinearity (Wooldridge, Ch. 4)
vif = variance_inflation_factors(X)
print(f"Max VIF: {vif['max_vif']}")  # Threshold: 10
```

### Available Wooldridge Topics

**Panel Data**: fixed_effects, random_effects, hausman_test, clustered_se, first_differencing

**Instrumental Variables**: instrumental_variables, 2sls, weak_instruments, overidentification, endogeneity_test

**Robust Inference**: robust_se, heteroskedasticity_robust, hc_variants

**Treatment Effects**: matching, propensity_score, diff_in_diff, regression_discontinuity

**Diagnostics**: reset_test (functional form), vif (multicollinearity)

### Portability Notes

- **Relative Paths**: All corpus paths use `Path(__file__).parent` for portability
- **Self-Contained**: No external API calls or downloads needed
- **GitHub-Ready**: Clone and run - textbook is included in the repository
```

### Verifying Corpus Installation

To verify the corpus is working correctly:

```python
from src.corpus import WooldridgeRetriever

# Initialize retriever (loads corpus data)
retriever = WooldridgeRetriever()

# Test semantic search
results = retriever.semantic_search("fixed effects panel data", top_k=3)
print(f"Found {len(results)} results")

# Test topic lookup
topic_info = retriever.lookup_topic("panel_data")
print(f"Topic info: {topic_info}")
```

See `docs/wooldridge_integration_guide.md` for detailed documentation.

## Project Structure

```
econometrics-agent/
├── .cursor/
│   └── rules/              # Cursor agent rules
├── src/
│   ├── data/               # Data loading and preprocessing
│   ├── models/             # Econometric models
│   │   ├── regression/     # OLS and core regression
│   │   ├── panel/          # Panel data methods
│   │   └── causal/         # Causal inference methods
│   ├── corpus/             # Wooldridge corpus tools
│   │   ├── agent_integration.py  # Agent integration layer
│   │   ├── triangulation.py     # Perspective triangulation
│   │   └── validation.py        # Validation system
│   ├── diagnostics/        # Diagnostic tests and plots
│   ├── guidance/           # Methodology selection guidance
│   ├── utils/              # Utility functions
│   ├── cli.py              # Command-line interface
│   └── main.py             # Main entry point
├── tests/                  # Test suite
├── data/                   # Data directories (gitignored)
│   ├── raw/
│   ├── processed/
│   └── outputs/
├── docs/
│   └── notebooks/          # Example notebooks
├── requirements.txt        # Core dependencies
├── requirements-dev.txt    # Development dependencies
└── setup.py                # Package setup
```

## Features

### Causal Inference Methods

#### Difference-in-Differences
- Automatic parallel trends testing
- Event study specification
- Balance tests
- Placebo tests with fake treatment dates
- Clustered standard errors

#### Regression Discontinuity
- Optimal bandwidth selection (cross-validation)
- Manipulation testing (McCrary test)
- Bandwidth robustness checks
- Visualization with binned data

#### Matching
- Propensity score matching
- Balance diagnostics (before/after)
- Multiple matching algorithms
- Common support checks

#### Instrumental Variables
- First-stage diagnostics (F-statistic)
- Weak instrument tests
- Overidentification tests
- Reduced-form estimates

### Panel Data Methods

- Two-way fixed effects
- Random effects with Hausman test
- Entity and time fixed effects
- Panel IV estimation with fixed effects
- Panel-specific diagnostics
- Clustered standard errors with small-sample correction

### Wooldridge Corpus Integration

- Semantic search of Wooldridge's textbook
- Triangulation with Hansen and Angrist perspectives
- Validation of rules and models against Wooldridge recommendations
- Methodology coverage analysis

### Diagnostics and Visualization

- Publication-quality figures
- Residual analysis plots
- Diagnostic test suite
- Model specification tests
- Colorblind-friendly palettes

## Usage Examples

### Example 1: Difference-in-Differences

```python
from src.models.causal.diff_in_diff import DifferenceInDifferences

did = DifferenceInDifferences(
    data=panel_data,
    outcome="earnings",
    treatment="treatment_group",
    time="year",
    unit="person_id"
)

results = did.estimate()
did.plot_parallel_trends()
did.run_event_study()
```

### Example 2: Fixed Effects Panel Regression

```python
from src.models.panel.fixed_effects import FixedEffects

fe = FixedEffects(
    data=panel_data,
    outcome="wage",
    covariates=["education", "experience"],
    entity="person_id",
    time="year"
)

results = fe.estimate()
fe.run_diagnostics()
```

### Example 3: Regression Discontinuity

```python
from src.models.causal.regression_discontinuity import RegressionDiscontinuity

rd = RegressionDiscontinuity(
    data=rd_data,
    outcome="outcome",
    running="score",
    cutoff=50,
    bandwidth=None,  # Will be selected automatically
    polynomial=1
)

results = rd.estimate()
print(rd.summary())
manipulation_test = rd.test_manipulation()
robustness = rd.estimate_robustness_bandwidths()
```

### Example 4: Matching

```python
from src.models.causal.matching import Matching

match = Matching(
    data=data,
    outcome="outcome",
    treatment="treatment",
    covariates=["X1", "X2", "X3"],
    matching_method="nearest_neighbor",
    trim_support=True
)

# Check balance before matching
balance_pre = match.test_balance_pre_matching()

# Estimate treatment effect
results = match.estimate()

# Check balance after matching
balance_post = match.test_balance_post_matching()
print(match.summary())
```

### Example 5: Instrumental Variables

```python
from src.models.causal.instrumental_variables import InstrumentalVariables

iv = InstrumentalVariables(
    data=data,
    outcome="outcome",
    treatment="treatment",
    instruments=["instrument1", "instrument2"],
    covariates=["X1", "X2"]
)

# Estimate first stage
first_stage = iv.estimate_first_stage()

# Estimate 2SLS
results = iv.estimate()

# Test for weak instruments
weak_test = iv.test_weak_instruments()

# Test overidentification (if over-identified)
overid_test = iv.test_overidentification()

# Estimate reduced form
reduced_form = iv.estimate_reduced_form()

print(iv.summary())
```

### Example 6: Random Effects Panel Regression

```python
from src.models.panel.random_effects import RandomEffects
from src.models.panel.fixed_effects import FixedEffects

# Estimate random effects
re = RandomEffects(
    data=panel_data,
    outcome="wage",
    covariates=["education", "experience"],
    entity="person_id",
    time="year"
)

re_results = re.estimate()

# Compare with fixed effects using Hausman test
fe = FixedEffects(
    data=panel_data,
    outcome="wage",
    covariates=["education", "experience"],
    entity="person_id",
    time="year"
)
fe_results = fe.estimate()

hausman = re.test_hausman(fe_results)
print(re.summary())
```

### Example 7: Panel IV

```python
from src.models.panel.panel_iv import PanelIV

panel_iv = PanelIV(
    data=panel_data,
    outcome="outcome",
    treatment="treatment",
    instruments=["instrument"],
    entity="entity_id",
    time="year",
    covariates=["X1", "X2"],
    entity_effects=True,
    time_effects=True
)

results = panel_iv.estimate()
first_stage = panel_iv.estimate_first_stage()
weak_test = panel_iv.test_weak_instruments()
print(panel_iv.summary())
```

## Development

### Running Tests

```bash
pytest tests/ -v
```

With coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

### Code Quality

Format code:
```bash
black src/ tests/
```

Lint:
```bash
flake8 src/ tests/
```

Type checking:
```bash
mypy src/
```

## Documentation

- See `.cursor/rules/` for detailed agent configuration and guidelines
- Check `docs/notebooks/` for example analyses
- **Wooldridge Corpus**: See `docs/wooldridge_integration_guide.md` for corpus usage
- **Triangulation**: See `.cursor/rules/triangulation-guide.mdc` for perspective synthesis
- API documentation (coming soon)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built for applied microeconometrics research
- Designed to work seamlessly with Cursor IDE
- Inspired by best practices in econometric software (Stata, R)

## Support

For issues, questions, or suggestions, please open an issue on the repository.

