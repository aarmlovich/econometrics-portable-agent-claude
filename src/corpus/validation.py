"""Main validation module for validating agent rules and models against Wooldridge corpus."""

from pathlib import Path
from typing import Dict, List, Any, Optional
from src.corpus.agent_integration import AgentIntegration
from src.corpus.rule_validator import RuleValidator
from src.corpus.model_validator import ModelValidator


class Validation:
    """Main validation coordinator for rules and models."""

    def __init__(self, project_root: Optional[Path] = None):
        """Initialize validation system.
        
        Args:
            project_root: Path to project root directory
        """
        if project_root is None:
            self.project_root = Path(".")
        else:
            self.project_root = Path(project_root)
        
        self.agent_integration = AgentIntegration(project_root=project_root)
        self.rule_validator = RuleValidator(self.agent_integration, project_root)
        self.model_validator = ModelValidator(self.agent_integration, project_root)

    def validate_rules_against_wooldridge(
        self, rule_files: Optional[List[Path]] = None
    ) -> Dict[str, Any]:
        """Validate agent rules against Wooldridge corpus.
        
        Args:
            rule_files: Optional list of specific rule files to validate.
                       If None, validates all rule files.
        
        Returns:
            Dictionary with validation results:
                - rules_validated: List of validated rule files
                - alignments: Dict mapping rule file to alignment status
                - gaps: List of identified gaps
                - recommendations: List of recommendations
        """
        return self.rule_validator.validate_all_rules(rule_files)

    def validate_models_against_wooldridge(
        self, model_files: Optional[List[Path]] = None
    ) -> Dict[str, Any]:
        """Validate model implementations against Wooldridge corpus.
        
        Args:
            model_files: Optional list of specific model files to validate.
                        If None, validates all model files.
        
        Returns:
            Dictionary with validation results:
                - models_validated: List of validated model files
                - alignments: Dict mapping model to alignment status
                - gaps: List of identified gaps
                - recommendations: List of recommendations
        """
        return self.model_validator.validate_all_models(model_files)

    def check_methodology_coverage(self) -> Dict[str, Any]:
        """Check if we cover Wooldridge's priority methodologies.
        
        Returns:
            Dictionary with coverage analysis:
                - methodologies_covered: List of covered methodologies
                - methodologies_missing: List of missing methodologies
                - coverage_percentage: Percentage of Wooldridge methods covered
                - priority_coverage: Coverage of priority methods
        """
        # Get all methodologies we implement
        our_methodologies = self._get_our_methodologies()
        
        # Get Wooldridge's key methodologies from corpus
        wooldridge_methodologies = self._get_wooldridge_methodologies()
        
        # Compare
        covered = set(our_methodologies) & set(wooldridge_methodologies)
        missing = set(wooldridge_methodologies) - set(our_methodologies)
        
        coverage_pct = (
            len(covered) / len(wooldridge_methodologies) * 100
            if wooldridge_methodologies
            else 0
        )
        
        # Priority methods (from our project overview)
        priority_methods = [
            "difference_in_differences",
            "regression_discontinuity",
            "matching",
            "instrumental_variables",
            "fixed_effects",
            "random_effects",
            "panel_iv",
        ]
        
        priority_covered = set(our_methodologies) & set(priority_methods)
        priority_missing = set(priority_methods) - set(our_methodologies)
        
        return {
            "methodologies_covered": sorted(list(covered)),
            "methodologies_missing": sorted(list(missing)),
            "coverage_percentage": round(coverage_pct, 2),
            "priority_covered": sorted(list(priority_covered)),
            "priority_missing": sorted(list(priority_missing)),
            "total_our_methodologies": len(our_methodologies),
            "total_wooldridge_methodologies": len(wooldridge_methodologies),
        }

    def _get_our_methodologies(self) -> List[str]:
        """Extract methodologies we implement from codebase."""
        methodologies = []
        
        # From models directory
        models_dir = self.project_root / "src" / "models"
        if models_dir.exists():
            for subdir in ["causal", "panel", "regression"]:
                subdir_path = models_dir / subdir
                if subdir_path.exists():
                    for file in subdir_path.glob("*.py"):
                        if file.stem != "__init__":
                            # Convert filename to methodology name
                            method_name = file.stem.replace("_", " ")
                            methodologies.append(method_name)
        
        # From rule files
        rules_dir = self.project_root / ".cursor" / "rules"
        if rules_dir.exists():
            rule_methodologies = self.rule_validator.extract_methodologies_from_rules()
            methodologies.extend(rule_methodologies)
        
        # Normalize and deduplicate
        normalized = []
        for m in methodologies:
            normalized_name = m.lower().replace(" ", "_")
            if normalized_name not in normalized:
                normalized.append(normalized_name)
        
        return normalized

    def _get_wooldridge_methodologies(self) -> List[str]:
        """Get key methodologies from Wooldridge corpus index."""
        try:
            index_path = (
                self.project_root
                / "data"
                / "corpus"
                / "wooldridge_index"
                / "index.json"
            )
            if index_path.exists():
                import json
                with open(index_path, "r", encoding="utf-8") as f:
                    index = json.load(f)
                    # Extract topic keys as methodologies
                    return list(index.get("topics", {}).keys())
        except Exception:
            pass
        
        # Fallback: known Wooldridge methodologies
        return [
            "fixed_effects_estimation",
            "random_effects_estimation",
            "clustered_standard_errors",
            "hc3_robust_standard_errors",
            "instrumental_variables",
            "difference_in_differences",
            "regression_discontinuity",
            "matching_methods",
            "panel_data_attrition",
            "survey_weights",
            "hac_standard_errors",
            "treatment_effects",
        ]

    def generate_validation_report(
        self, output_path: Optional[Path] = None
    ) -> str:
        """Generate comprehensive validation report.
        
        Args:
            output_path: Optional path to save report. If None, returns as string.
        
        Returns:
            Markdown-formatted validation report
        """
        from src.corpus.validation_report import ValidationReport
        
        report_generator = ValidationReport(self)
        report = report_generator.generate_full_report()
        
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report, encoding="utf-8")
        
        return report



