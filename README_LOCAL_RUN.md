# Running predicTCR Analysis Locally

Run TCR analysis on your h5/csv files directly from the command line, without the web UI.

## Quick Start

```bash
# Run with sample data
python3 run_local.py data/adata_LN7_sample.h5 data/tcr_table_LN7.csv

# Results saved to: results_adata_LN7_sample/
```

## Usage

```bash
python3 run_local.py <h5_file> <csv_file> [options]
```

### Options

| Option | Description |
|--------|-------------|
| `--script`, `-s` | Path to analysis script (default: `runner/script/script.sh`) |
| `--output`, `-o` | Output directory (default: `results_<h5_name>/`) |

### Examples

```bash
# Custom output directory
python3 run_local.py data/file.h5 data/file.csv --output ./my_results

# Use a custom analysis script
python3 run_local.py data/file.h5 data/file.csv --script my_analysis.sh
```

## Input Files

The script expects:

1. **H5 file** - Gene expression data (HDF5/AnnData format)
2. **CSV file** - TCR table with columns: `barcode`, `cdr3`, `chain`

## Output

Results are saved to three folders:

- `user_results/` - Results for the submitting user
- `trusted_user_results/` - Results for trusted users
- `admin_results/` - Admin-only results

## Creating a Custom Analysis Script

Your script should:

1. Read `input.h5` and `input.csv` from the working directory
2. Optionally read `input.json` for job metadata
3. Write results to `user_results/`, `trusted_user_results/`, and/or `admin_results/`

Example `my_analysis.sh`:

```bash
#!/bin/bash
echo "Running analysis..."

# Your analysis code here
# Input files: input.h5, input.csv, input.json
# Output dirs: user_results/, trusted_user_results/, admin_results/

echo "Done!"
```

## Validating Sample Files

Check if your input files are valid:

```bash
python3 data/validate_samples.py
```
