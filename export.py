"""Utility functions to export calculated results."""
import csv
import json
from typing import Mapping, Any


def export_csv(filename: str, data: Mapping[str, Any]) -> None:
    """Write dictionary data to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["property", "value"])
        for key, value in data.items():
            writer.writerow([key, value])


def export_json(filename: str, data: Mapping[str, Any]) -> None:
    """Write dictionary data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
