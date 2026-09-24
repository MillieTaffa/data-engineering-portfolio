# SocialPulse Architecture

SocialPulse is a small batch data pipeline for exploring social-media engagement data.
It takes one CSV input, validates and prepares it with Python and pandas, then makes
the results available as both a CSV file and a SQLite database for the dashboard.

```text
data/raw/social_media_engagement_dataset.csv
                    |
                    v
              ingest.py
                    |
                    v
             validate.py
                    |
                    v
               clean.py
                    |
                    v
             transform.py
              /           \
             v             v
         load.py       database.py
             |             |
             v             v
 processed CSV       SQLite posts table
                              |
                              v
                    analytics.py -> dashboard/app.py
```

## Pipeline stages

1. **Ingest** reads the raw CSV into a pandas DataFrame.
2. **Validate** reports missing columns and values, duplicate posts, invalid dates,
   negative metrics, invalid categories, and timestamp inconsistencies.
3. **Clean** drops unusable rows, standardizes text categories, parses timestamps,
   and recalculates the day and hour columns from each timestamp.
4. **Transform** adds total interactions, engagement, comment, and share rates,
   plus a `post_date` field for daily analysis.
5. **Load** writes `data/processed/social_media_clean.csv` and replaces the data in
   the SQLite `posts` table at `database/socialpulse.db`.
6. **Analyse and display** uses SQL queries in `src/analytics.py` and renders them
   in the Streamlit dashboard.

## Running the project

From the project root:

```bash
pip install -r requirements.txt
python -m src.pipeline
streamlit run dashboard/app.py
```

Run automated checks with:

```bash
pytest -q
```
