"""
Module 3 — Reusable utility functions (SOLUTION)

Reference implementation for the lab "Creating Reusable Functions".

This module demonstrates:
- validating structured records (list[dict])
- standardising keys for consistency
- using Pandas inside functions (lightweight, function-based cleaning)
- handling missing values
- flagging simple outliers
- producing small, reusable summaries
- composing a clean, testable pipeline

Note:
This solution is intentionally readable and beginner-friendly.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

import pandas as pd


def validate_records(records: Any) -> bool:
    """Validate that `records` is a non-empty list of dictionaries.

    Raises AssertionError with a helpful message if validation fails.
    """
    assert isinstance(records, list), "records must be a list"
    assert len(records) > 0, "records must not be empty"
    assert all(isinstance(r, dict) for r in records), "each record must be a dictionary"
    return True


def _standardise_key(key: Any) -> str:
    """Standardise a single key: strip whitespace, lowercase, spaces -> underscores."""
    return str(key).strip().lower().replace(" ", "_")


def standardise_keys(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return a NEW list of records with standardised keys.

    - Does not mutate the original list/dicts.
    - Ensures downstream functions can rely on consistent column names.
    """
    validate_records(records)

    standardised: List[Dict[str, Any]] = []
    for record in records:
        new_record: Dict[str, Any] = {}
        for k, v in record.items():
            new_record[_standardise_key(k)] = v
        standardised.append(new_record)

    return standardised


def to_dataframe(records: List[Dict[str, Any]]) -> pd.DataFrame:
    """Convert records to a DataFrame using standardised keys."""
    cleaned = standardise_keys(records)
    df = pd.DataFrame(cleaned)
    assert len(df) > 0, "DataFrame is empty after conversion"
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in a simple, explicit way.

    Rules (lab):
    - For `value`: drop rows where `value` is missing (NaN/None)
    - For `category`: fill missing with 'unknown'

    Returns a new DataFrame.
    """
    assert isinstance(df, pd.DataFrame), "df must be a Pandas DataFrame"
    assert "value" in df.columns, "Expected a 'value' column"
    assert "category" in df.columns, "Expected a 'category' column"

    df2 = df.copy()

    # Drop rows with missing `value`
    df2 = df2.dropna(subset=["value"])

    # Fill missing categories
    df2["category"] = df2["category"].fillna("unknown")

    # Post-conditions
    assert df2["value"].isna().sum() == 0, "Missing values remain in 'value' after cleaning"
    assert df2["category"].isna().sum() == 0, "Missing values remain in 'category' after cleaning"

    return df2


def flag_outliers(df: pd.DataFrame, threshold: float = 100) -> pd.DataFrame:
    """Add an `is_outlier` boolean column where `value` > threshold.

    This uses a simple rule-based approach appropriate for introductory labs.
    """
    assert isinstance(df, pd.DataFrame), "df must be a Pandas DataFrame"
    assert "value" in df.columns, "Expected a 'value' column"
    assert isinstance(threshold, (int, float)), "threshold must be a number"

    df2 = df.copy()
    df2["is_outlier"] = df2["value"] > float(threshold)
    return df2


def summarise_values(df: pd.DataFrame) -> Dict[str, float]:
    """Return summary statistics for the `value` column.

    Returns:
        dict with keys: count, mean, min, max
    """
    assert isinstance(df, pd.DataFrame), "df must be a Pandas DataFrame"
    assert "value" in df.columns, "Expected a 'value' column"
    assert len(df) > 0, "DataFrame must contain at least one row"

    s = df["value"]

    summary: Dict[str, float] = {
        "count": float(s.count()),
        "mean": float(s.mean()),
        "min": float(s.min()),
        "max": float(s.max()),
    }
    return summary


def run_pipeline(records: List[Dict[str, Any]], threshold: float = 100) -> Tuple[pd.DataFrame, Dict[str, float]]:
    """Run the full cleaning + summarising workflow.

    Steps:
    1) Convert records to DataFrame
    2) Handle missing values
    3) Flag simple outliers
    4) Summarise numeric values

    Returns:
        (cleaned_df, summary_dict)
    """
    df = to_dataframe(records)
    df = handle_missing(df)
    df = flag_outliers(df, threshold=threshold)
    summary = summarise_values(df)
    return df, summary
