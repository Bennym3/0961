"""Modelli termodinamici semplificati."""

import numpy as np
from typing import Dict

R = 8.314  # J/(mol*K)


def ideal_mixing_free_energy(composition: Dict[str, float], T: float) -> float:
    """Calcola l'energia libera di miscelazione ideale."""
    x = np.array(list(composition.values()))
    x = np.where(x > 0, x, 1e-12)
    return R * T * np.sum(x * np.log(x))


def regular_solution_free_energy(composition: Dict[str, float], T: float, interaction: float) -> float:
    """Modello di soluzione regolare binaria con coefficiente di interazione."""
    if len(composition) != 2:
        raise ValueError("Il modello di soluzione regolare implementato è binario")
    x = list(composition.values())
    return ideal_mixing_free_energy(composition, T) + interaction * x[0] * x[1]


def chemical_potentials(composition: Dict[str, float], T: float) -> Dict[str, float]:
    """Potenziali chimici per soluzione ideale."""
    mu = {}
    for el, x in composition.items():
        x = max(x, 1e-12)
        mu[el] = R * T * (np.log(x) + 1)
    return mu
