"""Interfaccia utente minimale per la simulazione."""

import sys
from typing import Dict

import matplotlib.pyplot as plt

from database import ALLOYS
from solver import binary_equilibrium


def run_cli():
    print("Alloy disponibili:")
    for i, name in enumerate(ALLOYS):
        print(f"[{i}] {name}")
    idx = int(input("Seleziona lega: "))
    alloy_name = list(ALLOYS.keys())[idx]
    comp = ALLOYS[alloy_name]
    T = float(input("Temperatura [K]: "))
    interaction = float(input("Parametro di interazione (J/mol): "))
    liq, sol = binary_equilibrium(comp, T, interaction)
    print(f"Frazione liquido: {liq:.2f}")
    print(f"Frazione solido: {sol:.2f}")
    plt.bar(["Liq", "Sol"], [liq, sol])
    plt.title(f"Equilibrio {alloy_name} a {T} K")
    plt.show()


if __name__ == "__main__":
    run_cli()
