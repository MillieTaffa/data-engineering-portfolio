import pandas as pd

REQUIRED_COLUMNS = [
    "post_id",
    "platform",
    "post_date",
    "content_type",
    "topic",
    "views",
    "likes",
    "comments",
    "shares"
]


def validate_data(df):
    issues = {}

    issues["missing_columns"] = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    issues["duplicate_ids"] = df["post_id"].duplicated().sum()

    issues["missing_values"] = df.isnull().sum().to_dict()

    metrics = ["views", "likes", "comments", "shares"]

    issues["negative_metrics"] = (
        df[metrics] < 0
    ).sum().to_dict()

    dates = pd.to_datetime(df["post_date"], errors="coerce")

    issues["invalid_dates"] = dates.isnull().sum()

    return issues