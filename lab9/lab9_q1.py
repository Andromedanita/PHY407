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

a1 = 1 + (h*(complex(hbar)/(2*M*(a**2))))
a2 = -h*(complex(hbar)/(4*M*(a**2)))
#########################################################
#creating matrix A where n is the dimension of the matrix
#########################################################
def A(n):
    Avals = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i == j:
                Avals[i][j] = a1.real
            elif abs(i-j) == 1:
                Avals[i][j] = a2.real
            else:
                Avals[i][j] = 0
    return Avals


b1 = 1 - (h*(complex(hbar)/(2*M*(a**2))))
b2 = h*(complex(hbar)/(4*M*(a**2)))

#defining v matrix as in page 441
def v(si):
    matrix = np.zeros(len(si))
    for i in range(len(si)-1):
        matrix[i] = (b1.real*si[i]) + b2.real*(si[i+1]+si[i-1])
    return matrix

up   = 3
down = 3

xvalues = np.arange(0,L,a)

###plotting part for animation
#plt.ion()
#fig  = plt.figure()
#ax   = plt.axes(xlim=(0,1),ylim=(-0.006,0.008))
#line = ax.plot(x,si,'-b')
#plt.show()

#solving for Ax = v
si_new = banded(A(len(xvalues)),v(si_return(xvalues)),up,down)

#making animation
#line[0].set_ydata(si_new)
#plt.draw()
#t +=deltat






