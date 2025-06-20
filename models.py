"""Classi di base per rappresentare materiali, fasi e trattamenti."""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Phase:
    """Rappresenta una fase con composizione e proprietà."""
    name: str
    composition: Dict[str, float]
    fraction: float = 0.0

@dataclass
class Material:
    """Materiale costituito da più fasi."""
    name: str
    phases: List[Phase]

    def total_composition(self) -> Dict[str, float]:
        comp: Dict[str, float] = {}
        for phase in self.phases:
            for el, c in phase.composition.items():
                comp[el] = comp.get(el, 0.0) + c * phase.fraction
        return comp
