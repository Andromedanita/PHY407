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
num_iter = int(1e5) #number of iterations

Nx = 20 #x grid dimension
Ny = 20 #y grid dimension
s  = np.zeros([Nx,Ny]) #2D array to hold spin values

#####################################
#functions
#####################################

#function for calculating energy of entire system
def energy(s):
    horizontal = np.sum(s[:,:-1]*s[:,1:])
    vertical   = np.sum(s.T[:,:-1]*s.T[:,1:])
    e_tot      = (horizontal+vertical)
    E          = -J * e_tot
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

#generating an array of Nx by Ny filled with -1 and 1 randomly
for j in range(Nx):
    for k in range(Ny):
        s[j][k] = random.choice([-1,1])

#creating empty lists to hold energy and magnetization values
energy_list = []
magnet_list = []

#adding the energies and magnetization of the current configuration to the list
energy_list.append(energy(s))
magnet_list.append(magnet(s))

t = []
t.append(0)
for i in range(num_iter):
    print i
    #index of array elements chosen randomly
    x = random.randrange(0,Nx)
    y = random.randrange(0,Ny)
    E_old = energy(s)
    s[x][y] *= - 1
    E_new = energy(s)
    accepting = acceptance(E_old,E_new)
    if accepting == True:
        energy_list.append(E_new)
        magnet_list.append(magnet(s))
        t.append(i)
    elif accepting == False:
        s[x][y] *= -1

    xvals = np.where(s == 1)
    yvals = np.where(s == -1)
    plt.ion()
    plt.clf()
    plt.plot(xvals[0],xvals[1],'b^',markersize=15)
    plt.plot(yvals[0],yvals[1],'rv',markersize=15)
    plt.xlim(-1,20)
    plt.ylim(-1,20)
    plt.pause(0.0001)
    plt.show()


'''
xvals = np.where(s == 1)
yvals = np.where(s == -1)
plt.ion()
#plt.clf()
plt.plot(xvals[0],xvals[1],'b^',markersize=15)
plt.plot(yvals[0],yvals[1],'rv',markersize=15)
plt.xlim(-1,20)
plt.ylim(-1,20)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spins")
#plt.pause(0.0001)
plt.show()
'''












