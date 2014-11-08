import numpy as np
import matplotlib.pylab as plt
from   random import randrange

#box size
L = 101

#initial values of i and j
i = L/2
j = L/2

#empty lists to hold i and j values
i_list = []
j_list = []
#appending the initial position values to the list
i_list.append(i)
j_list.append(j)

for k in range(1000):
    #generating random values for x and y
    randx = randrange(0,L)
    randy = randrange(0,L)
    #setting condition so that particle stays in the box
    if randx>0 and randy>0:
        if randx>L-i-1 and randy>L-j-1:
            i = randx
            j = randy
    if randx>0 and randy<0:
        if randx>L-i-1 and abs(randy)>j-1:
            i = randx
            j = randy
    if randx<0 and randy>0:
        if abs(randx)>i-1 and randy>L-j-1:
            i = randx
            j = randy
    
    if randx<0 and randy<0:
        if abs(randx)>i-1 and abs(randy)>j-1:
            i = randx
            j = randy
    #appending the good x and y positions to the lists
    i_list.append(i)
    j_list.append(j)

#plotting
plt.ion()
plt.figure(figsize=(7,7))
plt.plot(i_list,j_list)
plt.plot(L/2,L/2,'ro')
plt.plot([0, 0], [0, L], 'm-', lw=2) #4
plt.plot([0, L], [L, L], 'm-', lw=2) #3
plt.plot([L, L], [0, L], 'm-', lw=2) #2
plt.plot([0, L], [0, 0], 'm-', lw=2) #1
plt.xlim(-1,L+1)
plt.ylim(-1,L+1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
