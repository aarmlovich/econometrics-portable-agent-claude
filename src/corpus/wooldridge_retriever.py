"""Retrieval interface for Wooldridge corpus."""

import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional
from src.corpus.wooldridge_embeddings import WooldridgeEmbeddings
from src.corpus.wooldridge_index import WooldridgeIndexer


class WooldridgeRetriever:
    """Search and retrieve Wooldridge textbook content."""

    def __init__(
        self,
        embeddings_path: Optional[Path] = None,
        index_path: Optional[Path] = None,
        cross_refs_path: Optional[Path] = None,
        project_root: Optional[Path] = None,
    ):
        """Initialize retriever with embeddings and indices.
        
        Args:
            embeddings_path: Path to embeddings JSON file
            index_path: Path to topic index JSON file
            cross_refs_path: Path to cross-references JSON file
            project_root: Path to project root (for loading indices)
        """
        if project_root is None:
            self.project_root = Path(".")
        else:
            self.project_root = Path(project_root)

        # Default paths
        if embeddings_path is None:
            embeddings_path = (
                self.project_root
                / "data"
                / "corpus"
                / "wooldridge_embeddings"
                / "embeddings.json"
            )
        if index_path is None:
            index_path = (
                self.project_root
                / "data"
                / "corpus"
                / "wooldridge_index"
                / "index.json"
            )
        if cross_refs_path is None:
            cross_refs_path = (
                self.project_root
                / "data"
                / "corpus"
                / "wooldridge_index"
                / "cross_references.json"
            )

        self.embeddings_path = Path(embeddings_path)
        self.index_path = Path(index_path)
        self.cross_refs_path = Path(cross_refs_path)

        # Load data
        self.embeddings = None
        self.index = None
        self.cross_refs = None
        self.embedding_model = None

        self._load_data()

    def _load_data(self) -> None:
        """Load embeddings, index, and cross-references."""
        if self.embeddings_path.exists():
            with open(self.embeddings_path, "r", encoding="utf-8") as f:
                self.embeddings = json.load(f)
            print(f"Loaded {len(self.embeddings)} embeddings")
        else:
            print(f"Warning: Embeddings file not found: {self.embeddings_path}")

        if self.index_path.exists():
            with open(self.index_path, "r", encoding="utf-8") as f:
                self.index = json.load(f)
            print(f"Loaded index with {len(self.index.get('by_methodology', {}))} methodologies")
        else:
            print(f"Warning: Index file not found: {self.index_path}")

        if self.cross_refs_path.exists():
            with open(self.cross_refs_path, "r", encoding="utf-8") as f:
                self.cross_refs = json.load(f)
            print(f"Loaded cross-references for {len(self.cross_refs)} methodologies")
        else:
            print(f"Warning: Cross-references file not found: {self.cross_refs_path}")

    def semantic_search(
        self, query: str, top_k: int = 5
    ) -> List[Dict]:
        """Vector similarity search for relevant Wooldridge sections.
        
        Args:
            query: Search query text
            top_k: Number of results to return
            
        Returns:
            List of result dictionaries with:
                - content: Matching content
                - metadata: Source metadata
                - relevance_score: Similarity score
        """
        if self.embeddings is None:
            raise RuntimeError(
                "Embeddings not loaded. Build corpus first or check embeddings_path."
            )

        # Initialize embedding model if needed
        if self.embedding_model is None:
            self.embedding_model = WooldridgeEmbeddings()
            # Ensure model is loaded
            if self.embedding_model.model is None:
                self.embedding_model._load_model()

        # Generate query embedding
        query_embedding = self.embedding_model.model.encode(
            query, convert_to_numpy=True
        )

        # Compute similarities
        similarities = []
        for chunk in self.embeddings:
            chunk_embedding = np.array(chunk["embedding"])
            similarity = self._cosine_similarity(query_embedding, chunk_embedding)
            similarities.append((similarity, chunk))

        # Sort by similarity and return top_k
        similarities.sort(key=lambda x: x[0], reverse=True)

        results = []
        for score, chunk in similarities[:top_k]:
            results.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"],
                "relevance_score": float(score),
            })

        return results

    def lookup_topic(self, topic: str) -> Dict:
        """Direct topic-based retrieval.
        
        Args:
            topic: Topic name (e.g., "fixed effects", "panel_data", "causal_inference")
            
        Returns:
            Dictionary with topic information and related content
        """
        if self.index is None:
            raise RuntimeError(
                "Index not loaded. Build corpus first or check index_path."
            )

        result = {
            "topic": topic,
            "methodologies": [],
            "sections": [],
            "priority": None,
        }

        # Check if topic is a methodology
        if topic in self.index.get("by_methodology", {}):
            result["methodologies"] = self.index["by_methodology"][topic]
            result["type"] = "methodology"

        # Check if topic is a category
        if topic in self.index.get("by_topic", {}):
            result["sections"] = self.index["by_topic"][topic]
            result["type"] = "category"

        # Check if topic is a priority area
        if topic in self.index.get("by_priority", {}):
            result["priority"] = self.index["by_priority"][topic]
            result["type"] = "priority"

        return result

    def find_perspective(self, methodology: str) -> Dict:
        """Get Wooldridge's perspective on a specific methodology.
        
        Args:
            methodology: Methodology name (e.g., "fixed effects", "clustered standard errors")
            
        Returns:
            Dictionary with Wooldridge's perspective and recommendations
        """
        if self.index is None:
            raise RuntimeError(
                "Index not loaded. Build corpus first or check index_path."
            )

        result = {
            "methodology": methodology,
            "wooldridge_perspective": None,
            "sections": [],
            "cross_references": {},
        }

        # Find in index
        if methodology in self.index.get("by_methodology", {}):
            result["sections"] = self.index["by_methodology"][methodology]

        # Find cross-references
        if self.cross_refs and methodology in self.cross_refs:
            result["cross_references"] = self.cross_refs[methodology]

        # Try to extract perspective from sections
        perspectives = []
        for section in result["sections"]:
            context = section.get("context", "")
            # Look for recommendation language
            if any(
                word in context.lower()
                for word in ["should", "recommend", "prefer", "best practice"]
            ):
                perspectives.append({
                    "context": context,
                    "section": section.get("section"),
                    "page": section.get("page"),
                })

        if perspectives:
            result["wooldridge_perspective"] = perspectives

        return result

    def cross_reference(
        self, methodology: str
    ) -> Dict:
        """Get Wooldridge + Hansen + Angrist perspectives on a methodology.
        
        Args:
            methodology: Methodology name
            
        Returns:
            Dictionary with perspectives from all three sources
        """
        wooldridge = self.find_perspective(methodology)

        result = {
            "methodology": methodology,
            "wooldridge": {
                "sections": wooldridge["sections"],
                "perspective": wooldridge["wooldridge_perspective"],
            },
            "hansen": None,
            "angrist": None,
            "synthesis": None,
        }

        # Get cross-references
        if self.cross_refs and methodology in self.cross_refs:
            cross_ref = self.cross_refs[methodology]

            if cross_ref.get("hansen_evaluation"):
                result["hansen"] = cross_ref["hansen_evaluation"]

            if cross_ref.get("angrist_evaluation"):
                result["angrist"] = cross_ref["angrist_evaluation"]

            if cross_ref.get("wooldridge_evaluation"):
                result["wooldridge"]["evaluation"] = cross_ref[
                    "wooldridge_evaluation"
                ]

            result["agent_rules"] = cross_ref.get("agent_rules", [])

        return result

    def _cosine_similarity(
        self, vec1: np.ndarray, vec2: np.ndarray
    ) -> float:
        """Compute cosine similarity between two vectors."""
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return float(dot_product / (norm1 * norm2))

    def search_by_section(
        self, section_title: str, limit: int = 10
    ) -> List[Dict]:
        """Search for content by section title.
        
        Args:
            section_title: Section title to search for
            limit: Maximum number of results
            
        Returns:
            List of matching sections
        """
        if self.index is None:
            raise RuntimeError(
                "Index not loaded. Build corpus first or check index_path."
            )

        results = []
        section_title_lower = section_title.lower()

        for title, sections in self.index.get("by_chapter", {}).items():
            if section_title_lower in title.lower():
                results.extend(sections[:limit])

        return results[:limit]

