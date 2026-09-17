CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER PRIMARY KEY,
    platform TEXT NOT NULL,
    post_date DATE NOT NULL,
    content_type TEXT NOT NULL,
    topic TEXT,
    views INTEGER,
    likes INTEGER,
    comments INTEGER,
    shares INTEGER,
    total_interactions INTEGER,
    engagement_rate REAL,
    comment_rate REAL,
    share_rate REAL
);