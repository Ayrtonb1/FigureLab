"""Project-level domain models."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Measurement:
    """Reference to one source measurement without altering the raw file."""

    technique: str
    source_path: Path
    sample_id: str | None = None
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Project:
    """A collection of measurements belonging to one research project."""

    name: str
    measurements: tuple[Measurement, ...] = ()
