    """
        ingest.py

        This file's purpose is to load the raw CSV file into pandas

        This is the first stage of the pipeline. Keeping it separate from the other stages means we could swap the CSV for a different source without changing the validate.py, clean.py,transform.py at all
    """

import pandas as pd
from src import config

def load_raw_data(path=None):
    """
    This reads the raw data csv file and it returns it as a DataFrame.
    If no path is given, it uses the default raw data path from config.py
    """
    if path is None:
        path = config.RAW_DATA_PATH

    print(f"Loading raw data from: {path}")
    data = pd.read_csv(path)

    print("Dataset loaded successfully")
    print(f"Rows: {data.shape[0]}")
    print(f"Columns: {data.shape[1]}")

    return data

if __name__ == "__main__":
    # Running "python -m src.ingest" on its own lets us check
    # that the CSV loads correctly, without running the whole pipeline.
    raw_data = load_raw_data()
    print()
    print(raw_data.head())