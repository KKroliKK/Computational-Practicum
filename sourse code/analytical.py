from ivp import InitialValueProblem
from grid import Grid


class AnalyticalSolution(Grid):
    """Represents Analytical Solution"""

    def __init__(self, IVP: InitialValueProblem):
        super().__init__(IVP)

    def getYArray(self):
        return self._IVP.getAnalyticalYArray()