"""
tests/test_validate.py

Tests for the functions in src/validate.py.

We build small, custom DataFrames here so we can control exactly which
problems are present, instead of relying on the real dataset (which may
or may not contain any problems on a given day).
"""

import pandas as pd

from src.validate import (
    check_missing_columns,
    check_missing_values,
    check_duplicate_ids,
    check_duplicate_rows,
    check_invalid_dates,
    check_negative_numbers,
    check_hour_of_day_range,
)


def make_sample_row(post_id="POST_0001", likes=100, views=1000, hour=10):
    """Helper: builds one valid row as a dictionary, matching the raw dataset's columns."""
    return {
        "Post_ID": post_id,
        "Timestamp": "2024-01-01 10:00:00",
        "Platform": "Instagram",
        "Content_Type": "Photo",
        "Category": "Food",
        "Likes": likes,
        "Comments": 10,
        "Shares": 5,
        "Views": views,
        "Saves": 2,
        "Follower_Count": 5000,
        "Engagement_Rate": 1.5,
        "Hour_of_Day": hour,
        "Day_of_Week": "Monday",
        "Hashtag_Count": 3,
        "Content_Length": 100,
        "Sentiment": "Positive",
        "Influencer_Tier": "Micro",
        "Has_Media": True,
        "Is_Verified": False,
    }


def test_valid_dataset_has_no_problems():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0002")])

    assert check_missing_columns(data) == []
    assert check_missing_values(data).sum() == 0
    assert check_duplicate_ids(data) == 0
    assert check_duplicate_rows(data) == 0
    assert check_invalid_dates(data) == 0
    assert sum(check_negative_numbers(data).values()) == 0
    assert check_hour_of_day_range(data) == 0


def test_missing_column_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001")])
    data = data.drop(columns=["Platform"])

    missing = check_missing_columns(data)

    assert "Platform" in missing


def test_missing_value_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0002")])
    data.loc[0, "Category"] = None

    missing_values = check_missing_values(data)

    assert missing_values["Category"] == 1


def test_duplicate_post_id_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001"), make_sample_row("POST_0001")])

    assert check_duplicate_ids(data) == 1


def test_duplicate_row_is_detected():
    row = make_sample_row("POST_0001")
    data = pd.DataFrame([row, row])

    assert check_duplicate_rows(data) == 1


def test_negative_likes_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001", likes=-50)])

    negative_counts = check_negative_numbers(data)

    assert negative_counts["Likes"] == 1


def test_invalid_date_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001")])
    data.loc[0, "Timestamp"] = "not-a-real-date"

    assert check_invalid_dates(data) == 1


def test_hour_out_of_range_is_detected():
    data = pd.DataFrame([make_sample_row("POST_0001", hour=27)])

    assert check_hour_of_day_range(data) == 1