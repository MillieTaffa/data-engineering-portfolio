SocialPulse

SocialPulse is an end-to-end data engineering pipeline that processes raw, messy social media engagement data. It ingests, validates, cleans, and transforms raw CSV records, loads the structured output into a SQLite relational database, and presents actionable insights through an interactive Streamlit dashboard.

🏗 Pipeline Architecture

Raw CSV Data ➔ Ingestion ➔ Validation ➔ Cleaning ➔ Transformation ➔ SQLite DB ➔ Analytics ➔ Streamlit Dashboard


Ingestion (src/ingest.py): Loads raw CSV data into a pandas DataFrame.

Validation (src/validate.py): Identifies schema mismatches, duplicate IDs, missing values, and numeric anomalies.

Cleaning (src/clean.py): Fixes invalid records, standardizes dates (YYYY-MM-DD), and normalizes platform and content categories.

Transformation (src/transform.py): Calculates derived engagement metrics (total_interactions, engagement_rate, etc.).

Database Storage (src/database.py): Loads clean, structured data into a SQLite database using sql/schema.sql.

Analytics (src/analytics.py): Executes analytical queries from sql/analysis.sql against the database.

Dashboard (dashboard/app.py): Renders interactive charts and KPI metrics using Streamlit and Plotly.

📁 Folder Structure

socialpulse/
├── data/
│   ├── raw/            # Original messy dataset
│   └── processed/      # Cleaned data files
├── database/           # Generated SQLite database (socialpulse.db)
├── src/                # Pipeline logic modules
├── dashboard/          # Streamlit visualization app
├── sql/                # DDL schema and analytical queries
├── tests/              # Automated unit tests (pytest)
├── docs/               # Architecture and data dictionary documentation
├── requirements.txt    # Project dependencies
└── README.md


🚀 Getting Started

1. Prerequisites & Installation

Clone the repository and set up a virtual environment:

# Clone repository
git clone https://github.com/your-username/socialpulse.git
cd socialpulse

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


⚡ Running the Project

Execute Data Pipeline

Runs the end-to-end process: ingestion, validation, cleaning, transformation, and SQLite database storage.

python -m src.pipeline


Launch Interactive Dashboard

Opens the Streamlit dashboard in your web browser.

streamlit run dashboard/app.py


Run Unit Tests

Verifies validation, cleaning, and transformation modules using pytest.

pytest


🛠 Tech Stack

Language: Python

Data Processing: pandas

Database: SQLite & SQL

Visualization: Streamlit, Plotly

Testing: pytest

Version Control: Git, GitHub