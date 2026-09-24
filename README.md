<div align="center">

# 📊 Data Engineering Portfolio

### *My journey to becoming a Data Engineer.*

<p>
Building data pipelines • Learning SQL • Exploring data analytics • Solving real-world problems
</p>

![License](https://img.shields.io/badge/License-MIT-gold?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-SocialPulse-purple?style=for-the-badge)

</div>

---

## 👋 About

Welcome to my **Data Engineering Portfolio**.

I am a Software Engineering student at WeThinkCode_ building practical skills in
data engineering, Python, SQL, data cleaning, and analytics.

This repository currently contains **SocialPulse**, an end-to-end data engineering
project. It processes social-media engagement data, prepares it for analysis, stores
it in SQLite, and displays insights in an interactive dashboard.

My goal is to build reliable, well-documented data projects while learning by doing.

---

## 🎯 Goals

- ✅ Learn data engineering fundamentals
- ✅ Develop Python and SQL skills
- ✅ Build and test an end-to-end ETL pipeline
- 🔄 Work with APIs and real-world datasets
- 🔄 Practice data modelling and warehousing
- 🔄 Explore cloud, Airflow, and Spark tools
- 🔄 Build professional portfolio projects

---

## 🚀 Featured Project: SocialPulse

SocialPulse is a beginner-friendly project for analysing social-media engagement data.
It reads a CSV file of posts, validates and cleans the data, creates engagement metrics,
saves the output as a processed CSV and SQLite database, and presents the results in a
Streamlit dashboard.

### What SocialPulse does

1. Reads raw social-media post data from a CSV file.
2. Validates missing values, duplicate posts, invalid dates, negative values, and categories.
3. Cleans and standardises the data.
4. Calculates total interactions, engagement rate, comment rate, and share rate.
5. Saves the results to a processed CSV file and a SQLite database.
6. Displays performance charts and top posts in a Streamlit dashboard.

### Run SocialPulse

```bash
# Install project packages
pip install -r requirements.txt

# Process the data and create the SQLite database
python -m src.pipeline

# Open the dashboard
streamlit run dashboard/app.py

# Run automated tests
pytest -q
```

For complete setup instructions, see the [SocialPulse User Manual](docs/user_manual.md).

---

## 🛠️ Tech Stack

### Languages and databases

- Python
- SQL
- SQLite

### Data engineering

- ETL pipelines
- Data ingestion
- Data validation and cleaning
- Data transformation
- Derived metrics
- Relational database loading

### Tools and libraries

- pandas
- Streamlit
- Plotly
- pytest
- Git and GitHub
- VS Code

---

## 📚 Courses and learning

### IBM

- IBM Data Engineering Basics for Everyone

### Ongoing learning

This portfolio grows as I complete coursework, practise SQL and Python, and build
new data engineering projects.

---

## 📂 Repository Structure

```text
socialpulse/
│
├── assets/
│   └── images/                         Project image assets
│
├── courses/
│   └── ibm-data-engineering-basics/    Course notes
│
├── dashboard/
│   └── app.py                          Streamlit dashboard
│
├── data/
│   ├── raw/                            Original social-media CSV data
│   └── processed/                      Generated cleaned CSV data
│
├── docs/
│   ├── architecture.md                 Pipeline architecture
│   ├── data_dictionary.md              Field definitions
│   └── user_manual.md                  Setup and usage guide
│
├── sql/
│   ├── schema.sql                      SQLite table definition
│   └── analysis.sql                    Reusable analysis queries
│
├── src/                                Pipeline source code
│   ├── ingest.py
│   ├── validate.py
│   ├── clean.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   ├── analytics.py
│   └── pipeline.py
│
├── tests/                              Automated tests
├── requirements.txt                    Python dependencies
└── README.md
```

---

## 📖 Documentation

- [User Manual](docs/user_manual.md) — step-by-step setup, running, and troubleshooting.
- [Architecture](docs/architecture.md) — pipeline flow and component overview.
- [Data Dictionary](docs/data_dictionary.md) — raw and derived data field definitions.

---

## 📄 License

This project is available under the [MIT License](LICENSE).
