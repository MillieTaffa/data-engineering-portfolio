"""
analytics.py

Responsibility: run reusable analytical queries against the SQLite database.

Every function here returns a pandas DataFrame, so the dashboard (or
anyone else, like a Jupyter notebook) can call these functions instead
of writing SQL directly. This keeps all of the project's SQL logic in
one place, separate from how it is displayed.

The same queries also live in sql/analysis.sql, written as plain SQL,
so the SQL itself can be reviewed on its own without reading Python.
"""

from src.database import run_query


def get_summary_metrics():
    """Returns a one-row DataFrame of overall totals, used for the dashboard KPI cards."""
    query = """
        SELECT
            COUNT(*) AS total_posts,
            SUM(Views) AS total_views,
            SUM(Likes) AS total_likes,
            SUM(Comments) AS total_comments,
            SUM(Shares) AS total_shares,
            SUM(total_interactions) AS total_interactions,
            ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate
        FROM posts;
    """
    return run_query(query)


def get_platform_performance():
    """Returns post count and average engagement rate for each platform."""
    query = """
        SELECT
            Platform,
            COUNT(*) AS post_count,
            ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate,
            SUM(total_interactions) AS total_interactions
        FROM posts
        GROUP BY Platform
        ORDER BY avg_engagement_rate DESC;
    """
    return run_query(query)


def get_content_type_performance():
    """Returns post count and average engagement rate for each content type, by platform."""
    query = """
        SELECT
            Content_Type,
            Platform,
            COUNT(*) AS post_count,
            ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate,
            SUM(total_interactions) AS total_interactions
        FROM posts
        GROUP BY Content_Type, Platform
        ORDER BY avg_engagement_rate DESC;
    """
    return run_query(query)


def get_topic_performance():
    """Returns post count and average engagement rate for each content category."""
    query = """
        SELECT
            Category,
            COUNT(*) AS post_count,
            ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate,
            SUM(total_interactions) AS total_interactions
        FROM posts
        GROUP BY Category
        ORDER BY avg_engagement_rate DESC;
    """
    return run_query(query)


def get_engagement_over_time():
    """Returns post count and average engagement rate per day, for the trend chart."""
    query = """
        SELECT
            post_date,
            COUNT(*) AS post_count,
            ROUND(AVG(computed_engagement_rate), 2) AS avg_engagement_rate
        FROM posts
        GROUP BY post_date
        ORDER BY post_date;
    """
    return run_query(query)


def get_top_posts(limit=10):
    """Returns the top-performing posts, ranked by total_interactions."""
    query = f"""
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
        LIMIT {int(limit)};
    """
    return run_query(query)


if __name__ == "__main__":
    print("Summary metrics:")
    print(get_summary_metrics())
    print()
    print("Platform performance:")
    print(get_platform_performance())