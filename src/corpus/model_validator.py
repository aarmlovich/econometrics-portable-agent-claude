"""Validator for model implementations against Wooldridge corpus."""

import ast
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from src.corpus.agent_integration import AgentIntegration


class ModelValidator:
    """Validates model implementations against Wooldridge corpus."""

    def __init__(
        self,
        agent_integration: AgentIntegration,
        project_root: Optional[Path] = None,
    ):
        """Initialize model validator.
        
        Args:
            agent_integration: AgentIntegration instance for corpus queries
            project_root: Path to project root directory
        """
        self.agent_integration = agent_integration
        if project_root is None:
            self.project_root = Path(".")
        else:
            self.project_root = Path(project_root)
        
        self.models_dir = self.project_root / "src" / "models"

    def validate_all_models(
        self, model_files: Optional[List[Path]] = None
    ) -> Dict[str, Any]:
        """Validate all model files or specific ones.
        
        Args:
            model_files: Optional list of specific model files to validate
        
        Returns:
            Dictionary with validation results
        """
        if model_files is None:
            model_files = []
            for subdir in ["causal", "panel", "regression"]:
                subdir_path = self.models_dir / subdir
                if subdir_path.exists():
                    model_files.extend(subdir_path.glob("*.py"))
        else:
            model_files = [Path(f) for f in model_files]
        
        # Filter out __init__.py
        model_files = [f for f in model_files if f.name != "__init__.py"]
        
        results = {
            "models_validated": [],
            "alignments": {},
            "gaps": [],
            "recommendations": [],
            "standard_errors": {},
            "diagnostics": {},
        }
        
        for model_file in model_files:
            if not model_file.exists():
                continue
            
            validation = self.compare_with_wooldridge(model_file)
            model_name = model_file.stem
            results["models_validated"].append(str(model_file))
            results["alignments"][model_name] = validation.get("alignment", "unknown")
            results["standard_errors"][model_name] = validation.get("standard_errors", {})
            results["diagnostics"][model_name] = validation.get("diagnostics", {})
            
            if validation.get("gaps"):
                results["gaps"].extend(validation["gaps"])
            if validation.get("recommendations"):
                results["recommendations"].extend(validation["recommendations"])
        
        return results

    def analyze_model_implementation(self, model_file: Path) -> Dict[str, Any]:
        """Analyze a model implementation to extract key features.
        
        Args:
            model_file: Path to model file
        
        Returns:
            Dictionary with analysis results
        """
        if not model_file.exists():
            return {}
        
        content = model_file.read_text(encoding="utf-8")
        
        analysis = {
            "standard_errors": [],
            "diagnostics": [],
            "features": [],
            "model_type": None,
        }
        
        # Detect standard error usage
        se_patterns = [
            (r"robust\s*=\s*True", "robust"),
            (r"clustered\s*=\s*True", "clustered"),
            (r"hc3", "hc3"),
            (r"hac", "hac"),
            (r"vce\(robust\)", "robust"),
            (r"cov_type\s*=\s*['\"]clustered['\"]", "clustered"),
        ]
        
        for pattern, se_type in se_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                if se_type not in analysis["standard_errors"]:
                    analysis["standard_errors"].append(se_type)
        
        # Detect diagnostics
        diag_patterns = [
            (r"first.stage", "first_stage"),
            (r"weak.instrument", "weak_instruments"),
            (r"overidentification", "overidentification"),
            (r"hausman", "hausman"),
            (r"parallel.trends", "parallel_trends"),
            (r"balance.test", "balance_test"),
        ]
        
        for pattern, diag_type in diag_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                if diag_type not in analysis["diagnostics"]:
                    analysis["diagnostics"].append(diag_type)
        
        # Detect model type from filename or class name
        model_name = model_file.stem
        if "fixed" in model_name.lower() and "effect" in model_name.lower():
            analysis["model_type"] = "fixed_effects"
        elif "random" in model_name.lower() and "effect" in model_name.lower():
            analysis["model_type"] = "random_effects"
        elif "diff" in model_name.lower() or "did" in model_name.lower():
            analysis["model_type"] = "difference_in_differences"
        elif "discontinuity" in model_name.lower() or "rd" in model_name.lower():
            analysis["model_type"] = "regression_discontinuity"
        elif "instrumental" in model_name.lower() or "iv" in model_name.lower():
            analysis["model_type"] = "instrumental_variables"
        elif "match" in model_name.lower():
            analysis["model_type"] = "matching"
        
        return analysis

    def compare_with_wooldridge(self, model_file: Path) -> Dict[str, Any]:
        """Compare model implementation with Wooldridge recommendations.
        
        Args:
            model_file: Path to model file
        
        Returns:
            Dictionary with comparison results
        """
        # Analyze model
        analysis = self.analyze_model_implementation(model_file)
        model_type = analysis.get("model_type")
        
        if not model_type:
            return {
                "model_file": str(model_file),
                "alignment": "unknown",
                "gaps": [],
                "recommendations": [],
            }
        
        # Get Wooldridge's perspective on this model type (may fail if corpus not built)
        try:
            wooldridge_perspective = self.agent_integration.get_wooldridge_perspective(
                model_type
            )
        except (RuntimeError, FileNotFoundError, Exception):
            wooldridge_perspective = None
        
        # Check standard errors
        se_validation = self.check_standard_errors(analysis, model_type)
        
        # Check diagnostics
        diag_validation = self.check_diagnostics(analysis, model_type)
        
        # Determine alignment
        gaps = []
        recommendations = []
        
        if se_validation.get("gaps"):
            gaps.extend(se_validation["gaps"])
        if diag_validation.get("gaps"):
            gaps.extend(diag_validation["gaps"])
        
        if se_validation.get("recommendations"):
            recommendations.extend(se_validation["recommendations"])
        if diag_validation.get("recommendations"):
            recommendations.extend(diag_validation["recommendations"])
        
        alignment = "high"
        if gaps:
            alignment = "medium" if len(gaps) < 3 else "low"
        
        return {
            "model_file": str(model_file),
            "model_type": model_type,
            "analysis": analysis,
            "wooldridge_perspective": wooldridge_perspective is not None,
            "standard_errors": se_validation,
            "diagnostics": diag_validation,
            "alignment": alignment,
            "gaps": gaps,
            "recommendations": recommendations,
        }

    def check_standard_errors(
        self, analysis: Dict[str, Any], model_type: str
    ) -> Dict[str, Any]:
        """Check if standard error choices align with Wooldridge.
        
        Args:
            analysis: Model analysis results
            model_type: Type of model
        
        Returns:
            Dictionary with SE validation results
        """
        implemented_se = analysis.get("standard_errors", [])
        gaps = []
        recommendations = []
        
        # Wooldridge recommendations by model type
        wooldridge_se_recommendations = {
            "fixed_effects": ["clustered"],
            "random_effects": ["clustered"],
            "difference_in_differences": ["clustered"],
            "panel_iv": ["clustered"],
            "instrumental_variables": ["robust", "clustered"],
            "regression_discontinuity": ["robust"],
            "matching": ["robust"],
        }
        
        expected_se = wooldridge_se_recommendations.get(model_type, [])
        
        if expected_se:
            missing_se = set(expected_se) - set(implemented_se)
            if missing_se:
                gaps.append(
                    f"Model {model_type} should use {', '.join(missing_se)} standard errors (Wooldridge recommendation)"
                )
                recommendations.append(
                    f"Consider adding {', '.join(missing_se)} standard errors to {model_type} model"
                )
        
        return {
            "implemented": implemented_se,
            "expected": expected_se,
            "gaps": gaps,
            "recommendations": recommendations,
        }

    def check_diagnostics(
        self, analysis: Dict[str, Any], model_type: str
    ) -> Dict[str, Any]:
        """Check if diagnostic requirements align with Wooldridge.
        
        Args:
            analysis: Model analysis results
            model_type: Type of model
        
        Returns:
            Dictionary with diagnostics validation results
        """
        implemented_diag = analysis.get("diagnostics", [])
        gaps = []
        recommendations = []
        
        # Wooldridge diagnostic recommendations by model type
        wooldridge_diag_recommendations = {
            "instrumental_variables": ["first_stage", "weak_instruments"],
            "panel_iv": ["first_stage", "weak_instruments"],
            "random_effects": ["hausman"],
            "difference_in_differences": ["parallel_trends"],
            "matching": ["balance_test"],
        }
        
        expected_diag = wooldridge_diag_recommendations.get(model_type, [])
        
        if expected_diag:
            missing_diag = set(expected_diag) - set(implemented_diag)
            if missing_diag:
                gaps.append(
                    f"Model {model_type} should include {', '.join(missing_diag)} diagnostics (Wooldridge recommendation)"
                )
                recommendations.append(
                    f"Consider adding {', '.join(missing_diag)} diagnostics to {model_type} model"
                )
        
        return {
            "implemented": implemented_diag,
            "expected": expected_diag,
            "gaps": gaps,
            "recommendations": recommendations,
        }

