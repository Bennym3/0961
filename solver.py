"""Procedura semplificata per calcolare l'equilibrio di due fasi."""

from typing import Dict, Tuple
import numpy as np

from thermodynamics import regular_solution_free_energy


def binary_equilibrium(composition: Dict[str, float], T: float, interaction: float) -> Tuple[float, float]:
    """Stima rozza dell'equilibrio liquido-solido per un sistema binario."""
    x = composition.copy()
    g_liq = regular_solution_free_energy(x, T, interaction)
    x_s = {list(x.keys())[0]: 0.0, list(x.keys())[1]: 1.0}
    g_sol = regular_solution_free_energy(x_s, T, interaction)
    if g_liq < g_sol:
        return 1.0, 0.0
    else:
        return 0.0, 1.0
