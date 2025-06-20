import numpy as np
from dataclasses import dataclass

@dataclass
class PolynomialModel:
    """Simple polynomial regression model."""
    coeffs: np.ndarray

    def predict(self, x: float | np.ndarray) -> np.ndarray:
        return np.polyval(self.coeffs, x)


def fit_polynomial(x: np.ndarray, y: np.ndarray, degree: int) -> PolynomialModel:
    """Fit a polynomial of given degree to the data."""
    coeffs = np.polyfit(x, y, degree)
    return PolynomialModel(coeffs)


def fit_elastic_modulus(temperatures: np.ndarray, values: np.ndarray, degree: int = 1) -> PolynomialModel:
    """Return a model predicting elastic modulus as a function of temperature."""
    return fit_polynomial(np.asarray(temperatures), np.asarray(values), degree)


def fit_hardness(temperatures: np.ndarray, values: np.ndarray, degree: int = 1) -> PolynomialModel:
    """Return a model predicting hardness as a function of temperature."""
    return fit_polynomial(np.asarray(temperatures), np.asarray(values), degree)


def larson_miller_parameter(temperature: float, time_hours: float, C: float = 20.0) -> float:
    """Compute the Larson–Miller parameter (LMP). Temperature in Kelvin."""
    return temperature * (C + np.log10(time_hours))


def time_from_lmp(LMP: float, temperature: float, C: float = 20.0) -> float:
    """Return creep rupture time in hours from LMP and temperature."""
    return 10 ** (LMP / temperature - C)


def oxide_thickness(kp: float, time_seconds: float, initial: float = 0.0) -> float:
    """Simple parabolic oxide growth law x^2 = x0^2 + k_p * t."""
    return np.sqrt(initial ** 2 + kp * time_seconds)
