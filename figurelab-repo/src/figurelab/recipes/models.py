"""Models for reproducible processing recipes."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ProcessingStep:
    """One named processing operation and its explicit parameters."""

    operation: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Recipe:
    """Ordered collection of processing steps."""

    name: str
    steps: tuple[ProcessingStep, ...] = ()
