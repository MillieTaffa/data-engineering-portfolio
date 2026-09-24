-- analysis.sql
-- Analytical queries for the SocialPulse "posts" table.
-- These are the same queries used by src/analytics.py, written here as plain SQL so they can be run directly (e.g. with the sqlite3 CLI or DB Browser for SQLite) without going through Python at all.



-- Query 1: Top 10 performing posts by total interactions
SELECT
    Post_ID,
    Platform,
    Content_Type,
    Category,
    Views,
    total_interactions,
    computed_engagement_rate
FROM posts
ORDER BY total_interactions DESC
LIMIT 10;


-- Query 2: Average engagement rate by platform
SELECT
    Platform,
    COUNT(*) AS post_count,
    ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate
FROM posts
GROUP BY Platform
ORDER BY avg_engagement_rate DESC;


-- Query 3: Total interactions by content type
SELECT
    Content_Type,
    Platform,
    SUM(total_interactions) AS interactions
FROM posts
GROUP BY Content_Type, Platform
ORDER BY interactions DESC;


-- Query 4: Engagement rate over time (by day)
SELECT
    post_date,
    COUNT(*) AS post_count,
    ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate
FROM posts
GROUP BY post_date
ORDER BY post_date;


-- Query 5: Performance by content category
SELECT
    Category,
    COUNT(*) AS post_count,
    ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate
FROM posts
GROUP BY Category
ORDER BY avg_engagement_rate DESC;