import numpy as np
from abc import ABCMeta
from ivp import InitialValueProblem
from grid import Grid


class NumericalMethod(Grid, metaclass=ABCMeta):
    """Abstract class to represent numerical methods"""

    def __init__(self, IVP: InitialValueProblem):
        super().__init__(IVP)
        self._initYArray()
        self._h = (self._IVP.getX() - self._IVP.getX0()) / self._IVP.getN()
        self._computeYValues()
        self._computeTruncationErrors()

    def _initYArray(self):
        self._y = np.zeros(self._IVP.getN() + 1)
        self._y[0] = self._IVP.getY0()
    
    def _computeYValues(self):
        pass

    def _computeTruncationErrors(self):
        self._truncationErrors = np.zeros(self._IVP.getN() + 1)
        for i in range(1, self._IVP.getN() + 1):
            self._truncationErrors[i] = np.abs(self._IVP.getAnalyticalYArray(i) - self._y[i])

    def getYArray(self):
        return self._y

    def getTruncationErrors(self):
        return self._truncationErrors

    def getGlobalError(self):
        return np.max(self._truncationErrors)