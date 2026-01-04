"""Simple markdown-based search for Wooldridge corpus.

This module provides simple keyword-based search of Wooldridge markdown files,
replacing the complex embedding/RAG pipeline with straightforward text search.

Supports two markdown formats:
1. Old format (docs/wooldridge_extracts/): Part-based files with ## headers
2. New format (docs/wooldridge_textbook/): Page-range files with {page}--- markers
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


def _get_repo_root() -> Path:
    """Get repository root using relative path from this module."""
    # This file: src/corpus/wooldridge_search.py
    # Repo root: ../../
    return Path(__file__).parent.parent.parent


def _get_default_textbook_path() -> Path:
    """Get default path to Wooldridge textbook markdowns (portable)."""
    return _get_repo_root() / "docs" / "wooldridge_textbook"


def _get_legacy_extracts_path() -> Path:
    """Get path to legacy extracts (for backward compatibility)."""
    return _get_repo_root() / "docs" / "wooldridge_extracts"


class WooldridgeSearch:
    """Simple search interface for Wooldridge textbook content.

    Supports both the new page-range markdown format and legacy part-based format.
    """

    # Regex to match new page marker format: {241}------------------------------------------------
    PAGE_MARKER_PATTERN = re.compile(r'^\{(\d+)\}-+$')

    def __init__(self, extracts_dir: Optional[Path] = None, use_new_textbook: bool = True):
        """Initialize search with path to markdown files.

        Args:
            extracts_dir: Path to directory containing markdown files.
                         If None, uses default path based on use_new_textbook.
            use_new_textbook: If True (default), use docs/wooldridge_textbook/
                             If False, use docs/wooldridge_extracts/ (legacy)
        """
        if extracts_dir is None:
            if use_new_textbook:
                self.extracts_dir = _get_default_textbook_path()
            else:
                self.extracts_dir = _get_legacy_extracts_path()
        else:
            self.extracts_dir = Path(extracts_dir)

        # Try new textbook path, fall back to legacy if not found
        if not self.extracts_dir.exists():
            legacy_path = _get_legacy_extracts_path()
            if legacy_path.exists():
                self.extracts_dir = legacy_path
            else:
                raise FileNotFoundError(
                    f"Wooldridge content not found. Checked:\n"
                    f"  - {self.extracts_dir}\n"
                    f"  - {legacy_path}"
                )

        self.use_new_format = self._detect_format()

        # Cache for loaded content
        self._content_cache = {}
        self._section_index = None

    def _detect_format(self) -> bool:
        """Detect if using new page-range format or legacy format."""
        # Check for page-range files (pages_1-10.md, etc.)
        page_files = list(self.extracts_dir.glob('pages_*.md'))
        return len(page_files) > 0

    def _extract_page_number(self, line: str) -> Optional[int]:
        """Extract page number from new format marker.

        Args:
            line: Line to check for page marker

        Returns:
            Page number if found, None otherwise
        """
        match = self.PAGE_MARKER_PATTERN.match(line.strip())
        return int(match.group(1)) if match else None

    def _load_markdown_file(self, file_path: Path) -> str:
        """Load markdown file content."""
        if file_path not in self._content_cache:
            with open(file_path, 'r', encoding='utf-8') as f:
                self._content_cache[file_path] = f.read()
        return self._content_cache[file_path]

    def _extract_sections(self, content: str, file_name: str) -> List[Dict]:
        """Extract sections from markdown content.

        Handles both old format (## headers) and new format ({page}--- markers).

        Args:
            content: Markdown content
            file_name: Name of the file

        Returns:
            List of section dictionaries with title, content, page info, and metadata
        """
        sections = []

        # Split by headers (## or ###)
        header_pattern = r'^(#{2,3})\s+(.+)$'
        lines = content.split('\n')

        current_section = None
        current_content = []
        current_page = None  # Track page numbers for new format

        for line in lines:
            # Check for page marker in new format
            page_num = self._extract_page_number(line)
            if page_num is not None:
                current_page = page_num
                continue  # Don't include page marker in content

            header_match = re.match(header_pattern, line)
            if header_match:
                # Save previous section
                if current_section:
                    section_data = {
                        'title': current_section['title'],
                        'level': current_section['level'],
                        'content': '\n'.join(current_content).strip(),
                        'file_name': file_name,
                    }
                    # Add page info if available
                    if current_section.get('page_start'):
                        section_data['page_start'] = current_section['page_start']
                        section_data['page_end'] = current_page or current_section['page_start']
                    sections.append(section_data)

                # Start new section
                level = len(header_match.group(1))
                title = header_match.group(2).strip()
                current_section = {
                    'title': title,
                    'level': level,
                    'page_start': current_page
                }
                current_content = []
            else:
                current_content.append(line)

        # Add final section
        if current_section:
            section_data = {
                'title': current_section['title'],
                'level': current_section['level'],
                'content': '\n'.join(current_content).strip(),
                'file_name': file_name,
            }
            if current_section.get('page_start'):
                section_data['page_start'] = current_section['page_start']
                section_data['page_end'] = current_page or current_section['page_start']
            sections.append(section_data)

        return sections

    def _build_section_index(self) -> Dict:
        """Build index of all sections in markdown files.

        Returns:
            Dictionary mapping section titles to content
        """
        if self._section_index is not None:
            return self._section_index

        index = defaultdict(list)

        all_files = []

        if self.use_new_format:
            # New format: page-range files (pages_1-10.md, pages_11-20.md, etc.)
            # Sort by starting page number for proper ordering
            page_files = list(self.extracts_dir.glob('pages_*.md'))

            def extract_start_page(path: Path) -> int:
                """Extract starting page number from filename."""
                name = path.stem  # e.g., "pages_1-10"
                try:
                    start = name.replace('pages_', '').split('-')[0]
                    return int(start)
                except (ValueError, IndexError):
                    return 0

            page_files.sort(key=extract_start_page)
            all_files = page_files

            # Also check for merged file as fallback
            merged_file = self.extracts_dir / 'Wooldridge Panel & Timeseries Markdowns-merged.md'
            if merged_file.exists() and not page_files:
                all_files = [merged_file]
        else:
            # Legacy format: part-based files
            priority_files = [
                'full_textbook.md',
                'part6_panel_data.md',
                'part2_iv_gmm.md',
                'part4_nonlinear.md',
                'part5_nonlinear_models.md',
            ]

            for priority_file in priority_files:
                file_path = self.extracts_dir / priority_file
                if file_path.exists():
                    all_files.append(file_path)

            # Add other markdown files
            for file_path in self.extracts_dir.glob('*.md'):
                if file_path.name not in priority_files and file_path.name != 'extraction_log.md':
                    all_files.append(file_path)

        # Build index
        for file_path in all_files:
            content = self._load_markdown_file(file_path)
            sections = self._extract_sections(content, file_path.name)

            for section in sections:
                # Index by title (lowercase for matching)
                title_key = section['title'].lower()
                index[title_key].append(section)

                # Also index by keywords in title
                keywords = re.findall(r'\w+', title_key)
                for keyword in keywords:
                    if len(keyword) > 3:  # Skip short words
                        index[keyword].append(section)

        self._section_index = dict(index)
        return self._section_index

    def search_wooldridge(self, query: str, top_k: int = 5) -> List[Dict]:
        """Simple keyword search of Wooldridge markdown files.

        Args:
            query: Search query (keywords)
            top_k: Number of results to return

        Returns:
            List of result dictionaries with:
                - title: Section title
                - content: Section content
                - file_name: Source file
                - relevance_score: Simple relevance score
        """
        index = self._build_section_index()

        # Extract keywords from query
        query_lower = query.lower()
        keywords = re.findall(r'\w+', query_lower)
        keywords = [k for k in keywords if len(k) > 3]

        # Score sections by keyword matches
        section_scores = defaultdict(float)
        section_data = {}

        for keyword in keywords:
            # Exact keyword matches
            if keyword in index:
                for section in index[keyword]:
                    section_key = (section['file_name'], section['title'])
                    section_scores[section_key] += 1.0
                    section_data[section_key] = section

            # Partial keyword matches in content
            for title_key, sections in index.items():
                if keyword in title_key:
                    for section in sections:
                        section_key = (section['file_name'], section['title'])
                        # Higher score for title matches
                        section_scores[section_key] += 2.0
                        section_data[section_key] = section

        # Also search in content
        for section_key, section in section_data.items():
            content_lower = section['content'].lower()
            for keyword in keywords:
                # Count keyword occurrences in content
                count = content_lower.count(keyword)
                section_scores[section_key] += count * 0.5

        # Sort by score and return top_k
        sorted_sections = sorted(
            section_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        results = []
        for section_key, score in sorted_sections:
            section = section_data[section_key]
            result = {
                'title': section['title'],
                'content': section['content'][:500],  # Truncate for preview
                'file_name': section['file_name'],
                'relevance_score': score,
                'metadata': {
                    'file_name': section['file_name'],
                    'section_title': section['title'],
                }
            }
            # Add page citations if available (new format)
            if 'page_start' in section:
                result['page_start'] = section['page_start']
                result['page_end'] = section.get('page_end', section['page_start'])
                result['citation'] = f"Wooldridge, p.{section['page_start']}"
                if section.get('page_end') and section['page_end'] != section['page_start']:
                    result['citation'] = f"Wooldridge, p.{section['page_start']}-{section['page_end']}"
            results.append(result)

        return results

    def get_chapter(self, topic: str) -> str:
        """Return relevant chapter content for a topic.

        Args:
            topic: Topic name (e.g., "panel data", "fixed effects")

        Returns:
            Chapter content as markdown string
        """
        topic_lower = topic.lower()

        if self.use_new_format:
            # New format: use search to find relevant sections with page numbers
            # Topic to approximate page ranges (Wooldridge 2nd ed)
            topic_pages = {
                'panel': (247, 340),        # Ch 10-11
                'fixed effects': (263, 297),
                'random effects': (257, 265),
                'hausman': (291, 300),
                'instrumental variables': (83, 140),  # Ch 5-6
                'iv': (83, 113),
                '2sls': (90, 100),
                'gmm': (195, 240),          # Ch 8
                'weak instruments': (101, 103),
                'probit': (453, 490),       # Ch 15
                'logit': (453, 490),
                'tobit': (525, 540),        # Ch 16
                'nonlinear': (453, 550),
            }

            # Search for the topic
            results = self.search_wooldridge(topic, top_k=5)
            if results:
                output_parts = []
                for r in results:
                    citation = r.get('citation', r['file_name'])
                    output_parts.append(f"## {r['title']} ({citation})\n{r['content']}")
                return '\n\n'.join(output_parts)

            return f"No chapter content found for: {topic}"
        else:
            # Legacy format: map topics to file names
            topic_files = {
                'panel': 'part6_panel_data.md',
                'fixed effects': 'part6_panel_data.md',
                'random effects': 'part6_panel_data.md',
                'instrumental variables': 'part2_iv_gmm.md',
                'iv': 'part2_iv_gmm.md',
                'gmm': 'part2_iv_gmm.md',
                'nonlinear': 'part4_nonlinear.md',
                'limited dependent': 'part5_nonlinear_models.md',
                'probit': 'part5_nonlinear_models.md',
                'logit': 'part5_nonlinear_models.md',
                'tobit': 'part5_nonlinear_models.md',
            }

            # Find matching file
            file_name = None
            for key, fname in topic_files.items():
                if key in topic_lower:
                    file_name = fname
                    break

            if file_name is None:
                file_name = 'full_textbook.md'

            file_path = self.extracts_dir / file_name
            if not file_path.exists():
                return f"Chapter file not found: {file_name}"

            content = self._load_markdown_file(file_path)
            sections = self._extract_sections(content, file_name)

            # Find sections matching the topic
            relevant_sections = []
            for section in sections:
                if topic_lower in section['title'].lower():
                    relevant_sections.append(section)

            if not relevant_sections:
                return '\n\n'.join([
                    f"## {s['title']}\n{s['content'][:300]}..."
                    for s in sections[:3]
                ])

            return '\n\n'.join([
                f"## {s['title']}\n{s['content']}"
                for s in relevant_sections[:5]
            ])

    def get_methodology_guidance(self, method: str) -> str:
        """Get method-specific guidance from Wooldridge.

        Args:
            method: Methodology name (e.g., "fixed effects", "clustered standard errors")

        Returns:
            Guidance text specific to the methodology
        """
        # Search for the methodology
        results = self.search_wooldridge(method, top_k=3)

        if not results:
            return f"No specific guidance found for: {method}"

        # Format results as guidance
        guidance_parts = [f"Wooldridge on {method}:\n"]

        for i, result in enumerate(results, 1):
            guidance_parts.append(f"\n{i}. {result['title']}")
            # Include page citation if available
            if 'citation' in result:
                guidance_parts.append(f"   Reference: {result['citation']}")
            else:
                guidance_parts.append(f"   Source: {result['file_name']}")
            guidance_parts.append(f"   {result['content'][:300]}...")

        return '\n'.join(guidance_parts)


# Convenience functions for backwards compatibility

def search_wooldridge(query: str, top_k: int = 5) -> List[Dict]:
    """Simple grep/keyword search of markdown files.

    Args:
        query: Search query
        top_k: Number of results to return

    Returns:
        List of result dictionaries
    """
    searcher = WooldridgeSearch()
    return searcher.search_wooldridge(query, top_k)


def get_chapter(topic: str) -> str:
    """Return relevant chapter content.

    Args:
        topic: Topic name

    Returns:
        Chapter content
    """
    searcher = WooldridgeSearch()
    return searcher.get_chapter(topic)


def get_methodology_guidance(method: str) -> str:
    """Method-specific guidance.

    Args:
        method: Methodology name

    Returns:
        Guidance text
    """
    searcher = WooldridgeSearch()
    return searcher.get_methodology_guidance(method)
