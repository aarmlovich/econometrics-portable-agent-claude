"""Shared utilities for corpus tools."""

from pathlib import Path
from typing import Optional


def get_default_paths(project_root: Optional[Path] = None) -> dict:
    """Get default paths for corpus data.
    
    Args:
        project_root: Path to project root. Defaults to current directory.
        
    Returns:
        Dictionary with default paths
    """
    if project_root is None:
        project_root = Path(".")

    return {
        "extracts_dir": project_root / "docs" / "wooldridge_extracts",
        "index_dir": project_root / "data" / "corpus" / "wooldridge_index",
        "index_file": project_root / "data" / "corpus" / "wooldridge_index" / "index.json",
        "cross_refs_file": project_root / "data" / "corpus" / "wooldridge_index" / "cross_references.json",
        "analysis_file": project_root / "data" / "corpus" / "wooldridge_index" / "analysis.json",
        "methodology_map_file": project_root / "data" / "corpus" / "wooldridge_index" / "methodology_map.json",
    }



