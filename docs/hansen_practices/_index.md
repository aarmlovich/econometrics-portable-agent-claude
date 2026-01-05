# Hansen Practices Quick Reference

> Source: Bruce Hansen's Econometrics Textbook Code (Stata/R)
> Based on: HANSEN_EVALUATION.md

## Key Practices

### Standard Errors (High Agreement)
- **Default**: Use robust SE (HC1) - Stata's `, r` option
- **Panel data**: Use `vce(robust)` with fixed effects
- **Clustered**: Cluster at entity level when within-unit correlation exists
- **HC3 (jackknife)**: Preferred for small samples (<250 obs per regressor)

### IV Diagnostics (High Agreement)
- **Always report first-stage** regression and F-statistic
- **F-statistic threshold**: F > 10 (Staiger-Stock rule of thumb)
- **Overidentification tests**: Use non-robust tests (standard practice)
- **Use `testparm`**: For testing joint significance of instruments

### Panel Data Methods (High Agreement)
- **Fixed effects**: Use `xtreg, fe vce(robust)`
- **Clustering**: Our clustering is MORE appropriate than just robust SE
- **Serial correlation**: Account for within-unit correlation

### Code Quality
- **Simplicity over complexity**: Direct, readable code
- **Comparison tables**: Always show alternative specifications
- **Summary statistics**: Know your data before modeling
- **Random seeds**: Set seeds for reproducibility in bootstrap/jackknife

## Where Hansen and Agent Differ

| Topic | Hansen | Our Agent | Verdict |
|-------|--------|-----------|---------|
| Missing data | Silent deletion | Document all drops | Agent is more rigorous |
| Panel SE | `vce(robust)` | Clustered SE | Agent is more appropriate |
| RD bandwidth | Simple polynomial | Cross-validation | Agent is more rigorous |
| Balance tests | Implicit (summary stats) | Explicit tests | Agent is more rigorous |

## Files

- [HANSEN_EVALUATION.md](./HANSEN_EVALUATION.md) - Full evaluation document
