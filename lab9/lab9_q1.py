'''
Anita Bahmanyar
Student number: 998909098
'''

import numpy as np
import matplotlib.pylab as plt
import cmath as cm
from   banded import banded

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
    value = np.exp(-((x-x0)**2)/(2*(sigma**2))) * np.exp(1j*kappa*x)
    return value
'''
#returns si for an array of x values
def si_return(x):
    si  =np.zeros(len(x))
    for i in range(len(x)):
        si[i] = si_initial(x[i])
    return si
'''

a1 = 1 + (h*(complex(hbar)/(2*M*(a**2))))
a2 = -h*(complex(hbar)/(4*M*(a**2)))
#########################################################
#creating matrix A where n is the dimension of the matrix
#########################################################
def A(n,a1,a2):
    a_diag = np.zeros(n,complex)
    a_sup  = np.zeros(n,complex)
    a_sub  = np.zeros(n,complex)

    a_diag[0]     = 1
    a_diag[n-1]   = 1
    a_diag[1:n-1] = a1
    a_sup[2:]     = a2
    a_sub[:-2]    = a2
    
    return np.array([a_sup,a_diag,a_sub])


b1 = 1 - (h*(complex(hbar)/(2*M*(a**2))))
b2 = h*(complex(hbar)/(4*M*(a**2)))

#defining v matrix as in page 441
def v(si):
    matrix = np.zeros(len(si),complex)
    for i in range(len(si)-1):
        matrix[i] = (b1*si[i]) + b2*(si[i+1]+si[i-1])
    return matrix

up   = 1
down = 1
xvalues = np.arange(0,L,a)

si_vals = si_initial(xvalues)
###plotting part for animation
plt.ion()
fig  = plt.figure()
ax   = plt.axes(xlim=(0,1e-8))
line = ax.plot(xvalues,si_vals,'-b')
plt.show()


#calling A function to create the matrix
A       = A(len(xvalues),a1,a2)

t    = 0
tend = 1e-15 #seconds
si_solutions = [] #an empty list to include si values
while t<tend:
    si_new = banded(A,v(si_vals),up,down)
    si_solutions.append(si_new)
    si_vals = si_new
    
    line[0].set_ydata(si_new)
    plt.draw()
    print t
    t += h





