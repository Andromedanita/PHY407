import numpy as np
import matplotlib.pylab as plt
import cmath as cm
from   banded import banded
from   dcst import dst,idst

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

#calculating discrete sine transform
b_real = si_initial(x).real
b_imag = si_initial(x).imag

alpha  = dst(b_real)
eta    = dst(b_imag)
b_k    = alpha + eta

k = np.linspace(1,len(b_k),N)

#the arguement inside cos and sin function on page 443
vals = ((np.pi**2)*(hbar)*(k**2))/(2*(M)*(L**2))

plt.ion()
fig  = plt.figure()
ax   = plt.axes(xlim=(0,1e-8))
line = ax.plot(x,si_initial(x),'-b')
plt.show()

n    = 100
t    = 0
tend = 1e-16 #s
while t<tend:
    
    first    = alpha*(np.cos(vals*t))
    second   = eta*(np.sin(vals*t))
    tot      = (first-second)*(np.sin((np.pi*k*n))/N)
    true_val = idst(tot)
    real_val = true_val.real
    
    line[0].set_ydata(real_val)
    plt.draw()
    print t
    t +=h








