# SocialPulse

### Social-media engagement data pipeline and dashboard

An end-to-end Python and SQL project for validating, cleaning, transforming, and
analysing social-media engagement data.

![License](https://img.shields.io/badge/License-MIT-gold?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-SocialPulse-purple?style=for-the-badge)

## About

SocialPulse is a batch ETL project built around the synthetic dataset in
`data/raw/social_media_engagement_dataset.csv`. It uses pandas to prepare the data,
SQLite to store analytics-ready records, and Streamlit with Plotly to present the
results.

The pipeline runs these stages:

1. **Ingest** the raw CSV into a pandas DataFrame.
2. **Validate** required columns, missing values, duplicates, dates, numeric values, and categories.
3. **Clean** unusable rows, standardise text, and recalculate date-related fields.
4. **Transform** the data with total interactions, computed engagement rate, comment rate, share rate, and post date.
5. **Load** the results to `data/processed/social_media_clean.csv` and `database/socialpulse.db`.
6. **Analyse** the SQLite data in the interactive dashboard.

The raw `Engagement_Rate` field is retained as supplied. The project's
`computed_engagement_rate` is calculated separately as:

```text
(Likes + Comments + Shares + Saves) / Views * 100
```

This keeps the source metric separate from the project-defined metric.

## Dashboard

The dashboard reads from the generated SQLite database and includes:

- KPI totals for posts, views, interactions, likes, comments, shares, and average engagement rate.
- Daily engagement-rate trends.
- Platform, content-type, and category performance charts.
- A platform filter for the content-type chart.
- The top 10 posts ranked by total interactions.

## Run the project

Use Python 3.10 or newer. From the project root:

```bash
# Optional: create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline from the project root
python -m src.pipeline

# Start the dashboard
streamlit run dashboard/app.py

# Run the test suite
pytest -q
```

The pipeline creates or updates these generated outputs:

- `data/processed/social_media_clean.csv`
- `database/socialpulse.db`

For Windows setup, troubleshooting, and detailed instructions, see the
[SocialPulse User Manual](docs/user_manual.md).

## Tech stack

- Python and pandas for ingestion, validation, cleaning, and transformation
- SQLite for relational storage
- SQL for reusable schema and analysis queries
- Streamlit and Plotly for the dashboard
- pytest for automated tests

## Repository structure

```text
socialpulse/
├── assets/                              Project screenshots and image assets
├── courses/                             Course notes
├── dashboard/app.py                    Streamlit dashboard
├── data/raw/                           Original input CSV
├── data/processed/                     Generated cleaned CSV output
├── database/                            Generated SQLite database
├── docs/                               Project documentation
├── sql/                                Schema and analysis queries
├── src/                                Pipeline source code
├── tests/                              Automated tests
├── requirements.txt                    Python dependencies
└── README.md
```

## Documentation

- [User Manual](docs/user_manual.md) - setup, running, and troubleshooting.
- [Architecture](docs/architecture.md) - pipeline flow and component overview.
- [Data Dictionary](docs/data_dictionary.md) - raw and derived field definitions.
- [Project Notes](docs/social_pulse_info.md) - additional project information.

## License

This project is available under the [MIT License](LICENSE).
