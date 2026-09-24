# SocialPulse User Manual

## What is SocialPulse?

SocialPulse is a data engineering project for social-media engagement data. It reads
a CSV file of posts, checks and cleans the data, creates useful engagement metrics,
and saves the results for analysis.

It helps answer simple questions such as:

- Which platform has the highest engagement?
- Which content types perform best?
- How does engagement change over time?
- Which posts received the most interactions?

The project uses Python, pandas, SQLite, Streamlit, and Plotly. The included data is
synthetic, so it is safe to use for learning and portfolio work.

## What the project does

When you run the pipeline, SocialPulse:

1. Reads the raw CSV file from `data/raw/`.
2. Checks for missing values, duplicate posts, invalid dates, negative metrics, and unexpected categories.
3. Cleans the data by removing unusable rows and standardising text values.
4. Creates extra metrics, including total interactions and engagement rates.
5. Saves the processed data as a CSV file and in a SQLite database.
6. Uses the database to power an interactive Streamlit dashboard.

In short: raw data goes in, cleaner data and useful insights come out.

## Before you start

You need Python 3.10 or newer, `pip`, and a terminal such as Terminal, PowerShell,
or the VS Code terminal.

## Step 1: Open the project folder

Open a terminal and move into the SocialPulse project folder:

```bash
cd path/to/socialpulse
```

If you use VS Code, open the project folder and choose **Terminal → New Terminal**.

## Step 2: Create a virtual environment

A virtual environment keeps this project's packages separate from other Python projects.

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

When it is active, your terminal normally shows `(.venv)` at the beginning of the command line.

## Step 3: Install the required packages

Run:

```bash
pip install -r requirements.txt
```

This installs pandas for data processing, Streamlit and Plotly for the dashboard, and pytest for automated tests.

## Step 4: Run the data pipeline

From the project root, run:

```bash
python -m src.pipeline
```

The terminal will show each stage of the pipeline. A successful run ends with:

```text
PIPELINE COMPLETE
```

The pipeline creates or updates these files:

```text
data/processed/social_media_clean.csv
database/socialpulse.db
```

The processed CSV can be opened in Excel, Google Sheets, or another data tool. The SQLite database is used by the dashboard.

## Step 5: Run the dashboard

After the pipeline completes, start the dashboard:

```bash
streamlit run dashboard/app.py
```

Streamlit will print a local address, usually `http://localhost:8501`. Open it in your browser if it does not open automatically.

The dashboard includes summary cards, engagement-over-time charts, platform, content-type, and category charts, a platform filter, and a table of the top 10 posts by total interactions.

To stop the dashboard, return to the terminal and press `Ctrl + C`.

## Step 6: Run the tests

Run the automated tests whenever you change pipeline code:

```bash
pytest -q
```

A healthy project should finish with a result similar to `20 passed`.

## Main folders

| Folder | Purpose |
|---|---|
| `data/raw/` | Original input CSV file. |
| `data/processed/` | Cleaned and transformed CSV output. |
| `src/` | Pipeline Python code. |
| `sql/` | Database schema and analysis queries. |
| `database/` | Generated SQLite database. |
| `dashboard/` | Streamlit dashboard application. |
| `tests/` | Automated tests. |
| `docs/` | Project documentation. |

## Common problems and simple fixes

### `ModuleNotFoundError` or `No module named ...`

Your virtual environment may not be active, or packages may not be installed. Activate `.venv` and run:

```bash
pip install -r requirements.txt
```

### The dashboard says that no database was found

Run the pipeline first:

```bash
python -m src.pipeline
```

Then start the dashboard again.

### `python` is not recognised

Try `python3` instead:

```bash
python3 -m src.pipeline
```

### The dashboard does not update after a code change

Stop it with `Ctrl + C`, run the pipeline again, and restart Streamlit.

## Useful commands

```bash
# Run the complete pipeline
python -m src.pipeline

# Start the dashboard
streamlit run dashboard/app.py

# Run tests
pytest -q

# Leave the virtual environment
deactivate
```

## More technical detail

See [Architecture](architecture.md) for the pipeline flow and [Data Dictionary](data_dictionary.md) for descriptions of every input and derived field.
