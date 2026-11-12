import pandas as pd

def basic_cleaning_copy(df: pd.DataFrame) -> pd.DataFrame:
    """Make a safe working copy and standardize column-name whitespace.

    This intentionally does not impute values, remove outliers, or drop rows.
    Those decisions depend on the real dataset, study protocol, and outcome.
    """
    cleaned = df.copy()
    cleaned.columns = [str(col).strip() for col in cleaned.columns]
    return cleaned
