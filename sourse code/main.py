import numpy as np
from ivp import InitialValueProblem
from gui import GUI


# Create instane of IVP for variant 12
var12 = InitialValueProblem(ODE=lambda x,y: 5 - (y - x) ** 2, # y' = f(x,y)
                            findParameterC=lambda x,y: np.exp(-4 * x) * (1 / (y - x - 2) + 1 / 4), # C = k(x, y)
                            generalSolution=lambda x,C: 1 / (C * np.exp(4 * x) - 1 / 4) + x + 2, # y = g(x, C)
                            x0=0, y0=1, X=20, N=27,
                            # Latex strings for GUI printing
                            latexODE=r"$y'=5-x^{2}-y^{2}+2xy$",
                            latexGeneralSolution=r'$y(x)=\frac{1}{Ce^{4x}-\frac{1}{4}}+x+2$',
                            # Latex expression is separated in place where constant C should be substituted
                            latexExact1=r'$y(x)=\frac{1}{', # Here value of C will bw placed
                            latexExact2=r'e^{4x}-\frac{1}{4}}+x+2$') # Remaining part of the string after C

# To start application the user needs to create
# an instance of class GUI initialized by InitialValueProblem
# instance of needed variant
GUI(var12).startApplication()