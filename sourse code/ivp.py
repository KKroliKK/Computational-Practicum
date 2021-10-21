import numpy as np


class InitialValueProblem:

    def __init__(self, ODE, findParameterC, generalSolution, x0, y0, X, N, 
                 latexODE=None, latexGeneralSolution=None, latexExact1=None, latexExact2=None):

        # Lambda expression containing ODE
        self._ODE = ODE
        # Lambda expression of general solution with expressed C parameter via x and y
        self._findParameterC = findParameterC
        self._C = self._findParameterC(x0, y0)
        # Lambda expression containing analitical solution
        self._generalSolution = generalSolution
        self._x0 = x0
        self._y0 = y0
        self._X = X
        self._N = N
        # Array of computed x-grid
        self._xArray = np.linspace(x0, X, N + 1)
        # Array of computed exact y-values
        self._analyticalYArray = np.array([self._generalSolution(x, self._C) for x in self._xArray])
        # Latex strings for graph printing
        self._latexODE = latexODE
        self._latexGeneralSolution = latexGeneralSolution
        self._latexExact1 = latexExact1
        self._latexExact2 = latexExact2

    def recompute(self, x0, y0, X, N):
        """Recomputes IVP for new initial conditions"""

        self._C = self._findParameterC(x0, y0)
        self._x0 = x0
        self._y0 = y0
        self._X = X
        self._N = N
        self._xArray = np.linspace(x0, X, N + 1)
        self._analyticalYArray = np.array([self._generalSolution(x, self._C) for x in self._xArray])

    def recomputeForN(self, N):
        """
        Recomputes values for changed N
        It is needed for printing global errors graphs
        """

        self._N = N
        self._xArray = np.linspace(self._x0, self._X, N + 1)
        self._analyticalYArray = np.array([self._generalSolution(x, self._C) for x in self._xArray])
        return self

    def getODE(self, x, y):
        return self._ODE(x, y)

    def getX0(self):
        return self._x0
    
    def getY0(self):
        return self._y0

    def getX(self):
        return self._X

    def getN(self):
        return self._N

    def getC(self):
        return self._C

    def getXArray(self, index=None):
        if index == None:
            return self._xArray
        else:
            return self._xArray[index]

    def getAnalyticalYArray(self, index=None):
        if index == None:
            return self._analyticalYArray
        else:
            return self._analyticalYArray[index]

    def getLatexODE(self):
        return self._latexODE

    def getLatexGeneralSolution(self):
        return self._latexGeneralSolution

    def getLatexExact1(self):
        return self._latexExact1

    def getLatexExact2(self):
        return self._latexExact2