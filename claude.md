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

## Textbook Corpus

Direct file access to three sources:
- **Wooldridge**: `docs/wooldridge_panel/` (panel data, SE, IV)
- **Angrist/MHE**: `docs/angrist_mhe/` (causal inference)
- **Hansen**: `docs/hansen_practices/` (code practices)

Each has `_index.md` with table of contents. Page markers (`{123}---`) preserved for citations.

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
