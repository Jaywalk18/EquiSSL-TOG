"""Compatibility entry point; use main_finetune_seg.py for new runs."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from main_finetune_seg import main


if __name__ == "__main__":
    main()
