#!/usr/bin/env python3
"""
Run predicTCR analysis locally on h5/csv files without the web UI.

This script mimics what the Docker runner does:
1. Creates a temporary working directory
2. Copies input files (input.h5, input.csv)
3. Creates result folders (user_results/, admin_results/, trusted_user_results/)
4. Runs the analysis script (script.sh or custom)
5. Reports results

Usage:
    python run_local.py path/to/file.h5 path/to/file.csv
    python run_local.py path/to/file.h5 path/to/file.csv --script custom_script.sh
    python run_local.py path/to/file.h5 path/to/file.csv --output ./my_results
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run_analysis(
    h5_path: Path, csv_path: Path, script_path: Path, output_dir: Path | None = None
):
    """Run the analysis script on the input files."""

    print("=" * 60)
    print("predicTCR Local Runner")
    print("=" * 60)

    # Validate inputs
    if not h5_path.exists():
        print(f"❌ H5 file not found: {h5_path}")
        sys.exit(1)
    if not csv_path.exists():
        print(f"❌ CSV file not found: {csv_path}")
        sys.exit(1)
    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        sys.exit(1)

    print(f"\n📁 Input files:")
    print(f"   H5:  {h5_path}")
    print(f"   CSV: {csv_path}")
    print(f"   Script: {script_path}")

    # Create working directory
    with tempfile.TemporaryDirectory(prefix="predictcr_") as tmpdir:
        workdir = Path(tmpdir)
        print(f"\n📂 Working directory: {workdir}")

        # Copy input files
        print("\n[1] Copying input files...")
        shutil.copy(h5_path, workdir / "input.h5")
        shutil.copy(csv_path, workdir / "input.csv")
        print(f"   ✅ Copied input.h5 ({h5_path.stat().st_size / 1e6:.2f} MB)")
        print(f"   ✅ Copied input.csv ({csv_path.stat().st_size / 1e3:.2f} KB)")

        # Create result folders
        print("\n[2] Creating result folders...")
        result_folders = ["user_results", "trusted_user_results", "admin_results"]
        for folder in result_folders:
            (workdir / folder).mkdir()
            print(f"   ✅ Created {folder}/")

        # Create job info (mimicking runner)
        job_info = {
            "job_id": 0,
            "sample_id": 0,
            "sample_name": h5_path.stem,
            "local_run": True,
        }
        with open(workdir / "input.json", "w") as f:
            json.dump(job_info, f, indent=2)
        print(f"   ✅ Created input.json")

        # Copy and run script
        print("\n[3] Running analysis script...")
        dest_script = workdir / "script.sh"
        shutil.copy(script_path, dest_script)
        dest_script.chmod(0o755)

        try:
            result = subprocess.run(
                ["./script.sh"],
                cwd=workdir,
                capture_output=True,
                text=True,
                timeout=3600,  # 1 hour timeout
            )

            print(f"\n--- Script output ---")
            if result.stdout:
                for line in result.stdout.strip().split("\n"):
                    print(f"   {line}")
            if result.stderr:
                print(f"   [stderr] {result.stderr}")
            print(f"--- End output ---")

            if result.returncode != 0:
                print(f"\n❌ Script failed with exit code {result.returncode}")
            else:
                print(f"\n✅ Script completed successfully")

        except subprocess.TimeoutExpired:
            print(f"\n❌ Script timed out after 1 hour")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Error running script: {e}")
            sys.exit(1)

        # Collect results
        print("\n[4] Collecting results...")

        # Determine output location
        if output_dir is None:
            output_dir = Path.cwd() / f"results_{h5_path.stem}"
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        for folder in result_folders:
            src = workdir / folder
            dst = output_dir / folder
            if any(src.iterdir()):  # Only copy if folder has content
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
                file_count = len(list(dst.rglob("*")))
                print(f"   ✅ {folder}/ ({file_count} files)")
            else:
                print(f"   ⚠️  {folder}/ (empty)")

        print(f"\n📁 Results saved to: {output_dir}")

    print("\n" + "=" * 60)
    print("✅ Done!")
    print("=" * 60)

    return 0 if result.returncode == 0 else 1


def main():
    parser = argparse.ArgumentParser(
        description="Run predicTCR analysis locally on h5/csv files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with sample data:
  python run_local.py data/adata_LN7_sample.h5 data/tcr_table_LN7.csv

  # Use a custom script:
  python run_local.py data/file.h5 data/file.csv --script my_analysis.sh

  # Specify output directory:
  python run_local.py data/file.h5 data/file.csv --output ./results
        """,
    )
    parser.add_argument(
        "h5_file", type=Path, help="Path to the H5 file (gene expression data)"
    )
    parser.add_argument("csv_file", type=Path, help="Path to the CSV file (TCR table)")
    parser.add_argument(
        "--script",
        "-s",
        type=Path,
        default=Path(__file__).parent / "runner" / "script" / "script.sh",
        help="Path to analysis script (default: runner/script/script.sh)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output directory for results (default: results_<h5_name>/)",
    )

    args = parser.parse_args()

    sys.exit(
        run_analysis(
            h5_path=args.h5_file.resolve(),
            csv_path=args.csv_file.resolve(),
            script_path=args.script.resolve(),
            output_dir=args.output.resolve() if args.output else None,
        )
    )


if __name__ == "__main__":
    main()
