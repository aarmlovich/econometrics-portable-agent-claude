# Wooldridge Corpus Tools

Tools for analyzing and retrieving content from Wooldridge's "Econometric Analysis of Cross Section and Panel Data" textbook.

## Overview

The corpus tools enable:
- **Content Analysis**: Extract structured content, methodologies, and perspectives from markdown files
- **Semantic Search**: Find relevant sections using vector embeddings
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

### WooldridgeEmbeddings
Generates vector embeddings for semantic search:
- Chunks content into searchable segments
- Creates embeddings using sentence-transformers
- Stores embeddings with metadata

### WooldridgeRetriever
Provides search and retrieval interfaces:
- Semantic search via vector similarity
- Topic-based lookup
- Perspective finding
- Cross-reference queries

## Usage

### Building the Corpus

```bash
python -m src.corpus.cli build
```

This will:
1. Analyze all markdown files in `docs/wooldridge_extracts/`
2. Build topic indices
3. Create cross-references
4. Generate embeddings
5. Save everything to `data/corpus/`

### Searching the Corpus

```bash
# Semantic search
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
from src.corpus import WooldridgeRetriever

# Initialize retriever
retriever = WooldridgeRetriever()

# Semantic search
results = retriever.semantic_search("fixed effects estimation", top_k=5)

# Topic lookup
topic_info = retriever.lookup_topic("panel_data")

# Find perspective
perspective = retriever.find_perspective("clustered standard errors")

# Cross-reference
comparison = retriever.cross_reference("fixed effects")
```

## File Structure

```
data/corpus/
├── wooldridge_embeddings/
│   └── embeddings.json          # Vector embeddings
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

- `sentence-transformers`: For generating embeddings (local, no API required)
- `numpy`: For vector operations
- Standard library: `json`, `pathlib`, `re`

## Notes

- Embeddings use the `all-MiniLM-L6-v2` model by default (384 dimensions)
- Corpus build time depends on number of markdown files (~80+ files)
- Embeddings are stored as JSON (can be large, consider compression for production)



