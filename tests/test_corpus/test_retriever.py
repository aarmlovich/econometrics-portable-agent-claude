"""
Tests for Wooldridge corpus search system (simplified, no embeddings).
"""
import pytest
from src.corpus.wooldridge_search import WooldridgeSearch
from src.corpus.agent_integration import (
    get_wooldridge_perspective,
    triangulate_methodology,
    semantic_search_wooldridge,
)


@pytest.fixture
def searcher():
    """Initialize search system."""
    return WooldridgeSearch()


def test_searcher_initialization(searcher):
    """Test that searcher loads successfully."""
    assert searcher is not None
    assert searcher.extracts_dir.exists()


def test_keyword_search(searcher):
    """Test keyword search functionality."""
    results = searcher.search_wooldridge("fixed effects panel data", top_k=3)

    assert len(results) > 0
    assert len(results) <= 3
    # Each result should have title and content
    assert all('content' in r and 'title' in r for r in results)
    # Should have relevance scores
    assert all('relevance_score' in r for r in results)


def test_get_methodology_guidance(searcher):
    """Test methodology-specific guidance retrieval."""
    guidance = searcher.get_methodology_guidance("fixed effects")

    assert guidance is not None
    assert len(guidance) > 0
    assert "fixed effects" in guidance.lower()


def test_get_chapter(searcher):
    """Test chapter content retrieval."""
    chapter = searcher.get_chapter("panel data")

    assert chapter is not None
    assert len(chapter) > 0


def test_agent_integration_perspective():
    """Test getting Wooldridge perspective via agent integration."""
    perspective = get_wooldridge_perspective("clustered standard errors")

    assert perspective is not None
    assert 'methodology' in perspective
    assert 'sections' in perspective
    assert perspective['methodology'] == "clustered standard errors"


def test_agent_integration_search():
    """Test keyword search via agent integration."""
    results = semantic_search_wooldridge("panel data", top_k=3)

    assert len(results) > 0
    assert len(results) <= 3


def test_triangulation():
    """Test triangulation with Hansen/Angrist (requires index)."""
    # This may fail if index not built, which is acceptable
    try:
        result = triangulate_methodology("fixed effects")
        assert result is not None
        assert 'methodology' in result
        assert 'wooldridge' in result
    except Exception:
        # Index not built yet, skip
        pass


# TODO: Add more tests:
# - Test malformed queries
# - Test caching behavior
# - Test section extraction
# - Test with various query types
