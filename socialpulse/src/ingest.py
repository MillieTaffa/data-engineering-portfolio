import pandas as pd
from config import RAW_DATA_PATH


def ingest_raw_data(file_path=RAW_DATA_PATH):
    if not file_path.exists():
        raise FileNotFoundError("Source file is missing")

    data = pd.read_csv(file_path)

    return data


data = ingest_raw_data()

print(data)