# AI-Based Quality of Life Assessment for Type 2 Diabetes

A research-oriented machine-learning project to study and estimate health-related quality of life (HRQoL) among adults with Type 2 Diabetes.

## Current status
This is the initial project scaffold. No patient data or model results are included yet. The target variable and prediction task will be selected only after the real dataset and its codebook are reviewed.

## Setup
1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Put an approved, de-identified dataset in `data/raw/`.
5. Start the app: `streamlit run app.py`

## Data privacy
Do not put names, phone numbers, addresses, national IDs, hospital numbers, or other direct identifiers in the dataset. Use only data that you are authorized to process. Keep raw data private and do not commit it to Git.

## Project structure
- `data/raw/`: original de-identified dataset (not tracked by Git)
- `data/processed/`: cleaned dataset (not tracked by Git)
- `notebooks/`: analysis notebooks
- `src/`: reusable data and modelling code
- `reports/`: figures and reports
- `models/`: trained model artifacts

## Important research note
This software is for research and educational purposes. Predictions are not medical diagnoses or treatment recommendations. We will avoid claiming clinical validity without suitable validation.
