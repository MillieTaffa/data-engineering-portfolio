"""
        config.py

        This file stores the file paths and the dataset settings that are used across the entire SocialPulse project. It keeps everything in one  place means we don't have to repeat file paths or column names in every file
    """

from pathlib import Path

# BASE_DIR points to the project's root folder which is a level above src/
BASE_DIR = Path(__file__).resolve().parent.parent

# -------- DATA PATHS --------

# Raw data: the original, untouched CSV file

RAW_DATA_PATH  = BASE_DIR/ "data" /"raw" / "social_media_engagement_dataset.csv"

# Processed data: this is the path to the cleaned and transformed CSV we generate
PROCESSED_DATA_DIR = BASE_DIR/ "data"/ "processed"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR/ "social_media_clean.csv"

# -------- DATABASE PATHS --------

DATABASE_DIR = BASE_DIR/"database"
DATABASE_PATH = DATABASE_DIR / "socialpulse.db"

# -------- SQL PATHS --------

SQL_DIR = BASE_DIR/"sql"
SCHEMA_SQL_PATH = SQL_DIR / "schema.sql"

# -------- DATASET EXCEPTATIONS --------
# These lists describe what a "good" row of this dataset should look like.
# They were built by inspecting the real CSV file before writing any code.

# Every column that should exist in the raw CSV file
REQUIRED_COLUMNS = [
    "Post_ID",
    "Timestamp",
    "Platform",
    "Content_Type",
    "Category",
    "Likes",
    "Comments",
    "Shares",
    "Views",
    "Saves",
    "Follower_Count",
    "Engagement_Rate",
    "Hour_of_Day",
    "Day_of_Week",
    "Hashtag_Count",
    "Content_Length",
    "Sentiment",
    "Influencer_Tier",
    "Has_Media",
    "Is_Verified",
]

# Numeric columns that should never contain a negative number

NUMERIC_COLUMNS = [
    "Likes",
    "Comments",
    "Shares",
    "Views",
    "Saves",
    "Follower_Count",
    "Engagement_Rate",
    "Hashtag_Count",
    "Content_Length",
]

# The catergorical values we expect to see, based on inspecting the dataset.
# Validation flags anything outside these lists as "unexpected" so we notice
# new or misspelled categories instead of silently ignoring them.

EXPECTED_PLATFORMS = [
    "Instagram", "Twitter", "Facebook", "TikTok", "LinkedIn", "YouTube"
]
EXPECTED_DAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday",
]
EXPECTED_SENTIMENTS = ["Positive", "Neutral", "Negative"]
EXPECTED_TIERS = ["Nano", "Micro", "Mid-tier", "Macro"]