import pandas as pd


def clean_data(df):
    df = df.copy()

    df = df.drop_duplicates(subset=["post_id"], keep="first")

    df["platform"] = df["platform"].str.strip().str.capitalize()
    df["content_type"] = df["content_type"].str.strip().str.capitalize()

    df["post_date"] = pd.to_datetime(df["post_date"], errors="coerce")
    df = df.dropna(subset=["post_date"])

    numeric_columns = ["views", "likes", "comments", "shares"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(0)
        df[column] = df[column].clip(lower=0)

    return df