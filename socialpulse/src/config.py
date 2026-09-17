from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "social_media.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "social_media_clean.csv"
DATABASE_PATH = BASE_DIR / "database" / "socialpulse.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"