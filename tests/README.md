# Tests for Econometrics Portable Agent

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_models/test_diff_in_diff.py

# Run specific test
pytest tests/test_models/test_diff_in_diff.py::test_did_basic_estimation
```

## Test Structure

```
tests/
├── test_models/           # Tests for econometric models
│   ├── test_diff_in_diff.py
│   ├── test_regression_discontinuity.py
│   ├── test_matching.py
│   ├── test_instrumental_variables.py
│   ├── test_fixed_effects.py
│   ├── test_random_effects.py
│   └── test_standard_errors.py
│
├── test_corpus/           # Tests for Wooldridge corpus system
│   ├── test_retriever.py
│   ├── test_embeddings.py
│   └── test_triangulation.py
│
├── test_diagnostics/      # Tests for diagnostic tests
│   ├── test_weak_instruments.py
│   ├── test_parallel_trends.py
│   ├── test_balance_tests.py
│   └── test_manipulation_test.py
│
└── test_guidance/         # Tests for methodology selection
    ├── test_methodology_selection.py
    └── test_explanations.py
```

## Test Philosophy

### What to Test

1. **Correctness**: Do methods produce correct estimates?
   - Test against known results (simulated data with known parameters)
   - Test against published examples (Card-Krueger, Angrist-Krueger, etc.)
   - Validate against other implementations (statsmodels, linearmodels)

2. **Diagnostics**: Do diagnostic tests work correctly?
   - Test that weak instruments are detected
   - Test that parallel trends violations are caught
   - Test that manipulation tests work

3. **Edge Cases**: Handle unusual inputs gracefully
   - Empty data
   - Missing values
   - Perfect multicollinearity
   - Single time period
   - No within-variation

4. **Robustness**: Results stable across specifications
   - Standard errors change appropriately (robust vs clustered)
   - Estimates robust to reasonable specification changes

### What NOT to Test

- Don't test external libraries (statsmodels, linearmodels) - assume they work
- Don't test trivial functions (getters, setters)
- Don't test plotting functions extensively - visual inspection better

## Priority Tests to Add

### High Priority
1. **DiD validation** - Test against Card-Krueger (1994) data
2. **IV validation** - Test against Angrist-Krueger (1991) results
3. **Standard errors** - Validate HC1, HC2, HC3, clustered against statsmodels
4. **Panel FE** - Test within transformation matches linearmodels

### Medium Priority
5. **RD validation** - Test against Lee (2008) or similar
6. **Matching balance** - Test balance improvement metrics
7. **Corpus retrieval** - Test semantic search accuracy
8. **Methodology selection** - Test recommendation logic

### Lower Priority
9. **Plotting functions** - Basic smoke tests
10. **CLI interface** - Integration tests
11. **Data loading** - Test various formats

## Test Data

Tests use:
- **Simulated data** - Generated with known parameters
- **Public datasets** - Card-Krueger NJ minimum wage, Angrist-Krueger quarter of birth
- **Small examples** - From textbooks (Wooldridge, Stock-Watson)

## Coverage Goals

- **Models**: > 80% coverage
- **Diagnostics**: > 80% coverage
- **Corpus**: > 60% coverage (some functions hard to test)
- **Overall**: > 70% coverage

## Notes

- Tests are currently **stubs** - implementations needed
- Focus on **regression tests** - ensure changes don't break existing functionality
- Use **fixtures** for common data patterns
- Tests should run in **< 30 seconds** total (fast feedback)
- Mark slow tests with `@pytest.mark.slow` decorator
