'''
Anita Bahmanyar
Student number: 998909098
'''

import numpy as np
import matplotlib.pylab as plt
import cmath as cm
import banded
from   dcst import dst

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


###########################################
#Initial wavefunction (at t=0):
#This has the shape of a gaussian function
###########################################
def si_initial(x):
    value = np.exp(-((x-x0)**2)/(2*(sigma**2))) * cm.exp(kappa*x)
    return value

#returns si for an array of x values
def si_return(x):
    si  =np.zeros(len(x))
    for i in range(len(x)):
        si[i] = si_initial(x[i])
    return si

#defining E
def energy():
    E = (np.pi**2 * hbar**2 * k**2)/(2 * M * L**2)
    return E

#si_k(x,t)
def si(x,t,k):
    si_vals = np.sin(np.pi * k * x/L) * cm.exp(-E()*t/hbar)
    return

#calculating discrete sine transform
#creating arrays for real and imaginary b values
b_real  = np.zeros(N)
b_imag  = np.zeros(N)
b_k     = b_real + b_imag

si_tot = 0
for k in range(len(x)):
    si_tot += b_k * si_vals(x,t,k)






