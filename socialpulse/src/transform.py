import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["total_interactions"] = df["likes"] + df["comments"] + df["shares"]
    
    # Calculate rates, handling zero-view division safely
    df["engagement_rate"] = df.apply(
        lambda r: (r["total_interactions"] / r["views"] * 100) if r["views"] > 0 else 0.0,
        axis=1
    ).round(2)

    df["comment_rate"] = df.apply(
        lambda r: (r["comments"] / r["views"] * 100) if r["views"] > 0 else 0.0,
        axis=1
    ).round(2)

    df["share_rate"] = df.apply(
        lambda r: (r["shares"] / r["views"] * 100) if r["views"] > 0 else 0.0,
        axis=1
    ).round(2)

    return df