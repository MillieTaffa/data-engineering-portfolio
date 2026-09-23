"""
tests/test_transform.py

Tests for the functions in src/transform.py.
"""

import pandas as pd

from src.transform import (
    calculate_total_interactions,
    calculate_computed_engagement_rate,
    calculate_comment_rate,
    calculate_share_rate,
)


def make_transform_row():
    """Helper: a simple row with easy numbers to check the maths by hand."""
    return {
        "Likes": 100,
        "Comments": 20,
        "Shares": 10,
        "Saves": 5,
        "Views": 1000,
    }


def test_total_interactions_is_correct():
    data = pd.DataFrame([make_transform_row()])

    result = calculate_total_interactions(data)

    # 100 + 20 + 10 + 5 = 135
    assert result.loc[0, "total_interactions"] == 135


def test_computed_engagement_rate_is_correct():
    data = pd.DataFrame([make_transform_row()])
    data = calculate_total_interactions(data)

    result = calculate_computed_engagement_rate(data)

    # 135 / 1000 * 100 = 13.5
    assert result.loc[0, "computed_engagement_rate"] == 13.5


def test_comment_rate_is_correct():
    data = pd.DataFrame([make_transform_row()])

    result = calculate_comment_rate(data)

    # 20 / 1000 * 100 = 2.0
    assert result.loc[0, "comment_rate"] == 2.0


def test_share_rate_is_correct():
    data = pd.DataFrame([make_transform_row()])

    result = calculate_share_rate(data)

    # 10 / 1000 * 100 = 1.0
    assert result.loc[0, "share_rate"] == 1.0


def test_computed_engagement_rate_handles_zero_views():
    row = make_transform_row()
    row["Views"] = 0
    data = pd.DataFrame([row])
    data = calculate_total_interactions(data)

    result = calculate_computed_engagement_rate(data)

    # Should not raise a divide-by-zero error, and should be a real number.
    assert result.loc[0, "computed_engagement_rate"] >= 0