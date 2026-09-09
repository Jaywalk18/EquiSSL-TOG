"""Resolve external source and dataset paths used by the release."""

import importlib.util
import os
import re
import sys
from pathlib import Path


def add_sphere_uformer_to_path() -> None:
    """Make an external SphereUFormer source tree importable and validate it."""
    source = os.environ.get("SPHERE_UFORMER_SRC")
    if source:
        source_path = Path(source).expanduser().resolve()
        if not source_path.is_dir():
            raise FileNotFoundError(
                f"SPHERE_UFORMER_SRC is not a directory: {source_path}"
            )
        if str(source_path) not in sys.path:
            sys.path.insert(0, str(source_path))
    if (
        importlib.util.find_spec("trimesh_utils") is None
        or importlib.util.find_spec("network") is None
    ):
        raise ImportError(
            "SphereUFormer source was not found. Set SPHERE_UFORMER_SRC to "
            "its src directory or add that directory to PYTHONPATH."
        )


def sphere_uformer_data_dir() -> Path:
    """Find the data files distributed with SphereUFormer."""
    add_sphere_uformer_to_path()
    try:
        import trimesh_utils
    except ImportError as exc:
        raise ImportError(
            "SphereUFormer is required. Set SPHERE_UFORMER_SRC to its src "
            "directory or add that directory to PYTHONPATH."
        ) from exc
    return Path(trimesh_utils.__file__).resolve().parent / "data"


def dataset_dir(value: str | None, environment: str) -> str:
    """Use an explicit dataset path or a named environment variable."""
    path = value or os.environ.get(environment)
    if not path:
        raise ValueError(f"Set {environment} or provide the dataset path explicitly.")
    resolved = Path(os.path.expandvars(path)).expanduser()
    if re.search(r"\$\{[A-Za-z_][A-Za-z0-9_]*\}", str(resolved)):
        raise ValueError(f"Unresolved environment variable in dataset path: {path}")
    if not resolved.is_dir():
        raise FileNotFoundError(f"Dataset directory does not exist: {resolved}")
    return str(resolved.resolve())
