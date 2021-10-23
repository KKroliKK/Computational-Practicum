import numpy as np
from ivp import InitialValueProblem
from gui import GUI


class Var12(InitialValueProblem):
    def __init__(self, ODE, findParameterC, generalSolution, x0, y0, X, N,
                 latexODE=None, latexGeneralSolution=None, latexExact1=None, latexExact2=None,
                 exception=None):
        self._checkConstantExistance(x0, y0)
        super().__init__(ODE, findParameterC, generalSolution, x0, y0, X, N,
                         latexODE=latexODE, latexGeneralSolution=latexGeneralSolution, latexExact1=latexExact1, latexExact2=latexExact2,
                         exception=exception)

    def _checkConstantExistance(self, x0, y0):
        if y0 - x0 == 2:
            raise ValueError('C does not exist')

    def _createArrays(self):
        # Create x-grid
        self._xArray = np.linspace(self._x0, self._X, self._N + 1)
        if self._y0 - self._x0 < -2 :
            # Count point of discontinuity
            discontX = 0.25 * np.log(0.25 * np.exp(4 * self._x0) / (1 / (self._y0 - self._x0 - 2) + 0.25))
            # Delete points that are too close to the discontinuty
            # point to avoid errors and too big values
            for i in range(self._N + 2):
                if np.abs(self._xArray[i] - discontX) < 0.001:
                    np.delete(self._xArray, [i])
        # Compute analytical y-values on fixed x-grid
        self._analyticalYArray = np.array([self._generalSolution(x, self._C) for x in self._xArray])

    def recompute(self, x0, y0, X, N):
        self._checkConstantExistance(x0, y0)
        super().recompute(x0, y0, X, N)



# Create instane of IVP for variant 12
var12 = Var12(ODE=lambda x,y: 5 - (y - x) ** 2, # y' = f(x,y)
              findParameterC=lambda x,y: np.exp(-4 * x) * (1 / (y - x - 2) + 1 / 4), # C = k(x, y)
              generalSolution=lambda x,C: 1 / (C * np.exp(4 * x) - 1 / 4) + x + 2, # y = g(x, C)
              x0=0, y0=1, X=20, N=27,
              # Latex strings for GUI printing
              latexODE=r"$y'=5-x^{2}-y^{2}+2xy$",
              latexGeneralSolution=r'$y(x)=\frac{1}{Ce^{4x}-\frac{1}{4}}+x+2$',
              # Latex expression is separated in place where constant C should be substituted
              latexExact1=r'$y(x)=\frac{1}{', # Here value of C will bw placed
              latexExact2=r'e^{4x}-\frac{1}{4}}+x+2$', # Remaining part of the string after C
              exception='C does not exist if\n y0 - x0 = 2')

# To start application the user needs to create
# an instance of class GUI initialized by InitialValueProblem
# instance of needed variant
GUI(var12).startApplication()