import numpy as np
import matplotlib.pylab as plt
import cmath as cm
from   banded import banded
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

#x values to insert in wave function
x = np.arange(0,L,a)

###########################################
#Initial wavefunction (at t=0):
#This has the shape of a gaussian function
###########################################
def si_initial(x):
    values = np.zeros(len(x))
    value = np.exp(-((x-x0)**2)/(2*(sigma**2))) * np.exp(1j*kappa*x)
    values[0]  = 0
    values[-1] = 0
    return value

#separating real and imaginary parts of the wave function
b_real = si_initial(x).real
b_imag = si_initial(x).imag

#calculating discrete sine fourier transform
alpha = dst(b_real)
eta   = dst(b_imag)
b_k   = alpha + (1j*eta)

#plotting fourier coefficinets (bk)
plt.ion()
plt.plot(b_k)
plt.plot(abs(b_k))
plt.ylabel("Fourier Coefficients")
plt.title("Fourier Coefficients")
plt.show()












