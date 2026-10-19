"""Generic tabular data import helpers.

Instrument-specific parsers should live in separate modules rather than being
folded into this generic reader.
"""

from pathlib import Path

import pandas as pd


def read_delimited(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a delimited text file into a DataFrame.

    This intentionally performs no scientific interpretation. Column mapping,
    units and instrument metadata should be handled explicitly downstream.
    """
    return pd.read_csv(path, **kwargs)
