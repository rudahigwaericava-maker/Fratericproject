import pandas as pd

def dataset_overview(df: pd.DataFrame) -> dict:
    """Return basic structural checks; does not alter the source data."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_by_column": df.isna().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }
