# Cursor Rules for Econometrics Agent

This directory contains Cursor agent rules that guide the AI assistant in providing econometric analysis guidance.

## Rule Files

### Always Applied Rules (`alwaysApply: true`)
These rules are always loaded and available:

- **project-overview.mdc**: Project overview and purpose (always applied)
- **wooldridge-references.mdc**: Wooldridge corpus reference guide (always applied)
- **triangulation-guide.mdc**: Perspective triangulation framework (always applied)

### Context-Specific Rules
These rules are automatically selected based on file patterns (`globs`) or when relevant:

- **methodology-selection.mdc**: Methodology selection system (matches `**/guidance/**/*.py`)
- **causal-inference.mdc**: Causal inference methods (matches `**/causal/**/*.py`, etc.)
- **panel-data.mdc**: Panel data methods (matches `**/panel/**/*.py`)
- **regression-core.mdc**: Core regression methods
- **diagnostics.mdc**: Diagnostic tests
- **data-handling.mdc**: Data loading and preprocessing
- **reporting.mdc**: Reporting standards
- **visualization.mdc**: Visualization standards
- **time-series-basic.mdc**: Basic time series methods
- **workflow-best-practices.mdc**: Workflow guidelines
- **code-standards.mdc**: Code style guide

## Evaluation Document References

Some rule files reference evaluation documents:
- `WOOLDRIDGE_EVALUATION.md`
- `HANSEN_EVALUATION.md`
- `ANGRIST_EVALUATION.md`

These documents are **optional** - the rules will work without them, but references in rule files may point to non-existent files if the documents aren't included in your project.

To include evaluation documents, use the `--include-evaluations` flag when creating the portable package, or copy them manually from the source repository.

## Usage

Cursor automatically detects and loads rules from `.cursor/rules/` directory. No additional configuration needed.

When you ask questions in Cursor chat, the agent will:
1. Automatically apply always-applied rules (project overview, Wooldridge references, triangulation guide)
2. Select context-specific rules based on file patterns and relevance
3. Use the guidance system to provide methodology recommendations
4. Query the Wooldridge corpus when relevant

## First Question Tips

When using the agent for the first time, try:
- "What method should I use for my analysis?"
- "Help me choose an econometric method"
- "I have panel data, what methods are appropriate?"

The agent will automatically use the methodology selection system and relevant rules.

**Note**: Rules with `alwaysApply: true` (project-overview, wooldridge-references, triangulation-guide) are always loaded. Context-specific rules (with `globs`) are selected based on file patterns AND conversation context - even if you haven't created any files yet, asking about methodologies will trigger the methodology-selection rule.

