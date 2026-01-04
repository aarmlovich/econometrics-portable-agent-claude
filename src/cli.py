"""Command-line interface for econometrics agent."""

import argparse
import sys
from pathlib import Path
from typing import Optional
import pandas as pd
import numpy as np
import json

from src import __version__
from src.data.loaders import load_data, validate_data_structure
from src.models.regression.ols import OLSRegression
from src.models.causal.diff_in_diff import DifferenceInDifferences
from src.models.causal.regression_discontinuity import RegressionDiscontinuity
from src.models.causal.matching import Matching
from src.models.causal.instrumental_variables import InstrumentalVariables
from src.models.panel.fixed_effects import FixedEffects
from src.models.panel.random_effects import RandomEffects
from src.models.panel.panel_iv import PanelIV

# Global verbosity flag
VERBOSE = True


def run_analysis(args):
    """Run econometric analysis based on method specified."""
    global VERBOSE
    VERBOSE = not args.quiet

    # Load data
    if VERBOSE:
        print(f"Loading data from {args.data}...")
    data = load_data(args.data)
    if VERBOSE:
        print(f"Loaded {len(data)} observations with {len(data.columns)} variables.")
    
    # Run analysis based on method
    if args.method == 'ols':
        if not args.outcome or not args.covariates:
            print("Error: --outcome and --covariates required for OLS")
            sys.exit(1)
        
        # Determine HC type (use HC1 if robust, None if --no-robust specified)
        hc_type = 'HC1' if args.robust else None
        
        model = OLSRegression(
            data=data,
            outcome=args.outcome,
            covariates=args.covariates,
            hc_type=hc_type
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        # Save results if output specified
        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float, np.integer, np.floating))
                          else v.tolist() if hasattr(v, 'tolist') else str(v)
                          for k, v in results.items()}, f, indent=2)
            if VERBOSE:
                print(f"\nResults saved to {args.output}")
    
    elif args.method == 'did':
        if not all([args.outcome, args.treatment, args.time, args.unit]):
            print("Error: --outcome, --treatment, --time, and --unit required for DiD")
            sys.exit(1)
        
        model = DifferenceInDifferences(
            data=data,
            outcome=args.outcome,
            treatment=args.treatment,
            time=args.time,
            unit=args.unit,
            treatment_period=args.treatment_period
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        # Test parallel trends
        if VERBOSE:
            try:
                trends = model.test_parallel_trends()
                print("\nParallel Trends Test:")
                print(f"  P-value: {trends['pvalue']:.4f}")
                print(f"  {trends['interpretation']}")
            except Exception as e:
                print(f"\nCould not run parallel trends test: {e}")

        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float)) else str(v)
                          for k, v in results.items()}, f, indent=2)
            if VERBOSE:
                print(f"\nResults saved to {args.output}")
    
    elif args.method == 'fe':
        if not all([args.outcome, args.entity, args.time]):
            print("Error: --outcome, --entity, and --time required for fixed effects")
            sys.exit(1)
        
        covariates = args.covariates if args.covariates else []
        model = FixedEffects(
            data=data,
            outcome=args.outcome,
            covariates=covariates,
            entity=args.entity,
            time=args.time,
            entity_effects=True,
            time_effects=args.time_effects
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        if args.output:
            with open(args.output, 'w') as f:
                def convert_value(v):
                    if isinstance(v, (int, float, np.integer, np.floating)):
                        return float(v)
                    elif hasattr(v, 'tolist'):
                        return v.tolist()
                    else:
                        return str(v)
                json.dump({k: convert_value(v) for k, v in results.items()}, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    elif args.method == 'rd':
        if not all([args.outcome, args.running, args.cutoff is not None]):
            print("Error: --outcome, --running, and --cutoff required for RD")
            sys.exit(1)
        
        model = RegressionDiscontinuity(
            data=data,
            outcome=args.outcome,
            running=args.running,
            cutoff=float(args.cutoff),
            bandwidth=float(args.bandwidth) if args.bandwidth else None,
            polynomial=args.polynomial if args.polynomial else 1,
            covariates=args.covariates if args.covariates else None
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        # Run manipulation test
        if VERBOSE:
            try:
                manipulation = model.test_manipulation()
                print("\nManipulation Test (McCrary):")
                print(f"  Test statistic: {manipulation.get('test_statistic', 'N/A')}")
                print(f"  P-value: {manipulation.get('pvalue', 'N/A')}")
                print(f"  {manipulation.get('interpretation', 'N/A')}")
            except Exception as e:
                print(f"\nCould not run manipulation test: {e}")

        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float)) else str(v)
                          for k, v in results.items()}, f, indent=2)
            if VERBOSE:
                print(f"\nResults saved to {args.output}")
    
    elif args.method == 'matching':
        if not all([args.outcome, args.treatment, args.covariates]):
            print("Error: --outcome, --treatment, and --covariates required for matching")
            sys.exit(1)
        
        model = Matching(
            data=data,
            outcome=args.outcome,
            treatment=args.treatment,
            covariates=args.covariates,
            matching_method=args.matching_method if args.matching_method else 'nearest_neighbor',
            trim_support=args.trim_support if args.trim_support else True
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float)) else str(v)
                          for k, v in results.items()}, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    elif args.method == 'iv':
        if not all([args.outcome, args.treatment, args.instruments]):
            print("Error: --outcome, --treatment, and --instruments required for IV")
            sys.exit(1)
        
        model = InstrumentalVariables(
            data=data,
            outcome=args.outcome,
            treatment=args.treatment,
            instruments=args.instruments,
            covariates=args.covariates if args.covariates else None,
            hc_type=args.hc_type if args.hc_type else 'HC1'
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float)) else str(v)
                          for k, v in results.items()}, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    elif args.method == 're':
        if not all([args.outcome, args.entity, args.time, args.covariates]):
            print("Error: --outcome, --entity, --time, and --covariates required for random effects")
            sys.exit(1)
        
        model = RandomEffects(
            data=data,
            outcome=args.outcome,
            covariates=args.covariates,
            entity=args.entity,
            time=args.time,
            cluster_se=args.cluster_se if args.cluster_se else True
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        if args.output:
            with open(args.output, 'w') as f:
                def convert_value(v):
                    if isinstance(v, (int, float, np.integer, np.floating)):
                        return float(v)
                    elif hasattr(v, 'tolist'):
                        return v.tolist()
                    else:
                        return str(v)
                json.dump({k: convert_value(v) for k, v in results.items()}, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    elif args.method == 'panel_iv':
        if not all([args.outcome, args.treatment, args.instruments, args.entity, args.time]):
            print("Error: --outcome, --treatment, --instruments, --entity, and --time required for panel IV")
            sys.exit(1)
        
        model = PanelIV(
            data=data,
            outcome=args.outcome,
            treatment=args.treatment,
            instruments=args.instruments,
            entity=args.entity,
            time=args.time,
            covariates=args.covariates if args.covariates else None,
            entity_effects=args.entity_effects if args.entity_effects else True,
            time_effects=args.time_effects if args.time_effects else True
        )
        results = model.estimate()
        print("\n" + model.summary())
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump({k: float(v) if isinstance(v, (int, float)) else str(v)
                          for k, v in results.items()}, f, indent=2)
            print(f"\nResults saved to {args.output}")
    
    else:
        print(f"Error: Unknown method '{args.method}'")
        print("Supported methods: ols, did, fe, rd, matching, iv, re, panel_iv")
        sys.exit(1)


def validate_data(args):
    """Validate data structure."""
    global VERBOSE
    VERBOSE = not getattr(args, 'quiet', False)

    if VERBOSE:
        print(f"Loading data from {args.data}...")
    data = load_data(args.data)

    required_cols = args.columns if args.columns else []
    validation = validate_data_structure(
        data=data,
        required_columns=required_cols,
        min_observations=args.min_obs
    )

    if validation['valid']:
        print("✓ Data validation passed!")
        if VERBOSE:
            print(f"  Observations: {len(data)}")
            print(f"  Variables: {len(data.columns)}")
    else:
        print("✗ Data validation failed!")
        print("  Issues found:")
        for issue in validation['issues']:
            print(f"    - {issue}")
        sys.exit(1)


def generate_report(args):
    """Generate analysis report from results."""
    print("Report generation not yet implemented.")
    print("This feature will generate formatted reports from analysis results.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Econometrics Agent - Applied Microeconometrics Tools"
    )

    # Add global flags
    parser.add_argument('--version', action='version',
                       version=f'Econometrics Agent v{__version__}',
                       help='Show version information and exit')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run analysis command
    run_parser = subparsers.add_parser('run-analysis', help='Run econometric analysis')
    run_parser.add_argument('--method', required=True, 
                           choices=['ols', 'did', 'fe', 'rd', 'matching', 'iv', 're', 'panel_iv'],
                           help='Analysis method')
    run_parser.add_argument('--data', required=True, help='Path to data file')
    run_parser.add_argument('--output', help='Path to save results (JSON)')
    run_parser.add_argument('--outcome', help='Outcome variable name')
    run_parser.add_argument('--covariates', nargs='+', help='Covariate variable names')
    run_parser.add_argument('--treatment', help='Treatment variable (for DiD)')
    run_parser.add_argument('--time', help='Time variable (for DiD/panel)')
    run_parser.add_argument('--unit', help='Unit identifier (for DiD)')
    run_parser.add_argument('--entity', help='Entity identifier (for panel)')
    run_parser.add_argument('--treatment-period', type=int, help='Treatment period (for DiD)')
    run_parser.add_argument('--robust', action=argparse.BooleanOptionalAction, default=True,
                           help='Use robust standard errors (use --no-robust to disable)')
    run_parser.add_argument('--time-effects', action='store_true', default=True,
                           help='Include time fixed effects (for FE/panel_iv)')
    run_parser.add_argument('--quiet', action='store_true', default=False,
                           help='Suppress verbose output')
    run_parser.add_argument('--running', help='Running variable (for RD)')
    run_parser.add_argument('--cutoff', type=float, help='Cutoff value (for RD)')
    run_parser.add_argument('--bandwidth', type=float, help='Bandwidth (for RD, optional)')
    run_parser.add_argument('--polynomial', type=int, default=1, help='Polynomial order (for RD, default=1)')
    run_parser.add_argument('--instruments', nargs='+', help='Instrument variables (for IV/panel_iv)')
    run_parser.add_argument('--hc-type', choices=['HC1', 'HC2', 'HC3'], default='HC1',
                           help='Heteroskedasticity-consistent SE type (for IV)')
    run_parser.add_argument('--matching-method', choices=['nearest_neighbor', 'kernel', 'radius'],
                           default='nearest_neighbor', help='Matching algorithm (for matching)')
    run_parser.add_argument('--trim-support', action='store_true', default=True,
                           help='Trim common support (for matching)')
    run_parser.add_argument('--cluster-se', action='store_true', default=True,
                           help='Cluster standard errors (for RE)')
    run_parser.add_argument('--entity-effects', action='store_true', default=True,
                           help='Include entity fixed effects (for panel_iv)')
    run_parser.set_defaults(func=run_analysis)
    
    # Validate data command
    validate_parser = subparsers.add_parser('validate-data', help='Validate data structure')
    validate_parser.add_argument('--data', required=True, help='Path to data file')
    validate_parser.add_argument('--columns', nargs='+', help='Required column names')
    validate_parser.add_argument('--min-obs', type=int, default=10,
                                help='Minimum number of observations')
    validate_parser.add_argument('--quiet', action='store_true', default=False,
                                help='Suppress verbose output')
    validate_parser.set_defaults(func=validate_data)
    
    # Generate report command
    report_parser = subparsers.add_parser('generate-report', 
                                         help='Generate analysis report')
    report_parser.add_argument('--results', required=True, 
                              help='Path to results file (JSON)')
    report_parser.add_argument('--output', required=True, 
                              help='Path to save report')
    report_parser.set_defaults(func=generate_report)
    
    # Parse arguments and execute
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()

