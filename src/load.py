"""Write processed SocialPulse data to files for inspection and reuse."""

from src import config


def save_processed_data(data):
    """Save transformed data as a CSV and return its path."""
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(config.PROCESSED_DATA_PATH, index=False)
    return config.PROCESSED_DATA_PATH
