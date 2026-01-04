# Wooldridge Corpus Tools

Tools for analyzing and retrieving content from Wooldridge's "Econometric Analysis of Cross Section and Panel Data" textbook.

## Overview

The corpus tools enable:
- **Content Analysis**: Extract structured content, methodologies, and perspectives from markdown files
- **Keyword Search**: Find relevant sections using simple text search
- **Topic Lookup**: Direct access to content by methodology or topic
- **Cross-Referencing**: Link Wooldridge content to Hansen/Angrist evaluations and agent rules

## Components

### WooldridgeAnalyzer
Analyzes markdown files to extract:
- Section headers and hierarchy
- Methodological concepts
- Mathematical equations
- Wooldridge's perspectives and recommendations

### WooldridgeIndexer
Builds structured indices:
- By methodology (fixed effects, IV, etc.)
- By topic category (panel_data, causal_inference, etc.)
- By priority area
- Cross-references to evaluation documents and agent rules

### WooldridgeSearch
Provides simple keyword-based search and retrieval:
- Keyword search with relevance scoring
- Topic-based lookup
- Perspective finding
- Methodology-specific guidance

## Usage

### Building the Index

```bash
python -m src.corpus.cli build-index
```

This will:
1. Analyze all markdown files in `docs/wooldridge_extracts/`
2. Build topic indices
3. Create cross-references
4. Save everything to `data/corpus/wooldridge_index/`

Note: No embeddings are generated - the system uses simple markdown search.

### Searching the Corpus

```bash
# Keyword search
python -m src.corpus.cli search "fixed effects panel data" --top-k 5

# Topic lookup
python -m src.corpus.cli lookup "fixed effects" --limit 10

# Find Wooldridge's perspective
python -m src.corpus.cli perspective "clustered standard errors" --limit 5

# Compare with Hansen/Angrist
python -m src.corpus.cli compare "fixed effects"
```

### Programmatic Usage

```python
from src.corpus import WooldridgeSearch

# Initialize search
searcher = WooldridgeSearch()

# Keyword search
results = searcher.search_wooldridge("fixed effects estimation", top_k=5)

# Get chapter content
chapter = searcher.get_chapter("panel data")

# Get methodology guidance
guidance = searcher.get_methodology_guidance("clustered standard errors")
```

## File Structure

```
data/corpus/
└── wooldridge_index/
    ├── index.json                # Topic indices
    ├── cross_references.json     # Cross-reference mappings
    ├── analysis.json             # Raw analysis results
    └── methodology_map.json      # Methodology to agent mapping
```

## Integration with Agent

The corpus enables the agent to:
- Reference Wooldridge's methodological perspectives
- Compare approaches across Hansen, Angrist, and Wooldridge
- Retrieve relevant textbook sections for methodology questions
- Support triangulation analysis

## Dependencies

- Standard library only: `json`, `pathlib`, `re`
- No heavy ML dependencies needed

## Notes

- Uses simple keyword matching and section headers, not vector similarity
- Fast and lightweight - no model loading required
- Search is based on exact and partial keyword matches
- Results are ranked by keyword frequency and title matches


