"""Structured indexing for Wooldridge corpus."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from collections import defaultdict


class WooldridgeIndexer:
    """Build topic-based indices and cross-reference mappings."""

    # Methodology to topic mapping
    METHODOLOGY_TO_TOPIC = {
        "fixed effects": "panel_data",
        "random effects": "panel_data",
        "within transformation": "panel_data",
        "first-difference": "panel_data",
        "clustered standard errors": "panel_data",
        "panel data": "panel_data",
        "Hausman test": "panel_data",
        "attrition": "panel_data",
        "instrumental variables": "causal_inference",
        "two-stage least squares": "causal_inference",
        "difference-in-differences": "causal_inference",
        "regression discontinuity": "causal_inference",
        "matching": "causal_inference",
        "propensity score": "causal_inference",
        "treatment effects": "causal_inference",
        "overidentification": "causal_inference",
        "first-stage": "causal_inference",
        "robust standard errors": "regression",
        "heteroskedasticity": "regression",
        "HAC standard errors": "time_series",
        "autocorrelation": "time_series",
        "HC3": "regression",
        "small-sample correction": "panel_data",
        "survey weights": "data_handling",
        "inverse probability weighting": "causal_inference",
    }

    # Priority areas
    PRIORITY_AREAS = {
        "causal_inference": "Priority #1",
        "panel_data": "Priority #2",
    }

    def __init__(self, project_root: Optional[Path] = None):
        """Initialize indexer.
        
        Args:
            project_root: Path to project root. Defaults to current directory.
        """
        if project_root is None:
            self.project_root = Path(".")
        else:
            self.project_root = Path(project_root)

    def build_topic_index(
        self, analyzed_content: List[Dict]
    ) -> Dict:
        """Create topic-based lookup index.
        
        Args:
            analyzed_content: List of analysis results from WooldridgeAnalyzer
            
        Returns:
            Dictionary with topic-based indices:
                - by_methodology: Index by methodology name
                - by_topic: Index by topic category
                - by_priority: Index by priority area
                - by_chapter: Index by chapter/section
        """
        by_methodology = defaultdict(list)
        by_topic = defaultdict(list)
        by_priority = defaultdict(list)
        by_chapter = defaultdict(list)

        for file_analysis in analyzed_content:
            file_name = file_analysis["file_name"]
            file_path = file_analysis["file_path"]

            # Index by methodology
            for methodology in file_analysis["methodologies"]:
                meth_name = methodology["methodology"]
                by_methodology[meth_name].append({
                    "file_name": file_name,
                    "file_path": file_path,
                    "context": methodology["context"],
                    "section": methodology["section"],
                    "page": methodology["page"],
                })

            # Index by topic (derived from methodologies)
            topics_found = set()
            for methodology in file_analysis["methodologies"]:
                meth_name = methodology["methodology"]
                topic = self.METHODOLOGY_TO_TOPIC.get(
                    meth_name, "other"
                )
                topics_found.add(topic)

                by_topic[topic].append({
                    "file_name": file_name,
                    "file_path": file_path,
                    "methodology": meth_name,
                    "context": methodology["context"],
                    "section": methodology["section"],
                    "page": methodology["page"],
                })

            # Index by priority area
            for topic in topics_found:
                if topic in self.PRIORITY_AREAS:
                    priority = self.PRIORITY_AREAS[topic]
                    by_priority[priority].append({
                        "file_name": file_name,
                        "file_path": file_path,
                        "topic": topic,
                        "is_priority_file": file_analysis.get(
                            "is_priority", False
                        ),
                    })

            # Index by chapter/section
            for section in file_analysis["sections"]:
                section_title = section.get("title", "")
                if section_title:
                    by_chapter[section_title].append({
                        "file_name": file_name,
                        "file_path": file_path,
                        "level": section["level"],
                        "content_preview": section["content"][:200]
                        if section.get("content")
                        else "",
                        "page": section.get("page"),
                    })

        return {
            "by_methodology": dict(by_methodology),
            "by_topic": dict(by_topic),
            "by_priority": dict(by_priority),
            "by_chapter": dict(by_chapter),
            "metadata": {
                "total_files": len(analyzed_content),
                "total_methodologies": len(by_methodology),
                "total_topics": len(by_topic),
                "priority_areas": list(self.PRIORITY_AREAS.keys()),
            },
        }

    def create_cross_references(
        self, wooldridge_content: Dict, evaluations: Optional[Dict] = None
    ) -> Dict:
        """Link Wooldridge content to existing analysis.
        
        Args:
            wooldridge_content: Topic index from build_topic_index
            evaluations: Optional dictionary with evaluation file paths
            
        Returns:
            Dictionary with cross-reference mappings
        """
        if evaluations is None:
            evaluations = self._load_evaluation_files()

        cross_refs = defaultdict(dict)

        # Map methodologies to evaluation documents
        for methodology, entries in wooldridge_content[
            "by_methodology"
        ].items():
            # Find relevant sections in evaluation documents
            hansen_ref = self._find_evaluation_reference(
                methodology, "HANSEN_EVALUATION.md", evaluations
            )
            angrist_ref = self._find_evaluation_reference(
                methodology, "ANGRIST_EVALUATION.md", evaluations
            )
            wooldridge_ref = self._find_evaluation_reference(
                methodology, "WOOLDRIDGE_EVALUATION.md", evaluations
            )

            cross_refs[methodology] = {
                "wooldridge_sections": entries,
                "hansen_evaluation": hansen_ref,
                "angrist_evaluation": angrist_ref,
                "wooldridge_evaluation": wooldridge_ref,
                "agent_rules": self._find_agent_rules(methodology),
            }

        return dict(cross_refs)

    def _load_evaluation_files(self) -> Dict:
        """Load evaluation file paths."""
        eval_files = {
            "HANSEN_EVALUATION.md": self.project_root
            / "HANSEN_EVALUATION.md",
            "ANGRIST_EVALUATION.md": self.project_root
            / "ANGRIST_EVALUATION.md",
            "WOOLDRIDGE_EVALUATION.md": self.project_root
            / "WOOLDRIDGE_EVALUATION.md",
        }

        # Check which files exist
        existing = {
            name: path
            for name, path in eval_files.items()
            if path.exists()
        }

        return existing

    def _find_evaluation_reference(
        self, methodology: str, eval_file: str, evaluations: Dict
    ) -> Optional[Dict]:
        """Find reference to methodology in evaluation document."""
        if eval_file not in evaluations:
            return None

        eval_path = evaluations[eval_file]
        if not eval_path.exists():
            return None

        # Simple keyword search in evaluation file
        content = eval_path.read_text(encoding="utf-8")
        content_lower = content.lower()
        meth_lower = methodology.lower()

        if meth_lower in content_lower:
            # Find line numbers where methodology is mentioned
            lines = content.split("\n")
            mentions = []
            for i, line in enumerate(lines):
                if meth_lower in line.lower():
                    mentions.append({
                        "line": i + 1,
                        "content": line.strip()[:200],
                    })

            return {
                "file": str(eval_path),
                "mentions": mentions[:5],  # Limit to first 5 mentions
            }

        return None

    def _find_agent_rules(self, methodology: str) -> List[str]:
        """Find relevant agent rule files for methodology."""
        rules_dir = self.project_root / ".cursor" / "rules"
        if not rules_dir.exists():
            return []

        # Map methodology to likely rule files
        methodology_lower = methodology.lower()

        rule_mappings = {
            "fixed effects": "panel-data.mdc",
            "random effects": "panel-data.mdc",
            "panel data": "panel-data.mdc",
            "clustered standard errors": "panel-data.mdc",
            "instrumental variables": "causal-inference.mdc",
            "two-stage least squares": "causal-inference.mdc",
            "difference-in-differences": "causal-inference.mdc",
            "regression discontinuity": "causal-inference.mdc",
            "matching": "causal-inference.mdc",
            "treatment effects": "causal-inference.mdc",
            "robust standard errors": "regression-core.mdc",
            "heteroskedasticity": "regression-core.mdc",
            "HC3": "regression-core.mdc",
            "survey weights": "data-handling.mdc",
            "attrition": "panel-data.mdc",
        }

        relevant_rules = []
        for key, rule_file in rule_mappings.items():
            if key in methodology_lower:
                rule_path = rules_dir / rule_file
                if rule_path.exists():
                    relevant_rules.append(str(rule_path))

        return relevant_rules

    def generate_methodology_map(self) -> Dict:
        """Map Wooldridge methods to agent capabilities.
        
        Returns:
            Dictionary mapping methodologies to agent implementation status
        """
        # This would ideally check actual code, but for now we'll use
        # a static mapping based on known implementations
        methodology_map = {
            "fixed effects": {
                "agent_implementation": "src/models/panel/fixed_effects.py",
                "agent_rules": ".cursor/rules/panel-data.mdc",
                "status": "implemented",
            },
            "random effects": {
                "agent_implementation": "src/models/panel/random_effects.py",
                "agent_rules": ".cursor/rules/panel-data.mdc",
                "status": "implemented",
            },
            "instrumental variables": {
                "agent_implementation": "src/models/causal/instrumental_variables.py",
                "agent_rules": ".cursor/rules/causal-inference.mdc",
                "status": "implemented",
            },
            "difference-in-differences": {
                "agent_implementation": "src/models/causal/diff_in_diff.py",
                "agent_rules": ".cursor/rules/causal-inference.mdc",
                "status": "implemented",
            },
            "regression discontinuity": {
                "agent_implementation": "src/models/causal/regression_discontinuity.py",
                "agent_rules": ".cursor/rules/causal-inference.mdc",
                "status": "implemented",
            },
            "matching": {
                "agent_implementation": "src/models/causal/matching.py",
                "agent_rules": ".cursor/rules/causal-inference.mdc",
                "status": "implemented",
            },
            "clustered standard errors": {
                "agent_implementation": "src/models/panel/fixed_effects.py",
                "agent_rules": ".cursor/rules/panel-data.mdc",
                "status": "implemented",
            },
            "robust standard errors": {
                "agent_implementation": "src/models/regression/ols.py",
                "agent_rules": ".cursor/rules/regression-core.mdc",
                "status": "implemented",
            },
            "survey weights": {
                "agent_implementation": None,
                "agent_rules": ".cursor/rules/data-handling.mdc",
                "status": "documented",
            },
            "attrition": {
                "agent_implementation": None,
                "agent_rules": ".cursor/rules/panel-data.mdc",
                "status": "documented",
            },
        }

        return methodology_map

    def save_index(self, index: Dict, output_path: Path) -> None:
        """Save index to JSON file.
        
        Args:
            index: Index dictionary to save
            output_path: Path to save JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

        print(f"Saved index to {output_path}")

    def save_cross_references(
        self, cross_refs: Dict, output_path: Path
    ) -> None:
        """Save cross-references to JSON file.
        
        Args:
            cross_refs: Cross-reference dictionary to save
            output_path: Path to save JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(cross_refs, f, indent=2, ensure_ascii=False)

        print(f"Saved cross-references to {output_path}")



