"""Content analyzer for Wooldridge textbook markdown files."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json


class WooldridgeAnalyzer:
    """Analyze Wooldridge textbook markdown files to extract structured content."""

    # Priority sections based on agent focus
    PRIORITY_PARTS = {
        "part5_nonlinear_models.md": "Treatment Effects (Priority #1)",
        "part6_panel_data.md": "Panel Data Methods (Priority #2)",
    }

    # Key methodological terms to identify
    METHODOLOGY_KEYWORDS = [
        "fixed effects",
        "random effects",
        "clustered standard errors",
        "robust standard errors",
        "instrumental variables",
        "two-stage least squares",
        "difference-in-differences",
        "regression discontinuity",
        "matching",
        "propensity score",
        "treatment effects",
        "panel data",
        "within transformation",
        "first-difference",
        "Hausman test",
        "overidentification",
        "first-stage",
        "heteroskedasticity",
        "autocorrelation",
        "HAC standard errors",
        "HC3",
        "small-sample correction",
        "survey weights",
        "attrition",
        "inverse probability weighting",
    ]

    def __init__(self, extracts_dir: Optional[Path] = None):
        """Initialize analyzer with extracts directory.
        
        Args:
            extracts_dir: Path to wooldridge_extracts directory. 
                         Defaults to docs/wooldridge_extracts relative to project root.
        """
        if extracts_dir is None:
            # Assume we're in project root
            self.extracts_dir = Path("docs/wooldridge_extracts")
        else:
            self.extracts_dir = Path(extracts_dir)

    def analyze_markdown_file(self, file_path: Path) -> Dict:
        """Extract structured content from a single markdown file.
        
        Args:
            file_path: Path to markdown file to analyze
            
        Returns:
            Dictionary containing:
                - file_name: Name of the file
                - file_path: Path to file
                - sections: List of extracted sections
                - methodologies: List of identified methodologies
                - equations: List of extracted equations
                - perspectives: Dictionary of Wooldridge's perspectives
                - page_ranges: Extracted page ranges
                - is_priority: Whether this is a priority part
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        content = file_path.read_text(encoding="utf-8")
        file_name = file_path.name

        # Extract page ranges from filename if it's a page file
        page_range = self._extract_page_range(file_name)

        # Parse sections
        sections = self._extract_sections(content, file_name)

        # Extract methodologies
        methodologies = self._extract_methodologies(content, file_name)

        # Extract equations
        equations = self._extract_equations(content, file_name)

        # Identify perspectives
        perspectives = self._identify_perspectives(content, file_name)

        # Check if priority part
        is_priority = file_name in self.PRIORITY_PARTS
        priority_reason = (
            self.PRIORITY_PARTS.get(file_name) if is_priority else None
        )

        return {
            "file_name": file_name,
            "file_path": str(file_path),
            "page_range": page_range,
            "sections": sections,
            "methodologies": methodologies,
            "equations": equations,
            "perspectives": perspectives,
            "is_priority": is_priority,
            "priority_reason": priority_reason,
            "total_sections": len(sections),
            "total_methodologies": len(methodologies),
        }

    def _extract_page_range(self, file_name: str) -> Optional[Tuple[int, int]]:
        """Extract page range from filename like 'pages_101-110.md'."""
        match = re.search(r"pages_(\d+)-(\d+)", file_name)
        if match:
            return (int(match.group(1)), int(match.group(2)))
        return None

    def _extract_sections(
        self, content: str, file_name: str
    ) -> List[Dict]:
        """Extract section headers and hierarchy from markdown content.
        
        Returns list of sections with:
            - level: Header level (1-6)
            - title: Section title
            - content: Section content
            - page: Page number if available
        """
        sections = []
        lines = content.split("\n")

        current_section = None
        current_content = []
        current_page = None

        for line in lines:
            # Check for page markers
            page_match = re.match(r"^## Page (\d+)$", line.strip())
            if page_match:
                current_page = int(page_match.group(1))
                # Save previous section if exists
                if current_section:
                    current_section["content"] = "\n".join(current_content)
                    sections.append(current_section)
                current_section = None
                current_content = []
                continue

            # Check for headers
            header_match = re.match(r"^(#{1,6})\s+(.+)$", line)
            if header_match:
                # Save previous section
                if current_section:
                    current_section["content"] = "\n".join(current_content)
                    sections.append(current_section)

                # Start new section
                level = len(header_match.group(1))
                title = header_match.group(2).strip()
                current_section = {
                    "level": level,
                    "title": title,
                    "content": "",
                    "page": current_page,
                }
                current_content = []
            else:
                # Add to current section content
                if current_section:
                    current_content.append(line)
                elif current_content or line.strip():
                    # Content before first section
                    current_content.append(line)

        # Save last section
        if current_section:
            current_section["content"] = "\n".join(current_content)
            sections.append(current_section)

        return sections

    def _extract_methodologies(
        self, content: str, file_name: str
    ) -> List[Dict]:
        """Identify methodological concepts in content.
        
        Returns list of methodology mentions with:
            - methodology: Name of methodology
            - context: Surrounding text
            - section: Section where found
            - page: Page number if available
        """
        methodologies = []
        content_lower = content.lower()

        for keyword in self.METHODOLOGY_KEYWORDS:
            # Find all occurrences (case-insensitive)
            pattern = re.escape(keyword)
            matches = list(re.finditer(pattern, content_lower, re.IGNORECASE))

            for match in matches:
                # Extract context (100 chars before and after)
                start = max(0, match.start() - 100)
                end = min(len(content), match.end() + 100)
                context = content[start:end].strip()

                # Try to find section title
                section_title = self._find_section_for_position(
                    content, match.start()
                )

                # Try to find page number
                page = self._find_page_for_position(content, match.start())

                methodologies.append({
                    "methodology": keyword,
                    "context": context,
                    "section": section_title,
                    "page": page,
                    "position": match.start(),
                })

        # Remove duplicates (same methodology in same section)
        seen = set()
        unique_methodologies = []
        for meth in methodologies:
            key = (meth["methodology"], meth["section"], meth["page"])
            if key not in seen:
                seen.add(key)
                unique_methodologies.append(meth)

        return unique_methodologies

    def _extract_equations(self, content: str, file_name: str) -> List[Dict]:
        """Extract mathematical formulations and equations.
        
        Looks for:
            - LaTeX-style equations ($$ or $)
            - Numbered equations (equation X.X)
            - Mathematical expressions
        """
        equations = []

        # Pattern for numbered equations: "equation 17.70" or "equation (17.70)"
        equation_pattern = r"equation\s+(?:\(?(\d+\.\d+)\)?|(\d+))"
        equation_matches = re.finditer(
            equation_pattern, content, re.IGNORECASE
        )

        for match in equation_matches:
            eq_num = match.group(1) or match.group(2)

            # Extract context around equation reference
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context = content[start:end].strip()

            section = self._find_section_for_position(content, match.start())
            page = self._find_page_for_position(content, match.start())

            equations.append({
                "equation_number": eq_num,
                "context": context,
                "section": section,
                "page": page,
                "position": match.start(),
            })

        # Also look for LaTeX-style equations
        latex_pattern = r"\$\$.*?\$\$|\$[^\$]+\$"
        latex_matches = re.finditer(latex_pattern, content, re.DOTALL)

        for match in latex_matches:
            equation_text = match.group(0)
            section = self._find_section_for_position(content, match.start())
            page = self._find_page_for_position(content, match.start())

            equations.append({
                "equation_number": None,
                "equation_text": equation_text,
                "context": content[
                    max(0, match.start() - 100) : min(
                        len(content), match.end() + 100
                    )
                ].strip(),
                "section": section,
                "page": page,
                "position": match.start(),
            })

        return equations

    def _identify_perspectives(
        self, content: str, file_name: str
    ) -> Dict:
        """Extract Wooldridge's methodological positions and recommendations.
        
        Looks for:
            - Recommendations ("should use", "recommend", "prefer")
            - Comparisons ("better than", "preferred over")
            - Best practices ("best practice", "standard approach")
        """
        perspectives = {}

        # Patterns for recommendations
        recommendation_patterns = [
            r"should\s+use\s+([^\.]+)",
            r"recommend\s+([^\.]+)",
            r"prefer\s+([^\.]+)",
            r"best\s+practice\s+is\s+to\s+([^\.]+)",
            r"standard\s+approach\s+is\s+to\s+([^\.]+)",
        ]

        for pattern in recommendation_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                recommendation = match.group(1).strip()
                context = content[
                    max(0, match.start() - 150) : min(
                        len(content), match.end() + 150
                    )
                ].strip()

                # Try to identify which methodology this refers to
                for keyword in self.METHODOLOGY_KEYWORDS:
                    if keyword.lower() in recommendation.lower():
                        if keyword not in perspectives:
                            perspectives[keyword] = []
                        perspectives[keyword].append({
                            "recommendation": recommendation,
                            "context": context,
                            "section": self._find_section_for_position(
                                content, match.start()
                            ),
                            "page": self._find_page_for_position(
                                content, match.start()
                            ),
                        })
                        break

        return perspectives

    def _find_section_for_position(
        self, content: str, position: int
    ) -> Optional[str]:
        """Find the section title for a given character position."""
        # Get content up to position
        content_before = content[:position]

        # Find the last header before this position
        headers = list(
            re.finditer(r"^(#{1,6})\s+(.+)$", content_before, re.MULTILINE)
        )

        if headers:
            last_header = headers[-1]
            return last_header.group(2).strip()

        return None

    def _find_page_for_position(self, content: str, position: int) -> Optional[int]:
        """Find the page number for a given character position."""
        content_before = content[:position]

        # Find the last page marker before this position
        page_matches = list(
            re.finditer(r"^## Page (\d+)$", content_before, re.MULTILINE)
        )

        if page_matches:
            return int(page_matches[-1].group(1))

        return None

    def analyze_all_files(self) -> List[Dict]:
        """Analyze all markdown files in extracts directory.
        
        Returns:
            List of analysis results for each file
        """
        if not self.extracts_dir.exists():
            raise FileNotFoundError(
                f"Extracts directory not found: {self.extracts_dir}"
            )

        # Find all markdown files
        md_files = list(self.extracts_dir.glob("*.md"))
        md_files = [
            f
            for f in md_files
            if not f.name.startswith(".")
            and f.name != "extraction_log.md"
        ]

        results = []
        for md_file in sorted(md_files):
            try:
                result = self.analyze_markdown_file(md_file)
                results.append(result)
            except Exception as e:
                print(f"Error analyzing {md_file.name}: {e}")
                continue

        return results

    def save_analysis(self, results: List[Dict], output_path: Path) -> None:
        """Save analysis results to JSON file.
        
        Args:
            results: List of analysis results
            output_path: Path to save JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"Saved analysis to {output_path} ({len(results)} files analyzed)")

