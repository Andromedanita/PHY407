import numpy as np
import matplotlib.pylab as plt
from   random import random,randrange
import random

####################################
#constants
####################################
J        = 1.0
T        = 1.0 #temperature
kb       = 1.0 #Boltzmann constant
beta     = 1.0/(kb*T)
num_iter = 100 #number of iterations

Nx = 20 #x grid dimension
Ny = 20 #y grid dimension
s  = np.zeros([Nx,Ny]) #2D array to hold spin values

#####################################
#functions
#####################################

#function for calculating energy of entire system
def energy(s):
    e_tot = (s[i][i+1] + s[i][i-1] + s[i+1][i] + s[i-1][i])
    E = -J * e_tot
    return E

#funciton for magnetization
def magnet(s):
    return np.sum(s)

#function for accepting probability
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

#####################################
#program starts here
#####################################
#randint(-1,1) # also includes 0

#generating an array of Nx by Ny filled with -1 and 1 randomly
for j in range(20):
    for k in range(20):
        s[j][k] = random.choice([-1,1])

#creating empty lists to hold energy and magnetization values
energy_list = []
magnet_list = []

#adding the energies and magnetization of the current configuration to the list
energy_list.append(energy(s))
magnet_list.append(magnet(s))

for i in range(num_iter):
    #index of array elements chosen randomly
    x = random(1,Nx-1)
    y = random(1,Ny-1)
    E_old = energy(s[x][y])
    s[x][y] *= - 1
    E_new = energy(s[x][y])
    accepting = acceptance(E_new,E_old)
    if accepting == True:
        energy_list.append(E_new)











