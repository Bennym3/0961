"""Utility per esportare i risultati."""

import pandas as pd


def export_table(data: dict, filename: str) -> None:
    """Esporta un dizionario come tabella CSV."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
