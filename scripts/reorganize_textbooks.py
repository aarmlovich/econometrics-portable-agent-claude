#!/usr/bin/env python3
"""Reorganize textbook markdown files by TOC section instead of page ranges.

Transforms page-range files (pages_1-20.md) into section-based files
(ch03_1_regression_fundamentals.md) for semantic searchability.
"""

import re
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Section:
    """Represents a textbook section."""
    chapter: int
    section: Optional[float]  # e.g., 3.1, 3.2, None for chapter intro
    title: str
    content: str
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    level: int = 2  # ## = 2, ### = 3, #### = 4
    subsections: list = field(default_factory=list)


def get_repo_root() -> Path:
    """Get repository root."""
    return Path(__file__).parent.parent


def extract_page_number(line: str) -> Optional[int]:
    """Extract page number from marker like {123}---."""
    match = re.match(r'^\{(\d+)\}-+$', line.strip())
    return int(match.group(1)) if match else None


def parse_header(line: str) -> Optional[tuple]:
    """Parse markdown header, return (level, title) or None."""
    match = re.match(r'^(#{2,4})\s+(.+)$', line.strip())
    if match:
        level = len(match.group(1))
        title = match.group(2).strip()
        return (level, title)
    return None


def extract_chapter_section(title: str) -> tuple:
    """Extract chapter and section numbers from title.

    Examples:
        "3.4 Regression Details" -> (3, 4, "Regression Details")
        "3.4.1 Weighting Regression" -> (3, 4.1, "Weighting Regression")
        "Chapter 4: IV in Action" -> (4, None, "IV in Action")
        "Chapter 4" -> (4, None, "Chapter Introduction")
    """
    # First strip HTML tags
    title = strip_html(title).strip()

    # Pattern for "X.Y.Z Title" (subsection)
    match = re.match(r'^(\d+)\.(\d+)\.(\d+)\s+(.+)$', title)
    if match:
        chapter = int(match.group(1))
        section = float(f"{match.group(2)}.{match.group(3)}")
        return (chapter, section, match.group(4))

    # Pattern for "X.Y Title" (main section)
    match = re.match(r'^(\d+)\.(\d+)\s+(.+)$', title)
    if match:
        chapter = int(match.group(1))
        section = int(match.group(2))
        return (chapter, section, match.group(3))

    # Pattern for "Chapter X: Title" or "Chapter X Title"
    match = re.match(r'^Chapter\s+(\d+)[:\s]+(.+)$', title, re.IGNORECASE)
    if match:
        return (int(match.group(1)), None, match.group(2))

    # Pattern for "Chapter X" alone (chapter intro)
    match = re.match(r'^Chapter\s+(\d+)$', title, re.IGNORECASE)
    if match:
        return (int(match.group(1)), None, "Chapter Introduction")

    return (None, None, title)


def is_front_matter(title: str) -> bool:
    """Check if a section is front matter (to skip or categorize)."""
    front_matter_keywords = [
        'contents', 'list of figures', 'list of tables', 'preface',
        'acknowledgments', 'organization', 'acronyms', 'references',
        'bibliography', 'index', 'about the'
    ]
    title_lower = strip_html(title).lower()
    return any(keyword in title_lower for keyword in front_matter_keywords)


def strip_html(text: str) -> str:
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)


def slugify(text: str) -> str:
    """Convert title to filename-safe slug."""
    # Remove HTML tags first
    text = strip_html(text)
    # Remove special characters, replace spaces with underscores
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '_', slug)
    slug = slug.strip('_')
    return slug[:50]  # Limit length


def parse_textbook_content(source_dir: Path) -> list[Section]:
    """Parse page-range markdown files into sections.

    Key insight: Section boundaries may span multiple source files.
    We read ALL files as one continuous stream, then split by section headers.
    """
    sections = []

    # Get all page files sorted by starting page
    page_files = sorted(
        source_dir.glob('pages_*.md'),
        key=lambda p: int(p.stem.split('_')[1].split('-')[0])
    )

    if not page_files:
        print(f"  Warning: No pages_*.md files found in {source_dir}")
        return sections

    # Read all files as one continuous stream
    all_lines = []
    for file_path in page_files:
        content = file_path.read_text(encoding='utf-8')
        all_lines.extend(content.split('\n'))

    print(f"  Read {len(page_files)} files, {len(all_lines)} total lines")

    # Now parse the continuous stream
    current_section = None
    current_content = []
    current_page = None

    for line in all_lines:
        # Check for page marker
        page_num = extract_page_number(line)
        if page_num is not None:
            current_page = page_num
            # Include page marker in content for citation purposes
            current_content.append(line)
            continue

        # Check for header (## or ### level)
        header = parse_header(line)
        if header and header[0] <= 3:  # Only ## and ### headers
            level, title = header
            chapter, section_num, clean_title = extract_chapter_section(title)

            # Save previous section
            if current_section is not None:
                current_section.content = '\n'.join(current_content).strip()
                current_section.page_end = current_page
                if current_section.content:  # Only add non-empty
                    sections.append(current_section)

            # Start new section
            current_section = Section(
                chapter=chapter or 0,
                section=section_num,
                title=clean_title,  # Use cleaned title
                content='',
                page_start=current_page,
                level=level
            )
            current_content = []
        else:
            current_content.append(line)

    # Add final section
    if current_section is not None:
        current_section.content = '\n'.join(current_content).strip()
        current_section.page_end = current_page
        if current_section.content:
            sections.append(current_section)

    return sections


def generate_filename(section: Section, book: str) -> str:
    """Generate filename for section."""
    if section.chapter:
        if section.section is not None:
            # Format section as X_Y (e.g., 3_1 or 3_1_2)
            if isinstance(section.section, float) and section.section != int(section.section):
                # X.Y format (e.g., 1.2 -> 1_2)
                sec_str = str(section.section).replace('.', '_')
            else:
                # Integer section (e.g., 3 -> 3)
                sec_str = str(int(section.section))
            # e.g., ch03_2_regression_and_causality.md
            return f"ch{section.chapter:02d}_{sec_str}_{slugify(section.title)}.md"
        else:
            # Chapter intro: ch03_00_introduction.md
            return f"ch{section.chapter:02d}_00_{slugify(section.title)}.md"
    else:
        # No chapter number
        return f"{slugify(section.title)}.md"


def determine_part(chapter: int, book: str, title: str = '') -> str:
    """Determine which part/folder a chapter belongs to."""
    # Front matter goes to front_matter folder
    if is_front_matter(title):
        return 'front_matter'

    if book == 'angrist':
        if chapter in [1, 2]:
            return 'part1_introduction'
        elif chapter in [3, 4, 5]:
            return 'part2_core'
        elif chapter in [6, 7, 8]:
            return 'part3_extensions'
        elif chapter is None or chapter == 0:
            return 'other'
        else:
            return 'appendix'
    elif book == 'wooldridge':
        if chapter in [1, 2, 3]:
            return 'part1_foundations'
        elif chapter in [4, 5, 6, 7, 8]:
            return 'part2_linear_iv'
        elif chapter in [9]:
            return 'part3_systems'
        elif chapter in [10, 11, 12, 13, 14]:
            return 'part5_panel_data'
        elif chapter in [15, 16, 17]:
            return 'part4_nonlinear'
        elif chapter in [18, 19, 20, 21]:
            return 'part6_treatment_effects'
        elif chapter is None or chapter == 0:
            return 'other'
        else:
            return 'appendix'
    return 'other'


def write_section_file(section: Section, output_path: Path):
    """Write section to markdown file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Build header with metadata
    header = f"# {section.title}\n\n"
    if section.page_start:
        header += f"> Pages: {section.page_start}"
        if section.page_end and section.page_end != section.page_start:
            header += f"-{section.page_end}"
        header += "\n\n"

    content = header + section.content
    output_path.write_text(content, encoding='utf-8')


def generate_index(sections: list[Section], book: str) -> str:
    """Generate _index.md with TOC and page mappings."""
    lines = [f"# {book.title()} Table of Contents\n"]
    lines.append("## Quick Navigation\n")

    current_part = None
    current_chapter = None

    for section in sorted(sections, key=lambda s: (s.chapter or 0, s.section or 0)):
        part = determine_part(section.chapter or 0, book, section.title)

        if part != current_part:
            current_part = part
            lines.append(f"\n### {part.replace('_', ' ').title()}\n")

        if section.chapter != current_chapter:
            current_chapter = section.chapter
            if section.chapter:
                lines.append(f"\n**Chapter {section.chapter}**\n")

        filename = generate_filename(section, book)
        page_ref = ""
        if section.page_start:
            page_ref = f" (p.{section.page_start}"
            if section.page_end and section.page_end != section.page_start:
                page_ref += f"-{section.page_end}"
            page_ref += ")"

        # Indent based on whether it's a subsection
        indent = "  " if section.section else ""
        lines.append(f"{indent}- [{section.title}]({part}/{filename}){page_ref}")

    lines.append("\n\n## Page to File Mapping\n")
    lines.append("| Pages | File | Section |")
    lines.append("|-------|------|---------|")

    for section in sorted(sections, key=lambda s: s.page_start or 0):
        if section.page_start:
            pages = str(section.page_start)
            if section.page_end and section.page_end != section.page_start:
                pages = f"{section.page_start}-{section.page_end}"
            part = determine_part(section.chapter or 0, book, section.title)
            filename = generate_filename(section, book)
            lines.append(f"| {pages} | {part}/{filename} | {section.title} |")

    return '\n'.join(lines)


def reorganize_angrist(dry_run: bool = False):
    """Reorganize Angrist/MHE markdown files."""
    repo_root = get_repo_root()
    source_dir = repo_root / 'docs' / 'angrist_extracts'
    output_dir = repo_root / 'docs' / 'angrist_mhe'

    print(f"Parsing Angrist/MHE from {source_dir}...")
    sections = parse_textbook_content(source_dir)
    print(f"Found {len(sections)} sections")

    if dry_run:
        print("\n=== DRY RUN - Would create: ===")
        for section in sections[:20]:  # Show first 20
            part = determine_part(section.chapter or 0, 'angrist', section.title)
            filename = generate_filename(section, 'angrist')
            print(f"  {part}/{filename} (pp. {section.page_start}-{section.page_end})")
        if len(sections) > 20:
            print(f"  ... and {len(sections) - 20} more")
        return

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write section files
    for section in sections:
        part = determine_part(section.chapter or 0, 'angrist', section.title)
        filename = generate_filename(section, 'angrist')
        output_path = output_dir / part / filename
        write_section_file(section, output_path)
        print(f"  Created: {output_path.relative_to(repo_root)}")

    # Generate and write index
    index_content = generate_index(sections, 'angrist')
    index_path = output_dir / '_index.md'
    index_path.write_text(index_content, encoding='utf-8')
    print(f"  Created: {index_path.relative_to(repo_root)}")


def reorganize_wooldridge(dry_run: bool = False):
    """Reorganize Wooldridge markdown files."""
    repo_root = get_repo_root()
    source_dir = repo_root / 'docs' / 'wooldridge_textbook'
    output_dir = repo_root / 'docs' / 'wooldridge_panel'

    if not source_dir.exists():
        source_dir = repo_root / 'docs' / 'wooldridge_extracts'

    print(f"Parsing Wooldridge from {source_dir}...")
    sections = parse_textbook_content(source_dir)
    print(f"Found {len(sections)} sections")

    if dry_run:
        print("\n=== DRY RUN - Would create: ===")
        for section in sections[:20]:
            part = determine_part(section.chapter or 0, 'wooldridge', section.title)
            filename = generate_filename(section, 'wooldridge')
            print(f"  {part}/{filename} (pp. {section.page_start}-{section.page_end})")
        if len(sections) > 20:
            print(f"  ... and {len(sections) - 20} more")
        return

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write section files
    for section in sections:
        part = determine_part(section.chapter or 0, 'wooldridge', section.title)
        filename = generate_filename(section, 'wooldridge')
        output_path = output_dir / part / filename
        write_section_file(section, output_path)
        print(f"  Created: {output_path.relative_to(repo_root)}")

    # Generate and write index
    index_content = generate_index(sections, 'wooldridge')
    index_path = output_dir / '_index.md'
    index_path.write_text(index_content, encoding='utf-8')
    print(f"  Created: {index_path.relative_to(repo_root)}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Reorganize textbook markdown files')
    parser.add_argument('book', choices=['angrist', 'wooldridge', 'both'],
                       help='Which textbook to reorganize')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be created without writing files')

    args = parser.parse_args()

    if args.book in ['angrist', 'both']:
        reorganize_angrist(dry_run=args.dry_run)

    if args.book in ['wooldridge', 'both']:
        reorganize_wooldridge(dry_run=args.dry_run)
