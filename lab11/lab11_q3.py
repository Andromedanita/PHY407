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
#defining accepting function
def acceptance(E1,E2):
    if E2<E1:
        return True
    elif E2>E1:
        #probability
        pr = np.exp(-beta*(E2-E1))
        #choosing a random number to check with the probability distribution
        ran = random.random()
        if ran < pr:
            return True
        elif ran > pr:
            return False



####################################
#        Program starts here
####################################

#creating a 2D array to hold dimer positions
points = np.zeros([Nx,Ny])

for i in range(Nx):
    for j in range(Ny):
        points[i][j] =


for k in range(N):
    #choosing random index for the points of the grid
    xx    = randrange(0,Nx)
    yy    = randrange(0,Nx)
    #x2,y2 = adjacent(xx,yy)
    #checking if two points are adjacent
    if (points[xx][yy]-points[xx+1][yy] ==1) or (points[xx][yy]-points[xx-1][yy] ==1)) or  points[xx][yy]-points[xx][yy+1] ==1) or points[xx][yy]-points[xx][yy-1] ==1):
        #check if the adjacent points are empty
        if :
        #add dimer to the grid points
        points[][]






