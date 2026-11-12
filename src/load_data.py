from pathlib import Path
import pandas as pd

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}

def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV or Excel dataset without assuming its column names."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")
