"""
tests/test_clean.py

Tests for the functions in src/clean.py.
"""

import pandas as pd

from src.clean import (
    remove_duplicates,
    handle_missing_values,
    fix_invalid_dates,
    remove_negative_values,
    standardize_text_columns,
    recalculate_time_columns,
)
from tests.test_validate import make_sample_row


def test_remove_duplicates_drops_repeated_post_id():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0001")])

    cleaned = remove_duplicates(data)

    assert len(cleaned) == 1


def test_handle_missing_values_drops_incomplete_rows():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0002")])
    data.loc[0, "Category"] = None

    cleaned = handle_missing_values(data)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["Post_ID"] == "POST_0002"


def test_fix_invalid_dates_drops_bad_timestamps():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0002")])
    data.loc[0, "Timestamp"] = "not-a-real-date"

    cleaned = fix_invalid_dates(data)

    assert len(cleaned) == 1
    assert pd.api.types.is_datetime64_any_dtype(cleaned["Timestamp"])


def test_remove_negative_values_drops_bad_rows():
    data = pd.DataFrame([make_sample_row("POST_0001", likes=-50), make_sample_row("POST_0002")])

    cleaned = remove_negative_values(data)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["Post_ID"] == "POST_0002"


def test_standardize_text_columns_fixes_casing():
    data = pd.DataFrame([make_sample_row("POST_0001")])
    data.loc[0, "Platform"] = "  instagram  "

    cleaned = standardize_text_columns(data)

    assert cleaned.loc[0, "Platform"] == "Instagram"


def test_standardize_text_columns_preserves_internal_capitals():
    # A plain .title() would turn "tiktok" into "Tiktok" - this checks the
    # lookup-based fix in standardize_text_columns avoids that mistake.
    data = pd.DataFrame([make_sample_row("POST_0001")])
    data.loc[0, "Platform"] = "tiktok"

    cleaned = standardize_text_columns(data)

    assert cleaned.loc[0, "Platform"] == "TikTok"


def test_recalculate_time_columns_matches_timestamp():
    data = pd.DataFrame([make_sample_row("POST_0001")])
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    data.loc[0, "Hour_of_Day"] = 99  # deliberately wrong value

    cleaned = recalculate_time_columns(data)

    assert cleaned.loc[0, "Hour_of_Day"] == 10
    assert cleaned.loc[0, "Day_of_Week"] == "Monday"