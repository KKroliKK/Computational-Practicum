from ivp import InitialValueProblem
from numericalMethod import NumericalMethod


class RungeKutta(NumericalMethod):
    """Represents Runge-Kutta method"""

    def __init__(self, IVP: InitialValueProblem):
        super().__init__(IVP)

    def _computeYValues(self):
        for i in range(1, self._IVP.getN() + 1):
            k1 = self._h * self._IVP.getODE(self._IVP.getXArray(i - 1), self._y[i - 1])
            k2 = self._h * self._IVP.getODE(self._IVP.getXArray(i - 1) + self._h / 2, self._y[i - 1] + k1 / 2)
            k3 = self._h * self._IVP.getODE(self._IVP.getXArray(i - 1) + self._h / 2, self._y[i - 1] + k2 / 2)
            k4 = self._h * self._IVP.getODE(self._IVP.getXArray(i - 1) + self._h, self._y[i - 1] + k3)
            self._y[i] = self._y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6