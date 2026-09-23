    """
    conftest.py
    Pytest automatically loads this file before running any tests. It makes sure the project's root folder is on the python import path, so the "from src..." and "from tests..." imports work properly no matter which folder pytest is run from.

    """

import sys
from pathlib import pathlib

PROJECT_ROOT = Path(__file__). resolve().parent
if str(PROFECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROFECT_ROOT))