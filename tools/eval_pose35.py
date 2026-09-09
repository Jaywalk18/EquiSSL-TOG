"""Compatibility entry point; use main_eval_rotation.py for new runs."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from main_eval_rotation import main


if __name__ == "__main__":
    main()
