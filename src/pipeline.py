"""
pipeline.py

Responsibility: run the whole SocialPulse pipeline from start to finish.

Order of operations:
    ingest -> validate -> clean -> transform -> save to database

This is the project's main entry point. Run it from the project root with:
    python -m src.pipeline
"""

from src import config
from src.ingest import load_raw_data
from src.validate import run_validation
from src.clean import clean_data
from src.transform import transform_data
from src.load import save_processed_data
from src.database import save_to_database


def run_pipeline():
    print("=" * 50)
    print("SOCIALPULSE PIPELINE STARTING")
    print("=" * 50)

    # Step 1: Ingest the raw CSV
    print("\nSTEP 1: INGESTION")
    raw_data = load_raw_data()

    # Step 2: Validate (reports problems, does not stop the pipeline or
    # change the data - see validate.py)
    print("\nSTEP 2: VALIDATION")
    run_validation(raw_data)

    # Step 3: Clean (fixes the problems validation can detect)
    print("\nSTEP 3: CLEANING")
    cleaned_data = clean_data(raw_data)

    # Step 4: Transform (adds the analytics-ready columns)
    print("\nSTEP 4: TRANSFORMATION")
    transformed_data = transform_data(cleaned_data)

    # Save the processed data as a CSV too, so it can be opened and
    # inspected directly without needing the database.
    processed_data_path = save_processed_data(transformed_data)
    print(f"\nProcessed data saved to: {processed_data_path}")

    # Step 5: Load the processed data into SQLite
    print("\nSTEP 5: DATABASE")
    save_to_database(transformed_data)

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETE")
    print("=" * 50)

    return transformed_data


if __name__ == "__main__":
    run_pipeline()
