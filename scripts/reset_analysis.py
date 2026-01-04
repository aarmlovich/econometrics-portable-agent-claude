#!/usr/bin/env python3
"""
Reset analysis outputs to clean state before re-running models.

This script removes generated outputs to prevent pollution from previous
analysis runs when modifying models mid-workflow.

Cleans:
- All files in data/outputs/
- Common transient files in project root (*.png, *.pdf, *results*.csv, etc.)
- Cache files (*.pyc, __pycache__, .pytest_cache)
"""

import sys
from pathlib import Path
from typing import List


def find_files_to_delete(project_root: Path) -> List[Path]:
    """Find all files that should be deleted for a clean reset.
    
    Args:
        project_root: Path to project root directory
        
    Returns:
        List of file paths to delete
    """
    files_to_delete = []
    
    # Outputs directory (exclude .gitkeep)
    outputs_dir = project_root / "data" / "outputs"
    if outputs_dir.exists():
        for file in outputs_dir.rglob("*"):
            if file.is_file() and file.name != ".gitkeep":
                files_to_delete.append(file)
    
    # Common transient files in project root (analysis outputs only)
    transient_patterns = [
        "*.png",  # Figures
        "*results*.csv",  # Result files
        "*results*.xlsx",
        "*output*.csv",
        "*output*.xlsx",
        "*diagnostics*.png",
        "*plot*.png",
        "*figure*.png",
        "*table*.csv",
        "*table*.xlsx",
    ]
    # Note: Not deleting *.pdf or *.html to preserve reference documents
    
    for pattern in transient_patterns:
        for file in project_root.glob(pattern):
            if file.is_file():
                files_to_delete.append(file)
    
    # Cache directories
    cache_dirs = [
        project_root / "__pycache__",
        project_root / ".pytest_cache",
        project_root / ".mypy_cache",
    ]
    
    for cache_dir in cache_dirs:
        if cache_dir.exists():
            for file in cache_dir.rglob("*"):
                if file.is_file():
                    files_to_delete.append(file)
    
    return files_to_delete


def reset_analysis(project_root: Path = None, dry_run: bool = False) -> dict:
    """Reset analysis outputs to clean state.
    
    Args:
        project_root: Path to project root. Defaults to current directory.
        dry_run: If True, only list files without deleting (for testing)
        
    Returns:
        Dictionary with:
            - files_deleted: Number of files deleted
            - directories_cleaned: List of directories cleaned
            - errors: List of error messages
    """
    if project_root is None:
        project_root = Path(".")
    else:
        project_root = Path(project_root)
    
    files_to_delete = find_files_to_delete(project_root)
    directories_cleaned = set()
    errors = []
    files_deleted = 0
    
    if dry_run:
        print(f"DRY RUN: Would delete {len(files_to_delete)} files")
        for file in files_to_delete:
            print(f"  Would delete: {file}")
        return {
            "files_deleted": len(files_to_delete),
            "directories_cleaned": [],
            "errors": [],
        }
    
    # Delete files
    for file_path in files_to_delete:
        try:
            file_path.unlink()
            files_deleted += 1
            directories_cleaned.add(str(file_path.parent))
        except Exception as e:
            errors.append(f"Error deleting {file_path}: {e}")
    
    # Remove empty cache directories
    cache_dirs = [
        project_root / "__pycache__",
        project_root / ".pytest_cache",
        project_root / ".mypy_cache",
    ]
    
    for cache_dir in cache_dirs:
        if cache_dir.exists():
            try:
                # Remove all files first (already done above)
                # Now remove directory if empty
                if not any(cache_dir.rglob("*")):
                    cache_dir.rmdir()
                    directories_cleaned.add(str(cache_dir))
            except Exception as e:
                errors.append(f"Error removing {cache_dir}: {e}")
    
    return {
        "files_deleted": files_deleted,
        "directories_cleaned": sorted(list(directories_cleaned)),
        "errors": errors,
    }


def main():
    """Main execution function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Reset analysis outputs to clean state"
    )
    parser.add_argument(
        "--project-root",
        type=str,
        default=None,
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deleted without actually deleting"
    )
    
    args = parser.parse_args()
    
    project_root = Path(args.project_root) if args.project_root else Path(".")
    
    print("=" * 70)
    print("Reset Analysis Outputs")
    print("=" * 70)
    print(f"\nProject root: {project_root.absolute()}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'DELETE'}")
    print()
    
    result = reset_analysis(project_root, dry_run=args.dry_run)
    
    if args.dry_run:
        print(f"\nWould delete {result['files_deleted']} files")
    else:
        print(f"\nDeleted {result['files_deleted']} files")
        
        if result['directories_cleaned']:
            print(f"\nCleaned {len(result['directories_cleaned'])} directories:")
            for dir_path in result['directories_cleaned'][:10]:  # Show first 10
                print(f"  - {dir_path}")
            if len(result['directories_cleaned']) > 10:
                print(f"  ... and {len(result['directories_cleaned']) - 10} more")
        
        if result['errors']:
            print(f"\n⚠ Errors encountered ({len(result['errors'])}):")
            for error in result['errors'][:5]:  # Show first 5 errors
                print(f"  - {error}")
            if len(result['errors']) > 5:
                print(f"  ... and {len(result['errors']) - 5} more errors")
        
        print("\n✅ Analysis reset complete!")
        print("\nYou can now re-run your models without interference from previous outputs.")
    
    print()
    
    if result['errors']:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
