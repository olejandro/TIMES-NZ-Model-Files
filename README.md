# TIMES-NZ-Model-Files
## Model excel files for TIMES-NZ

Guide on getting started with the TIMES-NZ model stored here: https://github.com/EECA-NZ/TIMES-NZ-internal-guide-EECA

## Development
We recommend using a Python virtual environment:
```bash
python3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
After changing the TIMES-NZ model excel files, before you make a pull request, please run `times_excel_summary.py` in the utils subdirectory to generate a summary of the new model. This will help reviewers understand the changes made.
```bash
.venv/Scripts/Activate.ps1
cd utils
python .\raw_table_summary.py
```
Then commit changes and push to GitHub, and make a pull request.