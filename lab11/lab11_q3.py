import numpy as np
import matplotlib.pylab as plt
from random import random,randrange

####################################
#            Constants
####################################
Nx = 50  #x dimension
Ny = 50  #y dimension
N  = 100 #number of iterations

####################################
#            Functions
####################################

#function choosing which adjacent point to consider
def adjacent(i,j):
    ran = randrange(0,4)
    if   ran == 1:
        return i-1,j
    elif ran == 2:
        return i+1,j
    elif ran == 3:
        return i,j-1
    elif ran == 4:
        return i,j+1

#function computing energy is minus the number of dimers
def energy(dimers_list):
    E = -len(dimers_list)
    return E


####################################
#        Program starts here
####################################

#creating a 2D array to hold dimer positions
points = np.zeros([Nx,Ny])

for i in range(Nx):
    for j in range(Ny):
        points[i][j] =



for k in range(N):
    #choosing random x and y
    xx    = randrange(0,Nx)
    yy    = randrange(0,Nx)
    x2,y2 = adjacent(xx,yy)
    





