"""
conftest.py

Pytest automatically loads this file before running any tests.
It makes sure the project's root folder is on the Python import path,
so imports such as "from src..." work correctly.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))