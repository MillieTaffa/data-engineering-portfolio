"""
validate.py

Responsibility: check whether the raw data can be trusted before we
process it further.

Important: this file does NOT fix any problems it finds. It only
detects and reports them. Fixing problems is the job of clean.py.
Keeping "finding problems" and "fixing problems" separate makes both
files much easier to read, test, and reason about.
"""

import pandas as pd

from src import config


def check_missing_columns(data):
    """Returns a list of required columns that are missing from the DataFrame."""
    missing = []
    for column in config.REQUIRED_COLUMNS:
        if column not in data.columns:
            missing.append(column)
    return missing


def check_missing_values(data):
    """Returns a pandas Series: how many missing (NaN) values are in each column."""
    return data.isnull().sum()


def check_duplicate_ids(data):
    """Returns the number of duplicate Post_ID values."""
    return int(data["Post_ID"].duplicated().sum())


def check_duplicate_rows(data):
    """Returns the number of fully duplicated rows (every column identical)."""
    return int(data.duplicated().sum())


def check_invalid_dates(data):
    """Returns the number of rows where Timestamp cannot be parsed as a real date/time."""
    parsed_timestamps = pd.to_datetime(data["Timestamp"], errors="coerce")
    return int(parsed_timestamps.isnull().sum())


def check_negative_numbers(data):
    """
    Returns a dictionary of {column_name: number_of_negative_values} for every
    numeric column that should never contain a negative number.
    """
    negative_counts = {}
    for column in config.NUMERIC_COLUMNS:
        if column in data.columns:
            negative_counts[column] = int((data[column] < 0).sum())
    return negative_counts


def check_hour_of_day_range(data):
    """Returns the number of rows where Hour_of_Day is not between 0 and 23."""
    out_of_range = (data["Hour_of_Day"] < 0) | (data["Hour_of_Day"] > 23)
    return int(out_of_range.sum())


def check_unexpected_categories(data):
    """
    Compares Platform, Day_of_Week, Sentiment, and Influencer_Tier against
    the expected value lists in config.py.
    Returns a dictionary of {column_name: [unexpected values found]}.
    """
    unexpected = {}

    unexpected["Platform"] = list(
        data.loc[~data["Platform"].isin(config.EXPECTED_PLATFORMS), "Platform"].unique()
    )
    unexpected["Day_of_Week"] = list(
        data.loc[~data["Day_of_Week"].isin(config.EXPECTED_DAYS), "Day_of_Week"].unique()
    )
    unexpected["Sentiment"] = list(
        data.loc[~data["Sentiment"].isin(config.EXPECTED_SENTIMENTS), "Sentiment"].unique()
    )
    unexpected["Influencer_Tier"] = list(
        data.loc[~data["Influencer_Tier"].isin(config.EXPECTED_TIERS), "Influencer_Tier"].unique()
    )

    return unexpected


def check_timestamp_consistency(data):
    """
    The raw dataset already includes Hour_of_Day and Day_of_Week columns.
    This checks whether those columns actually match what Timestamp says,
    since a data-entry mistake could make them disagree.
    Returns a dictionary with the number of mismatched rows for each check.
    """
    parsed_timestamps = pd.to_datetime(data["Timestamp"], errors="coerce")
    hour_mismatches = int((parsed_timestamps.dt.hour != data["Hour_of_Day"]).sum())
    day_mismatches = int((parsed_timestamps.dt.day_name() != data["Day_of_Week"]).sum())
    return {"hour_mismatches": hour_mismatches, "day_mismatches": day_mismatches}


def run_validation(data):
    """
    Runs every validation check and prints a validation report.
    Returns a dictionary containing all of the results, so other code
    (like the pipeline or the tests) can use the results directly instead
    of re-parsing the printed report.
    """
    report = {
        "missing_columns": check_missing_columns(data),
        "missing_values": check_missing_values(data),
        "duplicate_ids": check_duplicate_ids(data),
        "duplicate_rows": check_duplicate_rows(data),
        "invalid_dates": check_invalid_dates(data),
        "negative_numbers": check_negative_numbers(data),
        "hour_out_of_range": check_hour_of_day_range(data),
        "unexpected_categories": check_unexpected_categories(data),
        "timestamp_consistency": check_timestamp_consistency(data),
    }

    print("Validation Report")
    print("-----------------")
    print(f"Missing columns: {report['missing_columns']}")
    print(f"Missing values (total across all columns): {int(report['missing_values'].sum())}")
    print(f"Duplicate Post_IDs: {report['duplicate_ids']}")
    print(f"Fully duplicated rows: {report['duplicate_rows']}")
    print(f"Invalid dates: {report['invalid_dates']}")
    print(f"Negative values by column: {report['negative_numbers']}")
    print(f"Hour_of_Day values out of range: {report['hour_out_of_range']}")
    print(f"Unexpected category values: {report['unexpected_categories']}")
    print(f"Hour_of_Day / Day_of_Week mismatches vs Timestamp: {report['timestamp_consistency']}")

    return report


if __name__ == "__main__":
    from src.ingest import load_raw_data

    raw_data = load_raw_data()
    run_validation(raw_data)