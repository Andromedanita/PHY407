'''
Anita Bahmanyar
Student number: 998909098
'''

import numpy as np
import matplotlib.pylab as plt
import cmath as cm
import banded

##########################################
               #constants#
##########################################
M     = 9.109e-31 #electron mass(Kg)
L     = 1e-8      #meters
h     = 1e-18     #seconds
N     = 1000      #number of timesteps
a     = L/N       #grid soacing
x0    = L/2       #x0 in page 440
sigma = 1e-10 #meters
kappa = 5e10  #1/meters
h_planck = 6.626e-34 #SI units
hbar  = h_planck/(2*np.pi)


# si (x,0) at time=0
def si_initial(x):
    value = np.exp(-((x-x0)**2)/(2*(sigma**2))) * cm.exp(kappa*x)
    return value

b1 = 1 - (h*(complex(hbar)/(2*M*(a**2))))
b2 = h*(complex(hbar)/(4*M*(a**2)))

#defining v matrix as in page 441
def v(si):
    matrix = np.zeros(len(si))
    for i in range(len(si)):
        matrix[i] = (b1*si[i]) + b2*(si[i+1]+si[i-1])
    return matrix

up   = 3
down = 3

x = np.arange(0,L,a)

#solving for Ax = v
si_new = banded(A,v(si_initial(x)),up,down)