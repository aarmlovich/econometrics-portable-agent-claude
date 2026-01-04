"""Embedding generation for Wooldridge corpus."""

import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional
import re


class WooldridgeEmbeddings:
    """Generate and manage embeddings for Wooldridge corpus."""

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        use_local: bool = True,
    ):
        """Initialize embedding generator.
        
        Args:
            model_name: Name of embedding model to use
            use_local: If True, use sentence-transformers (local).
                      If False, use OpenAI API (requires API key)
        """
        self.model_name = model_name
        self.use_local = use_local
        self.model = None
        self._load_model()

    def _load_model(self) -> None:
        """Load embedding model."""
        if self.use_local:
            try:
                from sentence_transformers import SentenceTransformer

                self.model = SentenceTransformer(self.model_name)
                print(f"Loaded local embedding model: {self.model_name}")
            except ImportError:
                raise ImportError(
                    "sentence-transformers not installed. "
                    "Install with: pip install sentence-transformers"
                )
        else:
            # OpenAI embeddings would be loaded here
            # For now, we'll use local by default
            raise NotImplementedError(
                "OpenAI embeddings not yet implemented. Use use_local=True"
            )

    def chunk_content(
        self, content: str, metadata: Dict, chunk_size: int = 500, overlap: int = 50
    ) -> List[Dict]:
        """Split content into semantically meaningful chunks.
        
        Args:
            content: Text content to chunk
            metadata: Metadata dictionary (file_name, section, page, etc.)
            chunk_size: Target chunk size in characters
            overlap: Overlap between chunks in characters
            
        Returns:
            List of chunk dictionaries with content and metadata
        """
        chunks = []

        # First, try to chunk by paragraphs
        paragraphs = content.split("\n\n")
        current_chunk = ""
        current_chunk_metadata = metadata.copy()

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # If adding this paragraph would exceed chunk size, save current chunk
            if current_chunk and len(current_chunk) + len(para) > chunk_size:
                if current_chunk:
                    chunks.append({
                        "content": current_chunk.strip(),
                        "metadata": current_chunk_metadata.copy(),
                    })
                # Start new chunk with overlap
                overlap_text = current_chunk[-overlap:] if len(current_chunk) > overlap else ""
                current_chunk = overlap_text + para
            else:
                if current_chunk:
                    current_chunk += "\n\n" + para
                else:
                    current_chunk = para

        # Add final chunk
        if current_chunk:
            chunks.append({
                "content": current_chunk.strip(),
                "metadata": current_chunk_metadata.copy(),
            })

        # If paragraphs are too long, split by sentences
        refined_chunks = []
        for chunk in chunks:
            if len(chunk["content"]) > chunk_size * 2:
                # Split by sentences
                sentences = re.split(r"[.!?]+\s+", chunk["content"])
                current = ""
                for sent in sentences:
                    if len(current) + len(sent) > chunk_size:
                        if current:
                            refined_chunk = chunk.copy()
                            refined_chunk["content"] = current.strip()
                            refined_chunks.append(refined_chunk)
                        current = sent
                    else:
                        current += " " + sent if current else sent
                if current:
                    refined_chunk = chunk.copy()
                    refined_chunk["content"] = current.strip()
                    refined_chunks.append(refined_chunk)
            else:
                refined_chunks.append(chunk)

        return refined_chunks

    def generate_embeddings(self, chunks: List[Dict]) -> List[Dict]:
        """Create vector embeddings for content chunks.
        
        Args:
            chunks: List of chunk dictionaries with 'content' and 'metadata'
            
        Returns:
            List of dictionaries with embeddings added:
                - content: Original content
                - metadata: Original metadata
                - embedding: numpy array of embedding vector
                - embedding_dim: Dimension of embedding
        """
        if self.model is None:
            raise RuntimeError("Model not loaded. Call _load_model() first.")

        # Extract texts
        texts = [chunk["content"] for chunk in chunks]

        # Generate embeddings
        print(f"Generating embeddings for {len(texts)} chunks...")
        embeddings = self.model.encode(
            texts, show_progress_bar=True, convert_to_numpy=True
        )

        # Add embeddings to chunks
        result = []
        for i, chunk in enumerate(chunks):
            result.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"],
                "embedding": embeddings[i].tolist(),  # Convert to list for JSON
                "embedding_dim": len(embeddings[i]),
            })

        return result

    def process_analyzed_content(
        self, analyzed_content: List[Dict]
    ) -> List[Dict]:
        """Process analyzed content from WooldridgeAnalyzer into embedded chunks.
        
        Args:
            analyzed_content: List of analysis results from WooldridgeAnalyzer
            
        Returns:
            List of embedded chunks with full metadata
        """
        all_chunks = []

        for file_analysis in analyzed_content:
            file_name = file_analysis["file_name"]
            file_path = file_analysis["file_path"]

            # Process each section
            for section in file_analysis["sections"]:
                if not section.get("content"):
                    continue

                section_metadata = {
                    "file_name": file_name,
                    "file_path": file_path,
                    "section_title": section.get("title", ""),
                    "section_level": section.get("level", 0),
                    "page": section.get("page"),
                    "page_range": file_analysis.get("page_range"),
                    "is_priority": file_analysis.get("is_priority", False),
                    "priority_reason": file_analysis.get("priority_reason"),
                }

                # Chunk section content
                chunks = self.chunk_content(
                    section["content"], section_metadata
                )

                # Generate embeddings for chunks
                embedded_chunks = self.generate_embeddings(chunks)
                all_chunks.extend(embedded_chunks)

        return all_chunks

    def save_embeddings(
        self, embeddings: List[Dict], output_path: Path
    ) -> None:
        """Persist embeddings to disk.
        
        Args:
            embeddings: List of embedded chunk dictionaries
            output_path: Path to save JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save as JSON (embeddings are already lists)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(embeddings, f, indent=2, ensure_ascii=False)

        print(
            f"Saved {len(embeddings)} embeddings to {output_path} "
            f"({len(embeddings[0]['embedding']) if embeddings else 0} dimensions)"
        )

    def load_embeddings(self, input_path: Path) -> List[Dict]:
        """Load embeddings from disk.
        
        Args:
            input_path: Path to JSON file with embeddings
            
        Returns:
            List of embedded chunk dictionaries
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Embeddings file not found: {input_path}")

        with open(input_path, "r", encoding="utf-8") as f:
            embeddings = json.load(f)

        print(f"Loaded {len(embeddings)} embeddings from {input_path}")
        return embeddings

    def compute_similarity(
        self, embedding1: List[float], embedding2: List[float]
    ) -> float:
        """Compute cosine similarity between two embeddings.
        
        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector
            
        Returns:
            Cosine similarity score (0-1)
        """
        vec1 = np.array(embedding1)
        vec2 = np.array(embedding2)

        # Cosine similarity
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return float(dot_product / (norm1 * norm2))



