"""Validation report generator."""

from pathlib import Path
from typing import Dict, Any
from datetime import datetime
from src.corpus.validation import Validation


class ValidationReport:
    """Generates markdown validation reports."""

    def __init__(self, validation: Validation):
        """Initialize report generator.
        
        Args:
            validation: Validation instance
        """
        self.validation = validation

    def generate_full_report(self) -> str:
        """Generate comprehensive validation report.
        
        Returns:
            Markdown-formatted report
        """
        # Run all validations
        rules_result = self.validation.validate_rules_against_wooldridge()
        models_result = self.validation.validate_models_against_wooldridge()
        coverage_result = self.validation.check_methodology_coverage()
        
        # Generate report sections
        report = []
        report.append(self._generate_header())
        report.append(self._generate_summary(rules_result, models_result, coverage_result))
        report.append(self._generate_rules_validation(rules_result))
        report.append(self._generate_models_validation(models_result))
        report.append(self._generate_coverage_analysis(coverage_result))
        report.append(self._generate_recommendations(rules_result, models_result, coverage_result))
        
        return "\n\n".join(report)

    def _generate_header(self) -> str:
        """Generate report header."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""# Corpus Validation Report

**Generated:** {timestamp}

This report validates the Econometrics Agent's rules and model implementations against Wooldridge's "Econometric Analysis of Cross Section and Panel Data" textbook corpus.

## Overview

This validation system:
- Compares agent rules with Wooldridge's methodological recommendations
- Validates model implementations against Wooldridge's best practices
- Analyzes methodology coverage to identify gaps
- Provides recommendations for alignment improvements"""

    def _generate_summary(
        self,
        rules_result: Dict[str, Any],
        models_result: Dict[str, Any],
        coverage_result: Dict[str, Any],
    ) -> str:
        """Generate summary section."""
        rules_count = len(rules_result.get("rules_validated", []))
        models_count = len(models_result.get("models_validated", []))
        
        rules_high = len([a for a in rules_result.get("alignments", {}).values() if a == "high"])
        rules_medium = len([a for a in rules_result.get("alignments", {}).values() if a == "medium"])
        rules_low = len([a for a in rules_result.get("alignments", {}).values() if a == "low"])
        
        models_high = len([a for a in models_result.get("alignments", {}).values() if a == "high"])
        models_medium = len([a for a in models_result.get("alignments", {}).values() if a == "medium"])
        models_low = len([a for a in models_result.get("alignments", {}).values() if a == "low"])
        
        gaps_count = len(rules_result.get("gaps", [])) + len(models_result.get("gaps", []))
        
        coverage_pct = coverage_result.get("coverage_percentage", 0)
        
        return f"""## Summary

### Rules Validation
- **Total rules validated:** {rules_count}
- **High alignment:** {rules_high}
- **Medium alignment:** {rules_medium}
- **Low alignment:** {rules_low}

### Models Validation
- **Total models validated:** {models_count}
- **High alignment:** {models_high}
- **Medium alignment:** {models_medium}
- **Low alignment:** {models_low}

### Coverage Analysis
- **Methodology coverage:** {coverage_pct:.1f}%
- **Covered methodologies:** {len(coverage_result.get('methodologies_covered', []))}
- **Missing methodologies:** {len(coverage_result.get('methodologies_missing', []))}

### Overall Assessment
- **Total gaps identified:** {gaps_count}
- **Recommendations:** {len(rules_result.get('recommendations', [])) + len(models_result.get('recommendations', []))}"""

    def _generate_rules_validation(self, rules_result: Dict[str, Any]) -> str:
        """Generate rules validation section."""
        report = ["## Rules Validation"]
        
        alignments = rules_result.get("alignments", {})
        wooldridge_refs = rules_result.get("wooldridge_references", {})
        
        report.append("### Rule Files")
        
        for rule_file in rules_result.get("rules_validated", []):
            rule_name = Path(rule_file).name
            alignment = alignments.get(rule_name, "unknown")
            refs = wooldridge_refs.get(rule_name, [])
            
            status_emoji = "✅" if alignment == "high" else "⚠️" if alignment == "medium" else "❌"
            
            report.append(f"\n#### {status_emoji} {rule_name}")
            report.append(f"- **Alignment:** {alignment}")
            report.append(f"- **Wooldridge references:** {len(refs)}")
            if refs:
                report.append(f"  - {', '.join(refs[:3])}")
                if len(refs) > 3:
                    report.append(f"  - ... and {len(refs) - 3} more")
        
        gaps = rules_result.get("gaps", [])
        if gaps:
            report.append("\n### Gaps Identified")
            for gap in gaps[:10]:
                report.append(f"- {gap}")
            if len(gaps) > 10:
                report.append(f"- ... and {len(gaps) - 10} more gaps")
        
        recommendations = rules_result.get("recommendations", [])
        if recommendations:
            report.append("\n### Recommendations")
            for rec in recommendations[:10]:
                report.append(f"- {rec}")
            if len(recommendations) > 10:
                report.append(f"- ... and {len(recommendations) - 10} more recommendations")
        
        return "\n".join(report)

    def _generate_models_validation(self, models_result: Dict[str, Any]) -> str:
        """Generate models validation section."""
        report = ["## Models Validation"]
        
        alignments = models_result.get("alignments", {})
        standard_errors = models_result.get("standard_errors", {})
        diagnostics = models_result.get("diagnostics", {})
        
        report.append("### Model Files")
        
        for model_file in models_result.get("models_validated", []):
            model_name = Path(model_file).stem
            alignment = alignments.get(model_name, "unknown")
            
            status_emoji = "✅" if alignment == "high" else "⚠️" if alignment == "medium" else "❌"
            
            report.append(f"\n#### {status_emoji} {model_name}")
            report.append(f"- **Alignment:** {alignment}")
            
            se_info = standard_errors.get(model_name, {})
            if se_info:
                report.append(f"- **Standard Errors:**")
                report.append(f"  - Implemented: {', '.join(se_info.get('implemented', []))}")
                report.append(f"  - Expected: {', '.join(se_info.get('expected', []))}")
            
            diag_info = diagnostics.get(model_name, {})
            if diag_info:
                report.append(f"- **Diagnostics:**")
                report.append(f"  - Implemented: {', '.join(diag_info.get('implemented', []))}")
                report.append(f"  - Expected: {', '.join(diag_info.get('expected', []))}")
        
        gaps = models_result.get("gaps", [])
        if gaps:
            report.append("\n### Gaps Identified")
            for gap in gaps[:10]:
                report.append(f"- {gap}")
            if len(gaps) > 10:
                report.append(f"- ... and {len(gaps) - 10} more gaps")
        
        recommendations = models_result.get("recommendations", [])
        if recommendations:
            report.append("\n### Recommendations")
            for rec in recommendations[:10]:
                report.append(f"- {rec}")
            if len(recommendations) > 10:
                report.append(f"- ... and {len(recommendations) - 10} more recommendations")
        
        return "\n".join(report)

    def _generate_coverage_analysis(self, coverage_result: Dict[str, Any]) -> str:
        """Generate coverage analysis section."""
        report = ["## Coverage Analysis"]
        
        coverage_pct = coverage_result.get("coverage_percentage", 0)
        covered = coverage_result.get("methodologies_covered", [])
        missing = coverage_result.get("methodologies_missing", [])
        priority_covered = coverage_result.get("priority_covered", [])
        priority_missing = coverage_result.get("priority_missing", [])
        
        report.append(f"### Overall Coverage: {coverage_pct:.1f}%")
        report.append(f"- **Covered:** {len(covered)} methodologies")
        report.append(f"- **Missing:** {len(missing)} methodologies")
        
        if covered:
            report.append("\n### Covered Methodologies")
            for meth in covered[:20]:
                report.append(f"- ✅ {meth}")
            if len(covered) > 20:
                report.append(f"- ... and {len(covered) - 20} more")
        
        if missing:
            report.append("\n### Missing Methodologies")
            for meth in missing[:20]:
                report.append(f"- ❌ {meth}")
            if len(missing) > 20:
                report.append(f"- ... and {len(missing) - 20} more")
        
        report.append("\n### Priority Coverage")
        report.append(f"- **Covered:** {len(priority_covered)}/{len(priority_covered) + len(priority_missing)}")
        if priority_covered:
            report.append(f"  - {', '.join(priority_covered)}")
        if priority_missing:
            report.append(f"- **Missing:** {', '.join(priority_missing)}")
        
        return "\n".join(report)

    def _generate_recommendations(
        self,
        rules_result: Dict[str, Any],
        models_result: Dict[str, Any],
        coverage_result: Dict[str, Any],
    ) -> str:
        """Generate recommendations section."""
        report = ["## Recommendations"]
        
        all_recommendations = []
        all_recommendations.extend(rules_result.get("recommendations", []))
        all_recommendations.extend(models_result.get("recommendations", []))
        
        # Add coverage-based recommendations
        missing = coverage_result.get("methodologies_missing", [])
        if missing:
            all_recommendations.append(
                f"Consider implementing missing methodologies: {', '.join(missing[:5])}"
            )
        
        if all_recommendations:
            report.append("### Priority Recommendations")
            for i, rec in enumerate(all_recommendations[:15], 1):
                report.append(f"{i}. {rec}")
            if len(all_recommendations) > 15:
                report.append(f"... and {len(all_recommendations) - 15} more recommendations")
        else:
            report.append("No specific recommendations at this time.")
        
        report.append("\n---")
        report.append("\n*Report generated by Corpus Validation System*")
        
        return "\n".join(report)



