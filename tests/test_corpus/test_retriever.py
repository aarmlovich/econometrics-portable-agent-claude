"""
Tests for Wooldridge corpus retrieval system.
"""
import pytest
from src.corpus.wooldridge_retriever import WooldridgeRetriever


@pytest.fixture
def retriever():
    """Initialize retriever (will load embeddings and index)."""
    return WooldridgeRetriever()


def test_retriever_initialization(retriever):
    """Test that retriever loads successfully."""
    assert retriever is not None
    # Check that embeddings and index are loaded
    assert hasattr(retriever, 'embeddings') or hasattr(retriever, '_embeddings')


def test_semantic_search(retriever):
    """Test semantic search functionality."""
    results = retriever.semantic_search("fixed effects panel data", top_k=3)

    assert len(results) > 0
    assert len(results) <= 3
    # Each result should have content and metadata
    assert all('content' in r or 'text' in r for r in results)


def test_find_perspective(retriever):
    """Test finding Wooldridge's perspective on a methodology."""
    perspective = retriever.find_perspective("fixed effects")

    assert perspective is not None
    # Should contain Wooldridge's guidance on fixed effects


def test_cross_reference(retriever):
    """Test cross-referencing with Hansen/Angrist evaluations."""
    cross_ref = retriever.cross_reference("clustered standard errors")

    assert cross_ref is not None
    # Should link to evaluation documents


# TODO: Add more tests:
# - Test topic lookup
# - Test chapter mappings
# - Test malformed queries
# - Test caching behavior
