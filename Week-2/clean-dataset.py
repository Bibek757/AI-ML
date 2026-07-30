
"""
clean_dataset.py

Cleans a messy raw CSV into an analysis-ready CSV.
Usage: python clean_dataset.py raw_data.csv cleaned_data.csv
"""

import sys
import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Standardize column names: lowercase, no spaces
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 2. Drop columns that are almost entirely empty (>50% missing)
    threshold = len(df) * 0.5
    df = df.dropna(axis=1, thresh=threshold)

    # 3. Fill remaining missing values
    for col in df.columns:
        if not df[col].isnull().any():
            continue
        if pd.api.types.is_numeric_dtype(df[col]):
            # numeric column -> fill with median (robust to outliers)
            df[col] = df[col].fillna(df[col].median())
        else:
            # text column -> fill with most frequent value
            df[col] = df[col].fillna(df[col].mode()[0])

    # 4. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 5. Strip whitespace from text values, fix inconsistent casing
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip().str.lower()

    # 6. Reset index after all the row drops above
    df = df.reset_index(drop=True)

    return df


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_dataset.py <input.csv> <output.csv>")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]

    raw_df = pd.read_csv(input_path)
    print("Raw shape:", raw_df.shape)

    clean_df = clean(raw_df)
    print("Cleaned shape:", clean_df.shape)

    clean_df.to_csv(output_path, index=False)
    print("Saved:", output_path)