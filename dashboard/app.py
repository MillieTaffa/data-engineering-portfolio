"""
dashboard/app.py

Responsibility: display the processed SocialPulse data in an interactive
Streamlit dashboard.

This reads from the SQLite database (via src/analytics.py), so the
pipeline (python -m src.pipeline) must be run at least once before
the dashboard will show any data.

Run with (from the project root):
    streamlit run dashboard/app.py
"""

import sys
from pathlib import Path

# This file lives inside dashboard/, one level below the project root.
# Add the project root to Python's import path so "from src import ..."
# works no matter which folder Streamlit is launched from.
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import plotly.express as px

from src import analytics
from src import config

st.set_page_config(page_title="SocialPulse", layout="wide")

st.title("SocialPulse")
st.caption("Social Media Engagement Intelligence Dashboard")

# If the pipeline has not been run yet, the database file will not exist.
# Show a friendly message instead of crashing.
if not config.DATABASE_PATH.exists():
    st.warning(
        "No database found yet. Run the pipeline first from the project "
        "root with:  python -m src.pipeline"
    )
    st.stop()

# ---------- KPI CARDS ----------
summary = analytics.get_summary_metrics().iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Posts", f"{int(summary['total_posts']):,}")
col2.metric("Total Views", f"{int(summary['total_views']):,}")
col3.metric("Total Interactions", f"{int(summary['total_interactions']):,}")
col4.metric("Avg Engagement Rate", f"{summary['avg_engagement_rate']}%")

col5, col6, col7 = st.columns(3)
col5.metric("Total Likes", f"{int(summary['total_likes']):,}")
col6.metric("Total Comments", f"{int(summary['total_comments']):,}")
col7.metric("Total Shares", f"{int(summary['total_shares']):,}")

st.divider()

# ---------- FILTER (sidebar) ----------
st.sidebar.header("Filters")
platform_data = analytics.get_platform_performance()
platform_options = ["All"] + sorted(platform_data["Platform"].unique().tolist())
selected_platform = st.sidebar.selectbox("Platform (for Content Type chart below)", platform_options)

# ---------- ENGAGEMENT OVER TIME ----------
st.subheader("Engagement Over Time")
time_data = analytics.get_engagement_over_time()
fig_time = px.line(
    time_data, x="post_date", y="avg_engagement_rate",
    title="Average Engagement Rate by Day",
    labels={"post_date": "Date", "avg_engagement_rate": "Avg Engagement Rate (%)"},
)
st.plotly_chart(fig_time, use_container_width=True)

# ---------- PLATFORM PERFORMANCE ----------
st.subheader("Platform Performance")
fig_platform = px.bar(
    platform_data, x="Platform", y="avg_engagement_rate",
    title="Average Engagement Rate by Platform",
    text="post_count",
    labels={"avg_engagement_rate": "Avg Engagement Rate (%)"},
)
st.plotly_chart(fig_platform, use_container_width=True)

# ---------- CONTENT TYPE PERFORMANCE ----------
st.subheader("Content Type Performance")
content_data = analytics.get_content_type_performance()
if selected_platform != "All":
    content_data = content_data[content_data["Platform"] == selected_platform]
fig_content = px.bar(
    content_data, x="Content_Type", y="avg_engagement_rate", color="Platform",
    title="Average Engagement Rate by Content Type",
    labels={"avg_engagement_rate": "Avg Engagement Rate (%)"},
)
st.plotly_chart(fig_content, use_container_width=True)

# ---------- CATEGORY PERFORMANCE ----------
st.subheader("Category Performance")
topic_data = analytics.get_topic_performance()
fig_topic = px.bar(
    topic_data, x="Category", y="avg_engagement_rate",
    title="Average Engagement Rate by Category",
    labels={"avg_engagement_rate": "Avg Engagement Rate (%)"},
)
st.plotly_chart(fig_topic, use_container_width=True)

# ---------- TOP POSTS TABLE ----------
st.subheader("Top 10 Posts by Total Interactions")
top_posts = analytics.get_top_posts(limit=10)
st.dataframe(top_posts, use_container_width=True)

st.divider()
st.caption(
    "Data source: social_media_engagement_dataset.csv (a synthetic dataset - "
    "see docs/DATA_DICTIONARY.md for details and limitations). "
    "computed_engagement_rate is calculated in this project as "
    "(Likes + Comments + Shares + Saves) / Views x 100, and is not the same "
    "as the Engagement_Rate column already present in the raw data."
)