# Claude Code Agent Guide

This file provides guidance for AI assistants working on this econometrics project.

## Project Overview

**Read first:** `README.md` for full project documentation.

This is an econometrics agent for applied microeconometrics research with:
- Causal inference methods (DiD, RD, IV, Matching)
- Panel data methods (FE, RE, Panel IV)
- Textbook corpus for methodology triangulation

## Cursor Rules

**Follow the rules in `.cursor/rules/*.mdc`** for methodology guidance:
- `project-overview.mdc` - Project structure and focus areas
- `triangulation-guide.mdc` - How to compare Hansen/Angrist/Wooldridge
- `causal-inference.mdc` - DiD, RD, IV, Matching methods
- `panel-data.mdc` - Fixed effects, random effects, panel IV
- `wooldridge-references.mdc` - Textbook corpus locations

## Textbook Access - Comprehensive Page Mappings

At the start of any econometric analysis, **load relevant textbook pages into context**.

### Textbook Locations
- **Wooldridge**: `docs/wooldridge/` (73 files, 10-page ranges)
- **Angrist/MHE**: `docs/angrist/` (15 files, 20-page ranges)
- **Hansen**: `docs/hansen_practices/HANSEN_EVALUATION.md`

Page markers (`{123}---`) preserved for citations.

### Panel Data Methods (Ch 10-11, pages 259-350)

**Core Panel Data (Ch 10: pages 259-310)**
- pages_251-260.md - (End of Ch 9, start of Ch 10)
- pages_261-270.md - Ch 10.1: Motivation, omitted variables problem
- pages_271-280.md - Ch 10.4: Random effects, FGLS, testing for effects
- pages_281-290.md - Ch 10.5: Fixed effects, asymptotic inference, dummy variables
- pages_291-300.md - Ch 10.5-10.6: FE policy analysis, first differencing, inference
- pages_301-310.md - Ch 10.7: FE vs FD, Hausman test

**Advanced Panel (Ch 11: pages 310-350)**
- pages_311-320.md - Ch 11.1: Sequential moment restrictions
- pages_321-330.md - Ch 11.1: Contemporaneous correlation, endogeneity
- pages_331-340.md - Ch 11.2: Individual-specific slopes, random trends
- pages_341-350.md - Ch 11.2: General individual slopes (end of Ch 11)

### Instrumental Variables (Ch 5-6, pages 98-156)

**IV Basics (Ch 5: pages 98-130)**
- pages_91-100.md - (End of Ch 4, start of Ch 5: IV motivation)
- pages_101-110.md - Ch 5.1-5.2: 2SLS, consistency, asymptotic normality
- pages_111-120.md - Ch 5.2: Efficiency, heteroskedasticity-robust inference
- pages_121-130.md - Ch 5.3: IV for omitted variables, measurement error

**IV Testing & Extensions (Ch 6: pages 129-156)**
- pages_131-140.md - Ch 6.1-6.2: Generated regressors, specification tests
- pages_141-150.md - Ch 6.2-6.3: Testing overid, sampling schemes
- pages_151-160.md - Ch 6.3: Cluster samples, stratified samples (end of Ch 6)

### OLS & Omitted Variables (Ch 4: pages 65-92)
- pages_61-70.md - (End of Ch 3, start of Ch 4: single-equation model)
- pages_71-80.md - Ch 4.2-4.3: Consistency, LM tests, omitted variables
- pages_81-90.md - Ch 4.3-4.4: Proxy variables, measurement error
- pages_91-100.md - Ch 4.4-5.1: Measurement error, start of IV

### Treatment Effects (Ch 18: pages 578-621)
- pages_571-580.md - (Start of Ch 18)
- pages_581-590.md - Ch 18: Treatment effect methods
- pages_591-600.md - Ch 18: Continued
- pages_601-610.md - Ch 18.3-18.4: Matching, PSM
- pages_611-620.md - Ch 18.3.1: Regression methods

### Quick Topic Reference

| Topic | Primary Files |
|-------|--------------|
| Fixed Effects | pages_271-280.md, pages_281-290.md |
| Random Effects | pages_271-280.md |
| Hausman Test | pages_301-310.md |
| Clustered SE | pages_181-190.md, pages_291-300.md |
| 2SLS | pages_101-110.md |
| Weak Instruments | pages_111-120.md |
| Difference-in-Differences | pages_291-300.md |
| Propensity Score Matching | pages_601-610.md |

## Model Selection Rules

### Easy Tasks → Use Haiku
**Cost**: Lowest | **Speed**: Fastest | **Capability**: Basic operations

Use for:
- Simple file operations (copy, delete, rename)
- Running existing scripts/tests
- Quick searches or lookups

**Example**: "Run pytest" or "List files in directory" or "Check Python version"

---

### Medium Tasks → Use Sonnet
**Cost**: Moderate | **Speed**: Fast | **Capability**: Complex reasoning

Use for:
- Data exploration and basic inspection
- Reading and understanding code
- Straightforward data transformations
- Cleanup tasks
- Writing new code modules
- Designing algorithms
- Debugging complex issues
- Code refactoring
- Creating documentation
- Implementing new features
- Data analysis and exploration
- Planning implementations

**Example**: "Implement a new diagnostic test" or "Create a migration guide" or "Fix a complex bug"

---

### Hard Tasks → Use Opus
**Cost**: Highest | **Speed**: Slower | **Capability**: Advanced reasoning, novel problems

Use for:
- Multi-phase projects requiring architectural decisions
- Novel econometric methods not yet in codebase
- Complex refactoring affecting multiple systems
- Advanced debugging of production issues
- Strategic planning for major features

**Example**: "Redesign the entire corpus system" or "Implement new econometric methodology"

---

## Quick Decision Tree

1. **Is it a quick operation?** (1 minute or less, no code writing)
   → **Haiku**

2. **Does it require writing new code or problem-solving?**
   → **Sonnet**

3. **Is it a major architectural decision or novel approach?**
   → **Opus**

---

## Current Project Context


---

## Reminders

- **Always check**: Is this a quick task or does it need complex reasoning?
- **Cost matters**: Haiku is ~5x cheaper, Sonnet is ~3x cheaper than Opus
- **Speed matters**: Haiku is fastest for simple tasks
- **Quality matters**: Use Sonnet/Opus for code quality and reasoning
- **Default**: When in doubt, use Sonnet (good balance of cost, speed, capability)

---

## Environment Notes

- **Python**: Always use `python3` (not `python`) - the global environment does not alias `python` to `python3`
- **Python version**: 3.14.2 (as of 2026-01-05)
- **Scripts**: Run scripts with `python3 scripts/script_name.py`

---

Last updated: 2026-01-05
