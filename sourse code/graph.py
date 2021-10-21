import matplotlib.pyplot as plt
import numpy as np
import copy
from ivp import InitialValueProblem
from analytical import AnalyticalSolution
from euler import EulerMethod
from improvedEuler import ImprovedEulerMethod
from rungeKutta import RungeKutta


class Graph:
    """Prints graphs for the first and second pages of application"""

    def __init__(self, IVP: InitialValueProblem):
        self._IVP = IVP

    def plotPage1(self, EU=True, IEM=True, RK=True, ES=True):
        """Creates graphs for the first page of application"""

        figure = plt.figure()
        figure.subplots_adjust(top=0.76)
        figure.suptitle('ODE: ' + self._IVP.getLatexODE() + '\nGeneral Solution: ' + self._IVP.getLatexGeneralSolution(), fontsize=15, y=1)

        functionGraph = figure.add_subplot(311)
        functionGraph.set_title('Exact Solution: ' + self._IVP.getLatexExact1() + f'{self._IVP.getC():G}' + self._IVP.getLatexExact2() + ' ', fontsize=15)
        functionGraph.set_xlabel('X-values')
        functionGraph.set_ylabel('Y-values')

        errorGraph = figure.add_subplot(313)
        errorGraph.set_title('Truncation errors', fontsize=15)
        errorGraph.set_xlabel('X-values')
        errorGraph.set_ylabel('Error-values')

        if EU == True:
            euler = EulerMethod(self._IVP)
            functionGraph.plot(euler.getXArray(), euler.getYArray(), color='green', label='Euler')
            errorGraph.plot(euler.getXArray(), euler.getTruncationErrors(), color='green', label='Euler')

        if IEM == True:
            improvedEuler = ImprovedEulerMethod(self._IVP)
            functionGraph.plot(improvedEuler.getXArray(), improvedEuler.getYArray(), color='red', label='Improved Euler')
            errorGraph.plot(improvedEuler.getXArray(), improvedEuler.getTruncationErrors(), color='red', label='Improved Euler')
        
        if RK == True:
            rungeKutta = RungeKutta(self._IVP)
            functionGraph.plot(rungeKutta.getXArray(), rungeKutta.getYArray(), color='orange', label='Runge-Kutta')
            errorGraph.plot(rungeKutta.getXArray(), rungeKutta.getTruncationErrors(), color='orange', label='Runge-Kutta')

        if ES == True:
            exactSolution = AnalyticalSolution(self._IVP)
            functionGraph.plot(exactSolution.getXArray(), exactSolution.getYArray(), color='blue', label='Exact')
        
        functionGraph.legend(loc='lower right')
        errorGraph.legend(loc='lower right')

        return figure


    def plotPage2(self, minN, maxN, EU=True, IEM=True, RK=True):
        """Creates graphs for the second page of application"""

        tmpIVP = copy.deepcopy(self._IVP)

        figure = plt.figure()

        globalErrorGraph = figure.add_subplot(111)
        globalErrorGraph.set_title('Global Error Graph', fontsize=15)
        globalErrorGraph.set_xlabel('N-values')
        globalErrorGraph.set_ylabel('Global Error values')

        xArray = np.array([x for x in range(minN, maxN + 1)])

        if EU == True:
            yArray = np.array([EulerMethod(tmpIVP.recomputeForN(n)).getGlobalError() for n in range(minN, maxN + 1)])
            globalErrorGraph.plot(xArray, yArray, color='green', label='Euler')

        if IEM == True:
            yArray = np.array([ImprovedEulerMethod(tmpIVP.recomputeForN(n)).getGlobalError() for n in range(minN, maxN + 1)])
            globalErrorGraph.plot(xArray, yArray, color='red', label='Improved Euler')

        if RK == True:
            yArray = np.array([RungeKutta(tmpIVP.recomputeForN(n)).getGlobalError() for n in range(minN, maxN + 1)])
            globalErrorGraph.plot(xArray, yArray, color='orange', label='Runge-Kutta')

        globalErrorGraph.legend(loc='lower right')

        return figure