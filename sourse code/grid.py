from abc import ABCMeta
from ivp import InitialValueProblem

class Grid(metaclass=ABCMeta):
    """Abstract class which represents x and y grids"""

    def __init__(self, IVP: InitialValueProblem):
        self._IVP = IVP

    def getXArray(self):
        return self._IVP.getXArray()

    def getYArray(self):
        pass