"""CLI interface for Wooldridge corpus operations."""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from src.corpus.wooldridge_analyzer import WooldridgeAnalyzer
from src.corpus.wooldridge_index import WooldridgeIndexer
from src.corpus.wooldridge_embeddings import WooldridgeEmbeddings
from src.corpus.wooldridge_retriever import WooldridgeRetriever
from src.corpus.utils import get_default_paths
from src.corpus.validation import Validation


def build_corpus(args):
    """Build corpus from markdown files."""
    paths = get_default_paths(args.project_root)

    print("=" * 60)
    print("Building Wooldridge Corpus")
    print("=" * 60)

    # Step 1: Analyze markdown files
    print("\nStep 1: Analyzing markdown files...")
    analyzer = WooldridgeAnalyzer(extracts_dir=paths["extracts_dir"])
    analyzed_content = analyzer.analyze_all_files()
    print(f"Analyzed {len(analyzed_content)} files")

    # Save analysis
    paths["index_dir"].mkdir(parents=True, exist_ok=True)
    analyzer.save_analysis(analyzed_content, paths["analysis_file"])

    # Step 2: Build indices
    print("\nStep 2: Building topic indices...")
    indexer = WooldridgeIndexer(project_root=args.project_root)
    topic_index = indexer.build_topic_index(analyzed_content)
    indexer.save_index(topic_index, paths["index_file"])

    # Build cross-references
    print("\nStep 3: Building cross-references...")
    cross_refs = indexer.create_cross_references(topic_index)
    indexer.save_cross_references(cross_refs, paths["cross_refs_file"])

    # Generate methodology map
    methodology_map = indexer.generate_methodology_map()
    indexer.save_index(
        methodology_map, paths["methodology_map_file"]
    )

    # Step 3: Generate embeddings
    print("\nStep 4: Generating embeddings...")
    embeddings_gen = WooldridgeEmbeddings()
    embedded_chunks = embeddings_gen.process_analyzed_content(analyzed_content)
    print(f"Generated {len(embedded_chunks)} embedded chunks")

    # Save embeddings
    paths["embeddings_dir"].mkdir(parents=True, exist_ok=True)
    embeddings_gen.save_embeddings(embedded_chunks, paths["embeddings_file"])

    print("\n" + "=" * 60)
    print("Corpus build complete!")
    print("=" * 60)
    print(f"  Analysis: {paths['analysis_file']}")
    print(f"  Index: {paths['index_file']}")
    print(f"  Cross-references: {paths['cross_refs_file']}")
    print(f"  Embeddings: {paths['embeddings_file']}")


def search_corpus(args):
    """Search corpus using semantic search."""
    paths = get_default_paths(args.project_root)

    retriever = WooldridgeRetriever(
        embeddings_path=paths["embeddings_file"],
        index_path=paths["index_file"],
        cross_refs_path=paths["cross_refs_file"],
        project_root=args.project_root,
    )

    print(f"\nSearching for: '{args.query}'")
    print("=" * 60)

    results = retriever.semantic_search(args.query, top_k=args.top_k)

    for i, result in enumerate(results, 1):
        print(f"\nResult {i} (relevance: {result['relevance_score']:.3f}):")
        print(f"  File: {result['metadata']['file_name']}")
        if result['metadata'].get('section_title'):
            print(f"  Section: {result['metadata']['section_title']}")
        if result['metadata'].get('page'):
            print(f"  Page: {result['metadata']['page']}")
        print(f"  Content preview:")
        content_preview = result['content'][:300]
        print(f"    {content_preview}...")


def lookup_topic(args):
    """Lookup topic in corpus."""
    paths = get_default_paths(args.project_root)

    retriever = WooldridgeRetriever(
        embeddings_path=paths["embeddings_file"],
        index_path=paths["index_file"],
        cross_refs_path=paths["cross_refs_file"],
        project_root=args.project_root,
    )

    print(f"\nLooking up topic: '{args.topic}'")
    print("=" * 60)

    result = retriever.lookup_topic(args.topic)

    if result.get("methodologies"):
        print(f"\nFound {len(result['methodologies'])} methodology references:")
        for meth in result["methodologies"][:args.limit]:
            print(f"  - {meth['file_name']}: {meth.get('section', 'N/A')}")

    if result.get("sections"):
        print(f"\nFound {len(result['sections'])} topic sections:")
        for section in result["sections"][:args.limit]:
            print(f"  - {section['file_name']}: {section.get('section', 'N/A')}")

    if result.get("priority"):
        print(f"\nPriority area: {result['priority']}")


def compare_perspectives(args):
    """Compare Wooldridge perspective with Hansen/Angrist."""
    paths = get_default_paths(args.project_root)

    retriever = WooldridgeRetriever(
        embeddings_path=paths["embeddings_file"],
        index_path=paths["index_file"],
        cross_refs_path=paths["cross_refs_file"],
        project_root=args.project_root,
    )

    print(f"\nComparing perspectives on: '{args.methodology}'")
    print("=" * 60)

    result = retriever.cross_reference(args.methodology)

    # Wooldridge perspective
    print("\nWooldridge Perspective:")
    if result["wooldridge"].get("sections"):
        print(f"  Found {len(result['wooldridge']['sections'])} references")
        for section in result["wooldridge"]["sections"][:3]:
            print(f"    - {section['file_name']}: {section.get('section', 'N/A')}")

    if result["wooldridge"].get("perspective"):
        print(f"  Recommendations found: {len(result['wooldridge']['perspective'])}")

    # Hansen perspective
    if result.get("hansen"):
        print("\nHansen Evaluation:")
        print(f"  File: {result['hansen']['file']}")
        if result["hansen"].get("mentions"):
            print(f"  Mentions: {len(result['hansen']['mentions'])}")

    # Angrist perspective
    if result.get("angrist"):
        print("\nAngrist Evaluation:")
        print(f"  File: {result['angrist']['file']}")
        if result["angrist"].get("mentions"):
            print(f"  Mentions: {len(result['angrist']['mentions'])}")

    # Agent rules
    if result.get("agent_rules"):
        print("\nAgent Rules:")
        for rule in result["agent_rules"]:
            print(f"  - {rule}")


def find_perspective(args):
    """Find Wooldridge's perspective on a methodology."""
    paths = get_default_paths(args.project_root)

    retriever = WooldridgeRetriever(
        embeddings_path=paths["embeddings_file"],
        index_path=paths["index_file"],
        cross_refs_path=paths["cross_refs_file"],
        project_root=args.project_root,
    )

    print(f"\nFinding Wooldridge's perspective on: '{args.methodology}'")
    print("=" * 60)

    result = retriever.find_perspective(args.methodology)

    if result.get("sections"):
        print(f"\nFound {len(result['sections'])} sections:")
        for section in result["sections"][:args.limit]:
            print(f"\n  File: {section['file_name']}")
            print(f"  Section: {section.get('section', 'N/A')}")
            if section.get('page'):
                print(f"  Page: {section['page']}")
            print(f"  Context: {section.get('context', '')[:200]}...")

    if result.get("wooldridge_perspective"):
        print(f"\nPerspectives/Recommendations:")
        for perspective in result["wooldridge_perspective"][:args.limit]:
            print(f"\n  Context: {perspective['context'][:300]}...")
            if perspective.get('section'):
                print(f"  Section: {perspective['section']}")

    if result.get("cross_references"):
        print(f"\nCross-references available")


def validate_all(args):
    """Run full validation of rules and models."""
    validation = Validation(project_root=args.project_root)
    
    print("=" * 60)
    print("Running Full Validation")
    print("=" * 60)
    
    # Validate rules
    print("\n[1/3] Validating rules...")
    rules_result = validation.validate_rules_against_wooldridge()
    print(f"  Validated {len(rules_result['rules_validated'])} rule files")
    print(f"  Alignments: {len([a for a in rules_result['alignments'].values() if a == 'high'])} high, "
          f"{len([a for a in rules_result['alignments'].values() if a == 'medium'])} medium, "
          f"{len([a for a in rules_result['alignments'].values() if a == 'low'])} low")
    if rules_result.get("gaps"):
        print(f"  Gaps found: {len(rules_result['gaps'])}")
    
    # Validate models
    print("\n[2/3] Validating models...")
    models_result = validation.validate_models_against_wooldridge()
    print(f"  Validated {len(models_result['models_validated'])} model files")
    print(f"  Alignments: {len([a for a in models_result['alignments'].values() if a == 'high'])} high, "
          f"{len([a for a in models_result['alignments'].values() if a == 'medium'])} medium, "
          f"{len([a for a in models_result['alignments'].values() if a == 'low'])} low")
    if models_result.get("gaps"):
        print(f"  Gaps found: {len(models_result['gaps'])}")
    
    # Check coverage
    print("\n[3/3] Checking methodology coverage...")
    coverage_result = validation.check_methodology_coverage()
    print(f"  Coverage: {coverage_result['coverage_percentage']:.1f}%")
    print(f"  Covered: {len(coverage_result['methodologies_covered'])} methodologies")
    print(f"  Missing: {len(coverage_result['methodologies_missing'])} methodologies")
    
    # Generate report if requested
    if args.output:
        print(f"\nGenerating validation report...")
        report_path = Path(args.output)
        validation.generate_validation_report(report_path)
        print(f"  Report saved to: {report_path}")
    else:
        print("\nUse --output to generate a full validation report")


def validate_rules(args):
    """Validate rule files against Wooldridge corpus."""
    validation = Validation(project_root=args.project_root)
    
    print("=" * 60)
    print("Validating Rules")
    print("=" * 60)
    
    rule_files = None
    if args.files:
        rule_files = [Path(f) for f in args.files]
    
    result = validation.validate_rules_against_wooldridge(rule_files)
    
    print(f"\nValidated {len(result['rules_validated'])} rule files:")
    for rule_file in result['rules_validated']:
        rule_name = Path(rule_file).name
        alignment = result['alignments'].get(rule_name, 'unknown')
        refs = result['wooldridge_references'].get(rule_name, [])
        print(f"  {rule_name}: {alignment} alignment ({len(refs)} Wooldridge references)")
    
    if result.get("gaps"):
        print(f"\nGaps identified: {len(result['gaps'])}")
        for gap in result['gaps'][:5]:
            print(f"  - {gap}")
        if len(result['gaps']) > 5:
            print(f"  ... and {len(result['gaps']) - 5} more")
    
    if args.output:
        import json
        output_path = Path(args.output)
        output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"\nResults saved to: {output_path}")


def validate_models(args):
    """Validate model implementations against Wooldridge corpus."""
    validation = Validation(project_root=args.project_root)
    
    print("=" * 60)
    print("Validating Models")
    print("=" * 60)
    
    model_files = None
    if args.files:
        model_files = [Path(f) for f in args.files]
    
    result = validation.validate_models_against_wooldridge(model_files)
    
    print(f"\nValidated {len(result['models_validated'])} model files:")
    for model_file in result['models_validated']:
        model_name = Path(model_file).stem
        alignment = result['alignments'].get(model_name, 'unknown')
        print(f"  {model_name}: {alignment} alignment")
    
    if result.get("gaps"):
        print(f"\nGaps identified: {len(result['gaps'])}")
        for gap in result['gaps'][:5]:
            print(f"  - {gap}")
        if len(result['gaps']) > 5:
            print(f"  ... and {len(result['gaps']) - 5} more")
    
    if args.output:
        import json
        output_path = Path(args.output)
        output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"\nResults saved to: {output_path}")


def validate_coverage(args):
    """Check methodology coverage against Wooldridge."""
    validation = Validation(project_root=args.project_root)
    
    print("=" * 60)
    print("Methodology Coverage Analysis")
    print("=" * 60)
    
    result = validation.check_methodology_coverage()
    
    print(f"\nCoverage: {result['coverage_percentage']:.1f}%")
    print(f"  Our methodologies: {result['total_our_methodologies']}")
    print(f"  Wooldridge methodologies: {result['total_wooldridge_methodologies']}")
    print(f"  Covered: {len(result['methodologies_covered'])}")
    print(f"  Missing: {len(result['methodologies_missing'])}")
    
    if result['methodologies_covered']:
        print(f"\nCovered methodologies:")
        for meth in result['methodologies_covered'][:10]:
            print(f"  ✓ {meth}")
        if len(result['methodologies_covered']) > 10:
            print(f"  ... and {len(result['methodologies_covered']) - 10} more")
    
    if result['methodologies_missing']:
        print(f"\nMissing methodologies:")
        for meth in result['methodologies_missing'][:10]:
            print(f"  ✗ {meth}")
        if len(result['methodologies_missing']) > 10:
            print(f"  ... and {len(result['methodologies_missing']) - 10} more")
    
    print(f"\nPriority coverage:")
    print(f"  Covered: {len(result['priority_covered'])}/{len(result['priority_covered']) + len(result['priority_missing'])}")
    if result['priority_missing']:
        print(f"  Missing: {', '.join(result['priority_missing'])}")
    
    if args.output:
        import json
        output_path = Path(args.output)
        output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"\nResults saved to: {output_path}")


def main():
    """Main CLI entry point for corpus operations."""
    parser = argparse.ArgumentParser(
        description="Wooldridge Corpus Tools - Search and analyze textbook content"
    )

    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path("."),
        help="Path to project root (default: current directory)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Build corpus command
    build_parser = subparsers.add_parser(
        "build", help="Build corpus from markdown files"
    )
    build_parser.set_defaults(func=build_corpus)

    # Search command
    search_parser = subparsers.add_parser(
        "search", help="Semantic search in corpus"
    )
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument(
        "--top-k", type=int, default=5, help="Number of results (default: 5)"
    )
    search_parser.set_defaults(func=search_corpus)

    # Lookup command
    lookup_parser = subparsers.add_parser(
        "lookup", help="Lookup topic in corpus"
    )
    lookup_parser.add_argument("topic", help="Topic to lookup")
    lookup_parser.add_argument(
        "--limit", type=int, default=10, help="Max results to show (default: 10)"
    )
    lookup_parser.set_defaults(func=lookup_topic)

    # Compare command
    compare_parser = subparsers.add_parser(
        "compare", help="Compare Wooldridge perspective with Hansen/Angrist"
    )
    compare_parser.add_argument(
        "methodology", help="Methodology to compare (e.g., 'fixed effects')"
    )
    compare_parser.set_defaults(func=compare_perspectives)

    # Find perspective command
    perspective_parser = subparsers.add_parser(
        "perspective", help="Find Wooldridge's perspective on a methodology"
    )
    perspective_parser.add_argument(
        "methodology", help="Methodology name (e.g., 'clustered standard errors')"
    )
    perspective_parser.add_argument(
        "--limit", type=int, default=5, help="Max results to show (default: 5)"
    )
    perspective_parser.set_defaults(func=find_perspective)

    # Validate all command
    validate_all_parser = subparsers.add_parser(
        "validate-all", help="Run full validation of rules and models"
    )
    validate_all_parser.add_argument(
        "--output", type=Path, help="Path to save validation report"
    )
    validate_all_parser.set_defaults(func=validate_all)

    # Validate rules command
    validate_rules_parser = subparsers.add_parser(
        "validate-rules", help="Validate rule files against Wooldridge corpus"
    )
    validate_rules_parser.add_argument(
        "--files", nargs="+", help="Specific rule files to validate (optional)"
    )
    validate_rules_parser.add_argument(
        "--output", type=Path, help="Path to save validation results (JSON)"
    )
    validate_rules_parser.set_defaults(func=validate_rules)

    # Validate models command
    validate_models_parser = subparsers.add_parser(
        "validate-models", help="Validate model implementations against Wooldridge corpus"
    )
    validate_models_parser.add_argument(
        "--files", nargs="+", help="Specific model files to validate (optional)"
    )
    validate_models_parser.add_argument(
        "--output", type=Path, help="Path to save validation results (JSON)"
    )
    validate_models_parser.set_defaults(func=validate_models)

    # Validate coverage command
    validate_coverage_parser = subparsers.add_parser(
        "validate-coverage", help="Check methodology coverage against Wooldridge"
    )
    validate_coverage_parser.add_argument(
        "--output", type=Path, help="Path to save coverage results (JSON)"
    )
    validate_coverage_parser.set_defaults(func=validate_coverage)

    # Parse arguments and execute
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()

