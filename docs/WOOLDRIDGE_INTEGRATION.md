# Wooldridge Thought Integration Guide

## What's New in This Release

This release integrates **Wooldridge Thought** - authoritative econometric guidance from Jeffrey Wooldridge's "Econometric Analysis of Cross Section and Panel Data" (2nd ed., 2010).

### Major Features

1. **Portable Wooldridge Textbook** (73 page-range files)
   - Self-contained in `docs/wooldridge_textbook/`
   - No external downloads or API calls required
   - Works offline and in any environment

2. **Page-Level Citations** (in all search results)
   - Search results include precise Wooldridge page references
   - Example: "Wooldridge, Ch. 10, Section 10.7.3, p.291-300"
   - All diagnostic thresholds cite their source

3. **Ask Wooldridge Interface** (natural language queries)
   - 9 pre-defined guidance topics
   - Corpus search fallback for general queries
   - Context-aware methodology recommendations

4. **New Specification Tests**
   - RESET test for functional form (Wooldridge, p.124-125)
   - VIF for multicollinearity (Wooldridge, Ch. 4)
   - Condition number for linear dependence

5. **Wooldridge Citations in Explanations**
   - 14 topics now include page references
   - Optional `include_citation` parameter
   - Educational mode with authoritative backing

## Getting Started

### 1. Search the Wooldridge Corpus

Find authoritative guidance on any econometric topic:

```python
from src.corpus import search_wooldridge

# Search for topics
results = search_wooldridge("hausman test", top_k=3)

for r in results:
    print(f"Title: {r['title']}")
    print(f"Citation: {r['citation']}")  # NEW: page-level citation
    print(f"Preview: {r['content'][:300]}...")
    print()
```

Output:
```
Title: 10.7.3 Specification Tests for Unobserved Effects Models
Citation: Wooldridge, p.291-300
Preview: The Hausman test can be used to test H0: RE is appropriate...
```

### 2. Ask Wooldridge for Guidance

Use natural language to get methodological advice:

```python
from src.corpus import ask_wooldridge

# Ask pre-defined topics
result = ask_wooldridge("When should I use FE vs RE?")
print(result['answer'])
print(f"Source: {result['citations']}")
print(f"Confidence: {result['confidence']}")  # high, medium, low
```

Available topics (just ask naturally):
- "Fixed effects vs random effects"
- "Weak instruments"
- "Clustered standard errors"
- "Parallel trends"
- "Robust standard errors"
- "Endogeneity test"
- "Propensity score matching"
- "First differencing"
- "Overidentification test"

### 3. Get Context-Aware Recommendations

Get Wooldridge guidance tailored to your diagnostics:

```python
from src.corpus import get_methodology_recommendation

# Based on your estimation results
rec = get_methodology_recommendation('iv',
    diagnostics={
        'f_stat': 8.5,      # First-stage F
        'sargan_p': 0.02,   # Overidentification test p-value
    })

# View warnings based on Wooldridge's guidance
print(rec['warnings'])
# Output:
# - "Weak instruments detected (F = 8.50 < 10). Consider LIML (Wooldridge, p.101-103)"
# - "Overidentification test rejects (p = 0.020). At least one instrument invalid..."

print(rec['citation'])
# Output: Wooldridge, Ch. 5, p.83-113
```

### 4. Use New Specification Tests

#### RESET Test (Functional Form)

```python
from src.diagnostics import reset_test
import numpy as np

# Estimate model and get fitted values
model = ... # your estimation
y = model.data['outcome']
X = model.data[['x1', 'x2']]
fitted = model.predict()

# Test for functional form misspecification
reset = reset_test(y, X, fitted_values=fitted, power_terms=[2, 3])

print(reset['f_statistic'])  # F-statistic
print(reset['f_pvalue'])     # p-value
print(reset['interpretation'])
# Output: "RESET test: F(2, 97) = 8.453, p = 0.0004. Reject H0..."
print(reset['citation'])     # Wooldridge, Ch. 6, Section 6.2.3, p.124-125
```

#### Variance Inflation Factors (Multicollinearity)

```python
from src.diagnostics import variance_inflation_factors
import numpy as np

# Compute VIF for each variable
X = data[['education', 'experience', 'age']]
vif = variance_inflation_factors(X, variable_names=X.columns.tolist())

print(vif['vif'])
# Output: {'education': 2.45, 'experience': 8.92, 'age': 1.13}

print(vif['max_vif'])  # 8.92 (below threshold of 10)
print(vif['high_vif_vars'])  # []
print(vif['interpretation'])
# Output: "No concerning multicollinearity. Max VIF = 8.92..."
```

### 5. Use Citations in Explanations

```python
from src.guidance import get_explanation

# Get explanation with optional Wooldridge citation
explanation = get_explanation(
    'diagnostic_hausman',
    mode='educational',
    include_citation=True  # NEW
)

print(explanation)
# Output:
# "The Hausman test compares fixed effects (FE) and random effects (RE)...
#  [Reference: Wooldridge, Ch. 10, Section 10.7.3, p.291-300]"
```

## Migration Guide for Existing Users

### Breaking Changes

None! All existing code continues to work. New features are additive.

### Recommended Updates

1. **If you use `search_wooldridge()`**
   - No changes needed
   - Results now include `citation` field automatically
   - Use `citation` in your output for better documentation

2. **If you use `get_explanation()`**
   - No changes needed
   - Add `include_citation=True` for Wooldridge references
   - Example: `get_explanation('diagnostic_hausman', include_citation=True)`

3. **If you perform IV estimation**
   - Weak instrument warnings now include Wooldridge citation
   - No code changes needed; just better diagnostics

4. **If you do panel data analysis**
   - Hausman test results now include citation
   - No code changes; better documentation in output

### New Imports to Consider

```python
# New query interface
from src.corpus import ask_wooldridge, get_methodology_recommendation

# New diagnostics
from src.diagnostics import reset_test, variance_inflation_factors

# New page index
from src.corpus import (
    METHODOLOGY_PAGES,
    get_page_citation,
    get_page_range,
)
```

## Available Topics with Page References

### Panel Data (Chapter 10)
- Fixed effects (p.263-297)
- Random effects (p.257-265)
- Hausman test (p.291-300)
- Clustered standard errors (p.274-276)
- First differencing (p.279-284)

### Instrumental Variables (Chapter 5)
- Instrumental variables (p.83-113)
- 2SLS (p.90-100)
- Weak instruments (p.101-103) [Staiger-Stock rule]
- First-stage diagnostics (p.101-103)

### Specification Tests (Chapter 6)
- Overidentification test (p.122-124)
- Endogeneity test (p.118-122)
- RESET test (p.124-125)

### Robust Inference (Chapter 4)
- Heteroskedasticity-robust SE (p.55-58)
- HC variants (p.57-58)
- Multicollinearity (Ch. 4)

### Treatment Effects (Chapter 21)
- Propensity score matching (p.704-710)
- Difference-in-differences (p.713-720)
- Regression discontinuity (p.720-725)

### Discrete Response (Chapter 15)
- Probit/logit models (p.453-490)
- Marginal effects (p.467-475)

### Limited Dependent Variables (Chapter 16)
- Tobit model (p.525-540)
- Censored regression (p.525-545)

### Generalized Method of Moments (Chapter 8)
- GMM estimation (p.195-240)
- Dynamic panel models (Ch. 11)

## Diagnostic Thresholds with Citations

All diagnostic thresholds now cite Wooldridge:

| Test | Threshold | Citation |
|------|-----------|----------|
| First-stage F | > 10 | Wooldridge, p.101-103 (Staiger-Stock) |
| Sargan/Hansen J | p > 0.05 | Wooldridge, p.122-124 |
| Hausman test | p > 0.05 | Wooldridge, p.291-300 |
| VIF | < 10 | Wooldridge, Ch. 4 |
| HC3 when | n/k < 100 | Wooldridge, p.57-58 |

## Portability and Self-Containment

### Why This Matters

- **Clone and Go**: `git clone` + `pip install` = ready to use
- **Offline**: No internet required for Wooldridge guidance
- **Reproducible**: Same results across all machines
- **No External APIs**: No rate limits or service dependencies

### Technical Details

All paths use relative resolution:

```python
from pathlib import Path

# Automatically finds repo root from anywhere
repo_root = Path(__file__).parent.parent.parent
textbook_path = repo_root / "docs" / "wooldridge_textbook"
```

This means the repo works whether you clone it to:
- `/home/user/econometrics-portable-agent-claude`
- `/Users/researcher/Projects/claude-econ`
- `C:\Users\Student\econometrics-agent`
- Any other location

## FAQ

### Q: Do I need to download anything for Wooldridge?

**A:** No. All 73 textbook page-range files are already in the repo. Just `git clone` and you're ready to go.

### Q: Can I use ask_wooldridge() offline?

**A:** Yes. Everything is self-contained - no API calls to external services.

### Q: Are the diagnostics thresholds different from before?

**A:** No. We use the same thresholds (F > 10, p < 0.05, etc.) as before. Now they include Wooldridge citations.

### Q: Will my existing code break?

**A:** No. All new features are backwards compatible. Existing imports and functions work unchanged.

### Q: How accurate is the Wooldridge corpus?

**A:** The textbook was converted from PDF to markdown. While conversion is generally clean, some equations and special characters may not be perfect. Use the page references to verify specific technical details in the original textbook.

## Examples: Before and After

### Before (v1)
```python
results = search_wooldridge("hausman test")
print(f"Found: {results[0]['title']}")
print(f"Source: {results[0]['file_name']}")
```

### After (v2) - NEW citations!
```python
results = search_wooldridge("hausman test")
print(f"Found: {results[0]['title']}")
print(f"Citation: {results[0]['citation']}")  # NEW!
# Output: Citation: Wooldridge, p.291-300
```

### New Interface
```python
# Just ask in plain English
from src.corpus import ask_wooldridge

result = ask_wooldridge("When should I use Hausman test?")
print(result['answer'])  # Wooldridge's direct guidance
```

## Next Steps

1. **Try ask_wooldridge()** with questions about your analysis
2. **Use search_wooldridge()** to cite Wooldridge in your reports
3. **Apply RESET/VIF tests** for comprehensive diagnostics
4. **Check diagnostic warnings** - they now include Wooldridge citations

## Support and Questions

For issues or questions about the Wooldridge integration:

1. Check this guide for examples
2. See the docstrings in code: `help(ask_wooldridge)`
3. Review the plan in `/docs/WOOLDRIDGE_INTEGRATION.md`
4. Open an issue on GitHub

---

**Reference:**

Wooldridge, J. M. (2010). *Econometric Analysis of Cross Section and Panel Data* (2nd ed.). MIT Press.

All page references refer to the 2nd edition (2010).
