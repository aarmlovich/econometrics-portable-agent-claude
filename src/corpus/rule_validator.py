"""Validator for agent rule files against Wooldridge corpus."""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from src.corpus.agent_integration import AgentIntegration


class RuleValidator:
    """Validates rule files against Wooldridge corpus."""

    def __init__(
        self,
        agent_integration: AgentIntegration,
        project_root: Optional[Path] = None,
    ):
        """Initialize rule validator.
        
        Args:
            agent_integration: AgentIntegration instance for corpus queries
            project_root: Path to project root directory
        """
        self.agent_integration = agent_integration
        if project_root is None:
            self.project_root = Path(".")
        else:
            self.project_root = Path(project_root)
        
        self.rules_dir = self.project_root / ".cursor" / "rules"

    def validate_all_rules(
        self, rule_files: Optional[List[Path]] = None
    ) -> Dict[str, Any]:
        """Validate all rule files or specific ones.
        
        Args:
            rule_files: Optional list of specific rule files to validate
        
        Returns:
            Dictionary with validation results
        """
        if rule_files is None:
            rule_files = list(self.rules_dir.glob("*.mdc"))
        else:
            rule_files = [Path(f) for f in rule_files]
        
        results = {
            "rules_validated": [],
            "alignments": {},
            "gaps": [],
            "recommendations": [],
            "wooldridge_references": {},
        }
        
        for rule_file in rule_files:
            if not rule_file.exists():
                continue
            
            validation = self.compare_rule_with_wooldridge(rule_file)
            results["rules_validated"].append(str(rule_file))
            results["alignments"][rule_file.name] = validation.get("alignment", "unknown")
            results["wooldridge_references"][rule_file.name] = validation.get(
                "wooldridge_references", []
            )
            
            if validation.get("gaps"):
                results["gaps"].extend(validation["gaps"])
            if validation.get("recommendations"):
                results["recommendations"].extend(validation["recommendations"])
        
        return results

    def compare_rule_with_wooldridge(self, rule_file: Path) -> Dict[str, Any]:
        """Compare a specific rule file with Wooldridge corpus.
        
        Args:
            rule_file: Path to rule file
        
        Returns:
            Dictionary with comparison results
        """
        # Extract methodologies from rule file
        methodologies = self.extract_methodologies_from_rule_file(rule_file)
        
        # Check for Wooldridge references
        wooldridge_refs = self.validate_rule_references(rule_file)
        
        # Query corpus for each methodology
        alignments = []
        gaps = []
        recommendations = []
        
        for methodology in methodologies:
            # Get Wooldridge's perspective (may fail if corpus not built)
            try:
                wooldridge_perspective = self.agent_integration.get_wooldridge_perspective(
                    methodology
                )
            except (RuntimeError, FileNotFoundError, Exception):
                wooldridge_perspective = None
            
            if wooldridge_perspective:
                # Check if rule references Wooldridge for this methodology
                ref_found = any(
                    methodology.lower() in ref.lower() or ref.lower() in methodology.lower()
                    for ref in wooldridge_refs
                )
                
                if not ref_found:
                    gaps.append(
                        f"Rule {rule_file.name} discusses {methodology} but doesn't reference Wooldridge"
                    )
                    recommendations.append(
                        f"Consider adding Wooldridge reference for {methodology} in {rule_file.name}"
                    )
                
                alignments.append({
                    "methodology": methodology,
                    "wooldridge_covered": True,
                    "reference_found": ref_found,
                })
            else:
                alignments.append({
                    "methodology": methodology,
                    "wooldridge_covered": False,
                    "reference_found": False,
                })
        
        # Determine overall alignment
        if not alignments:
            alignment = "unknown"
        elif all(a.get("wooldridge_covered", False) for a in alignments):
            alignment = "high" if all(a.get("reference_found", False) for a in alignments) else "medium"
        else:
            alignment = "low"
        
        return {
            "rule_file": str(rule_file),
            "methodologies": methodologies,
            "wooldridge_references": wooldridge_refs,
            "alignments": alignments,
            "alignment": alignment,
            "gaps": gaps,
            "recommendations": recommendations,
        }

    def extract_methodologies_from_rules(self) -> List[str]:
        """Extract all methodologies mentioned across all rule files.
        
        Returns:
            List of methodology names
        """
        methodologies = set()
        
        if not self.rules_dir.exists():
            return []
        
        for rule_file in self.rules_dir.glob("*.mdc"):
            rule_methods = self.extract_methodologies_from_rule_file(rule_file)
            methodologies.update(rule_methods)
        
        return sorted(list(methodologies))

    def extract_methodologies_from_rule_file(self, rule_file: Path) -> List[str]:
        """Extract methodologies mentioned in a rule file.
        
        Args:
            rule_file: Path to rule file
        
        Returns:
            List of methodology names found
        """
        if not rule_file.exists():
            return []
        
        content = rule_file.read_text(encoding="utf-8")
        
        # Known methodologies to look for
        known_methods = [
            "fixed effects",
            "random effects",
            "difference in differences",
            "difference-in-differences",
            "regression discontinuity",
            "instrumental variables",
            "matching",
            "propensity score",
            "clustered standard errors",
            "robust standard errors",
            "hc3",
            "hac standard errors",
            "panel iv",
            "treatment effects",
            "attrition",
            "survey weights",
        ]
        
        found_methods = []
        content_lower = content.lower()
        
        for method in known_methods:
            # Look for methodology mentions
            pattern = re.compile(
                r"\b" + re.escape(method.lower()) + r"\b", re.IGNORECASE
            )
            if pattern.search(content):
                found_methods.append(method.replace(" ", "_").replace("-", "_"))
        
        # Also look for section headers that might indicate methodologies
        header_pattern = re.compile(r"^##+\s+(.+)$", re.MULTILINE)
        headers = header_pattern.findall(content)
        for header in headers:
            header_lower = header.lower()
            if any(
                keyword in header_lower
                for keyword in ["method", "estimation", "model", "effect", "regression"]
            ):
                # Normalize header to methodology name
                method_name = header.lower().replace(" ", "_").replace("-", "_")
                if method_name not in found_methods:
                    found_methods.append(method_name)
        
        return found_methods

    def validate_rule_references(self, rule_file: Path) -> List[str]:
        """Check if rule file references Wooldridge appropriately.
        
        Args:
            rule_file: Path to rule file
        
        Returns:
            List of Wooldridge references found
        """
        if not rule_file.exists():
            return []
        
        content = rule_file.read_text(encoding="utf-8")
        
        # Look for Wooldridge references
        wooldridge_patterns = [
            r"wooldridge",
            r"chapter\s+\d+",
            r"corpus\s+query",
            r"agent_integration",
            r"lookup_wooldridge",
        ]
        
        references = []
        for pattern in wooldridge_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            references.extend(matches)
        
        # Also look for specific chapter references
        chapter_pattern = re.compile(r"chapter\s+(\d+)", re.IGNORECASE)
        chapters = chapter_pattern.findall(content)
        references.extend([f"Chapter {ch}" for ch in chapters])
        
        return list(set(references))

