-- schema.sql

-- This defines the "posts" table used to store the cleaned and transformed social media data. This table is created by the scr/database.py file before the data is inserted.

-- Post_ID is the primary key because it identifies each post, and the cleaning step (src/clean.py) already guarantees there are no duplicate Post_ID values by the time the data gets to the table.

CREATE TABLE IF NOT EXISTS posts (
    Post_ID TEXT PRIMARY KEY,
    Timestamp TEXT NOT NULL,
    post_date TEXT NOT NULL,
    Platform TEXT NOT NULL,
    Content_Type TEXT NOT NULL,
    Category TEXT NOT NULL,
    Likes INTEGER NOT NULL,
    Comments INTEGER NOT NULL,
    Shares INTEGER NOT NULL,
    Views INTEGER NOT NULL,
    Saves INTEGER NOT NULL,
    Follower_Count INTEGER NOT NULL,
    Engagement_Rate REAL,
    Hour_of_Day INTEGER,
    Day_of_Week TEXT,
    Hashtag_Count INTEGER,
    Content_Length INTEGER,
    Sentiment TEXT,
    Influencer_Tier TEXT,
    Has_Media INTEGER,
    Is_Verified INTEGER,
    total_interactions INTEGER,
    computed_engagement_rate REAL,
    comment_rate REAL,
    share_rate REAL
);