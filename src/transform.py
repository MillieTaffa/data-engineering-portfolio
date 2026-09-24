"""
transform.py

Responsibility: turn cleaned data into analytics-ready data by calculating
new metrics that are not explicitly present in the raw dataset.

New columns created here
-------------------------
- total_interactions        = Likes + Comments + Shares + Saves
- computed_engagement_rate  = total_interactions / Views x 100
- comment_rate               = Comments / Views x 100
- share_rate                 = Shares / Views x 100
- post_date                  = the calendar date of the post (no time)

A note on Engagement_Rate
---------------------------
The raw dataset already contains an "Engagement_Rate" column. Before writing
this file, that column was compared against a formula built from
Likes/Comments/Shares/Saves/Views, and the two did not line up (the
correlation between them was close to zero). This means we cannot be sure
exactly how the original Engagement_Rate column was calculated.

Rather than guessing or pretending they are the same thing, this project:
  1. keeps the original Engagement_Rate column exactly as provided, and
  2. adds its own "computed_engagement_rate" column using the clearly
     documented formula above.

The two are never merged or confused with each other. See
docs/DATA_DICTIONARY.md for more detail.
"""


def calculate_total_interactions(data):
    """Adds total_interactions: Likes + Comments + Shares + Saves."""
    data = data.copy()
    data["total_interactions"] = data["Likes"] + data["Comments"] + data["Shares"] + data["Saves"]
    return data


def calculate_computed_engagement_rate(data):
    """
    Adds computed_engagement_rate: total_interactions divided by Views,
    shown as a percentage. "total_interactions" must already exist on the
    DataFrame (run calculate_total_interactions first).
    """
    data = data.copy()
    # A rate cannot be calculated when a post has no views.
    safe_views = data["Views"].replace(0, float("nan"))
    data["computed_engagement_rate"] = ((data["total_interactions"] / safe_views) * 100).round(2)
    return data


def calculate_comment_rate(data):
    """Adds comment_rate: Comments divided by Views, shown as a percentage."""
    data = data.copy()
    safe_views = data["Views"].replace(0, float("nan"))
    data["comment_rate"] = ((data["Comments"] / safe_views) * 100).round(2)
    return data


def calculate_share_rate(data):
    """Adds share_rate: Shares divided by Views, shown as a percentage."""
    data = data.copy()
    safe_views = data["Views"].replace(0, float("nan"))
    data["share_rate"] = ((data["Shares"] / safe_views) * 100).round(2)
    return data


def add_post_date(data):
    """Adds post_date: just the calendar date part of Timestamp, as text."""
    data = data.copy()
    data["post_date"] = data["Timestamp"].dt.date.astype(str)
    return data


def transform_data(data):
    """Runs every transformation step in order and returns the transformed DataFrame."""
    print("Transforming data...")

    data = calculate_total_interactions(data)
    data = calculate_computed_engagement_rate(data)
    data = calculate_comment_rate(data)
    data = calculate_share_rate(data)
    data = add_post_date(data)

    print("New columns added: total_interactions, computed_engagement_rate, comment_rate, share_rate, post_date")

    return data


if __name__ == "__main__":
    from src.ingest import load_raw_data
    from src.clean import clean_data

    raw_data = load_raw_data()
    cleaned_data = clean_data(raw_data)
    transformed_data = transform_data(cleaned_data)

    print()
    print(transformed_data[
        ["Post_ID", "total_interactions", "computed_engagement_rate", "comment_rate", "share_rate", "post_date"]
    ].head())
