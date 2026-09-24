"""
clean.py

Responsibility: fix the problems that validate.py can detect.

Cleaning rules used in this project
------------------------------------

1. Duplicate rows / duplicate Post_ID
   Problem  -> the same post appears more than once.
   Decision -> keep the first occurrence, drop the rest.

2. Missing required values
   Problem  -> a required column is empty for some row.
   Decision -> drop the row. A social media post with no platform or no
               view count cannot be analysed reliably.

3. Invalid Timestamp values
   Problem  -> Timestamp cannot be understood as a real date and time.
   Decision -> drop the row, since we cannot plot or group a post we
               cannot place in time.

4. Negative numeric values
   Problem  -> a metric such as Likes or Views is negative.
   Decision -> drop the row. A negative number of likes or views is not
               physically possible, so we treat it as corrupted data
               rather than guessing a "correct" value.

5. Inconsistent text casing
   Problem  -> the same category is written in different ways, e.g.
               "instagram", "Instagram", "INSTAGRAM".
   Decision -> strip extra whitespace and convert to Title Case, so every
               spelling of a category becomes one consistent value.

6. Hour_of_Day / Day_of_Week
   Decision -> instead of trusting the raw columns, these are recalculated
               directly from Timestamp after it has been cleaned. This
               guarantees they always match the post's actual date, even
               if the original values were wrong.

Note: when this project's own dataset was inspected, none of these
problems were actually present (see docs/DATA_DICTIONARY.md for the
full inspection results). The functions below are still written to
handle every case correctly - the automated tests in
tests/test_clean.py build small, deliberately messy datasets to prove
that.
"""

import pandas as pd
from src import config

def remove_duplicates(data):
    """Removes fully duplicated rows and rows with a repeated Post_ID."""
    data = data.drop_duplicates()
    data = data.drop_duplicates(subset="Post_ID", keep="first")
    return data


def handle_missing_values(data):
    """Drops any row that is missing a value in a required column."""
    data = data.dropna(subset=config.REQUIRED_COLUMNS)
    return data


def fix_invalid_dates(data):
    """Converts Timestamp to a real datetime column and drops rows that fail to parse."""
    data = data.copy()
    data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")
    data = data.dropna(subset=["Timestamp"])
    return data


def remove_negative_values(data):
    """Drops any row that has a negative value in a metric column."""
    for column in config.NUMERIC_COLUMNS:
        if column in data.columns:
            data = data[data[column] >= 0]
    return data


def standardize_text_columns(data):
    """
    Cleans up spacing and casing in text columns so values are consistent.

    Plain Title Case does not work for every value in this dataset - for
    example "tiktok".title() gives "Tiktok" instead of "TikTok", and
    "mid-tier".title() gives "Mid-Tier" instead of "Mid-tier". So for
    columns that have a fixed, known list of values (config.py), each
    value is matched against that list case-insensitively and replaced
    with the correct spelling. Columns without a fixed list just get
    whitespace stripped and Title Case applied as a best effort.
    """
    data = data.copy()

    # Columns where we know the exact, correctly-cased values in advance.
    canonical_value_lists = {
        "Platform": config.EXPECTED_PLATFORMS,
        "Sentiment": config.EXPECTED_SENTIMENTS,
        "Influencer_Tier": config.EXPECTED_TIERS,
    }

    for column, canonical_values in canonical_value_lists.items():
        if column in data.columns:
            # Build a lookup from lowercase value -> correctly-cased value,
            # e.g. "tiktok" -> "TikTok".
            lookup = {value.lower(): value for value in canonical_values}
            stripped = data[column].astype(str).str.strip()
            data[column] = stripped.apply(lambda value: lookup.get(value.lower(), value.title()))

    # Content_Type and Category do not have internal capitals like "TikTok"
    # does, so a simple strip + Title Case is enough to fix them.
    simple_columns = ["Content_Type", "Category"]
    for column in simple_columns:
        if column in data.columns:
            data[column] = data[column].astype(str).str.strip().str.title()

    return data


def recalculate_time_columns(data):
    """
    Recalculates Hour_of_Day and Day_of_Week directly from Timestamp.
    Timestamp must already be a real datetime column when this runs
    (fix_invalid_dates takes care of that earlier in the pipeline).
    """
    data = data.copy()
    data["Hour_of_Day"] = data["Timestamp"].dt.hour
    data["Day_of_Week"] = data["Timestamp"].dt.day_name()
    return data


def clean_data(data):
    """
    Runs every cleaning step in order and returns a clean DataFrame.
    """
    print("Cleaning data...")
    rows_before = len(data)

    data = remove_duplicates(data)
    data = handle_missing_values(data)
    data = fix_invalid_dates(data)
    data = remove_negative_values(data)
    data = standardize_text_columns(data)
    data = recalculate_time_columns(data)

    data = data.reset_index(drop=True)

    rows_after = len(data)
    print(f"Rows before cleaning: {rows_before}")
    print(f"Rows after cleaning: {rows_after}")
    print(f"Rows removed: {rows_before - rows_after}")

    return data


if __name__ == "__main__":
    from src.ingest import load_raw_data

    raw_data = load_raw_data()
    cleaned_data = clean_data(raw_data)
    print()
    print(cleaned_data.head())