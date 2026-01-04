# Wooldridge Integration Guide

## Overview

This guide explains how the Wooldridge corpus is integrated into the econometrics agent, enabling systematic reference to Wooldridge's methodological perspectives alongside Hansen and Angrist evaluations.

## Architecture

The integration has three main components:

1. **Corpus System**: Analyzes and indexes Wooldridge textbook markdown files
2. **Agent Integration**: Provides functions for the agent to query corpus
3. **Rule Integration**: Embeds Wooldridge references in agent rules

## How It Works

### Corpus Building

The corpus is built from markdown files in `docs/wooldridge_extracts/`:

```bash
python -m src.corpus.cli build
```

This process:
1. Analyzes markdown files to extract methodologies, sections, and perspectives
2. Builds topic-based indices (by methodology, chapter, priority area)
3. Generates vector embeddings for semantic search
4. Creates cross-references to evaluation documents

### Agent Usage

The agent can query the corpus in several ways:

#### 1. Quick Lookup

```python
from src.corpus.agent_helpers import quick_lookup

# Fast perspective lookup
summary = quick_lookup("fixed effects")
```

#### 2. Full Perspective

```python
from src.corpus.agent_integration import get_wooldridge_perspective

# Get Wooldridge's perspective
perspective = get_wooldridge_perspective("clustered standard errors")
formatted = format_perspective_response(perspective)
```

#### 3. Triangulation

```python
from src.corpus.triangulation import triangulate

# Compare all three perspectives
comparison = triangulate("fixed effects")
synthesis = synthesize_recommendation(comparison)
```

#### 4. Semantic Search

```python
from src.corpus.agent_integration import semantic_search_wooldridge

# Flexible search
results = semantic_search_wooldridge("how to handle missing data in panels", top_k=5)
```

## Integration Points

### Rule Files

Rule files (`.cursor/rules/*.mdc`) now include:
- Wooldridge chapter references
- Corpus query examples
- Cross-references to evaluation documents
- Synthesis guidance

Example from `panel-data.mdc`:
```markdown
**Wooldridge Reference: Chapter 23 - Basic Panel Data Models**

**Corpus Query**: Use `get_wooldridge_perspective("fixed effects")` to retrieve Wooldridge's detailed guidance.

**Cross-Reference**: See WOOLDRIDGE_EVALUATION.md:144-162 for comparison with Hansen/Angrist.
```

### Agent Behavior

When the agent discusses methodologies, it should:
1. Query corpus for Wooldridge's perspective (when relevant)
2. Compare with Hansen/Angrist perspectives
3. Provide synthesis that combines all three
4. Cite sources appropriately

### Response Format

Agent responses should follow this pattern:

```
**Wooldridge's Perspective (Chapter X):**
[Wooldridge's recommendation]

**Hansen's Approach:**
[Hansen's position]

**Angrist/MHE Approach:**
[Angrist's position]

**Our Synthesis:**
[Combined recommendation]
```

## When to Reference Wooldridge

### Always Reference For:
- Panel data methods (Wooldridge's expertise - Priority #2)
- Context-appropriate standard errors
- Attrition handling
- Survey weights
- Small-sample corrections

### Consider Referencing For:
- Treatment effects (especially panel treatment effects)
- IV methods (especially panel IV)
- Data handling practices
- Methodology questions

### Don't Over-Reference:
- Basic OLS (unless discussing SE choice)
- Simple diagnostics
- Topics outside Wooldridge's expertise

## Triangulation Framework

The triangulation system compares all three perspectives:

### High Agreement
All three perspectives agree → High confidence recommendation

### Medium Agreement
Two agree, third validates → Medium-high confidence

### Low Agreement
Perspectives differ → Synthesis required, explain differences

## Examples

### Example 1: Panel Data Clustering

**User asks**: "Should I cluster standard errors in panel data?"

**Agent workflow**:
```python
# Query corpus
perspective = get_wooldridge_perspective("clustered standard errors")
comparison = triangulate("clustered standard errors")

# Format response
response = format_triangulation_response(comparison)
```

**Agent response**:
```
Yes, you should cluster standard errors in panel data. All three perspectives agree:

**Wooldridge (Chapter 23)**: Recommends clustered SE with small-sample correction
**Hansen**: Validates clustering when appropriate
**Angrist/MHE**: Uses clustered SE when relevant

**Our approach**: We default to clustered SE with small-sample correction (Wooldridge's approach), validated by Hansen's modern practices.

**Confidence**: High - all three perspectives agree.
```

### Example 2: Standard Error Selection

**User asks**: "What standard errors should I use for my model?"

**Agent workflow**:
```python
# Get context-specific guidance
se_guidance = get_standard_error_guidance("limited_dependent_variable")
comparison = compare_standard_errors("limited_dependent_variable")
```

**Agent response**:
```
For limited dependent variable models, use HC3 (jackknife) standard errors.

**Wooldridge (Chapter 17)**: Consistently uses HC3 for limited dependent variables
**Hansen**: Uses robust SE by default, but supports HC variants
**Our synthesis**: Use HC3 for LDV models (Wooldridge's recommendation), with robust (HC1) as default for other contexts (Hansen's modern practice).

**Corpus Query**: `get_wooldridge_perspective("HC3")` for detailed guidance.
```

## Best Practices

1. **Query corpus when relevant** - Don't hardcode Wooldridge perspectives
2. **Show all three perspectives** - When triangulating, include all three
3. **Provide synthesis** - Always explain how perspectives combine
4. **Cite sources** - Include chapter/page references when available
5. **Link to evaluations** - Cross-reference evaluation documents
6. **Use semantic search** - For flexible queries about concepts
7. **Format consistently** - Use response templates for consistency

## File Locations

- **Corpus data**: `data/corpus/wooldridge_*`
- **Integration code**: `src/corpus/agent_*.py`
- **Rule files**: `.cursor/rules/*.mdc`
- **Evaluation docs**: `WOOLDRIDGE_EVALUATION.md`, `HANSEN_EVALUATION.md`, `ANGRIST_EVALUATION.md`

## Troubleshooting

### Corpus Not Found
If corpus files don't exist, build the corpus:
```bash
python -m src.corpus.cli build
```

### No Results from Query
- Try semantic search instead of exact lookup
- Check methodology name spelling
- Verify corpus was built successfully

### Slow Queries
- Embeddings are loaded on first use (may take a moment)
- Subsequent queries are fast
- Consider caching results for common queries

## Future Enhancements

- Pre-computed triangulation results for common methodologies
- Cached perspective lookups
- Interactive corpus exploration
- Integration with methodology selection system



