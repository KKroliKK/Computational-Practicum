from ivp import InitialValueProblem
from numericalMethod import NumericalMethod


class EulerMethod(NumericalMethod):
    """Represents Euler's method"""

    def __init__(self, IVP: InitialValueProblem):
        super().__init__(IVP)

    def _computeYValues(self):
        for i in range(1, self._IVP.getN() + 1):
            self._y[i] = self._y[i - 1] + self._h * self._IVP.getODE(self._IVP.getXArray(i - 1), self._y[ i - 1])