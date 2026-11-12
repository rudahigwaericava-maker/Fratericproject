from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def save_missingness_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    missing = df.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0]
    if missing.empty:
        return
    plt.figure(figsize=(10, max(4, len(missing) * 0.35)))
    sns.barplot(x=missing.values, y=missing.index)
    plt.xlabel("Number of missing values")
    plt.ylabel("Column")
    plt.title("Missing values by column")
    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()
