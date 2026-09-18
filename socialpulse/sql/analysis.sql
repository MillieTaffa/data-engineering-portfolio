-- Average engagement rate by platform
SELECT
    platform,
    COUNT(post_id) AS total_posts,
    AVG(engagement_rate) AS avg_engagement_rate
FROM posts
GROUP BY platform
ORDER BY avg_engagement_rate DESC;


-- Top 5 posts by total interactions
SELECT
    post_id,
    platform,
    content_type,
    total_interactions,
    engagement_rate
FROM posts
ORDER BY total_interactions DESC
LIMIT 5;


-- Average engagement rate by content type
SELECT
    content_type,
    COUNT(post_id) AS total_posts,
    AVG(engagement_rate) AS avg_engagement_rate
FROM posts
GROUP BY content_type
ORDER BY avg_engagement_rate DESC;


-- Most viewed posts
SELECT
    post_id,
    platform,
    content_type,
    views
FROM posts
ORDER BY views DESC
LIMIT 5;


-- Total interactions by platform
SELECT
    platform,
    SUM(likes) AS total_likes,
    SUM(comments) AS total_comments,
    SUM(shares) AS total_shares,
    SUM(total_interactions) AS total_interactions
FROM posts
GROUP BY platform
ORDER BY total_interactions DESC;