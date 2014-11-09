import numpy as np
import matplotlib.pylab as plt
#from   visual import *
from   random import randrange,random

#box size
L = 101

#initial values of i and j
i = L/2
j = L/2

#empty lists to hold i and j values
i_list = []
j_list = []
#appending the initial position values to the list
i_list.append(i)#_init)
j_list.append(j)#_init)


###plotting part for animation
plt.ion()
fig  = plt.figure()
ax   = plt.axes()
line = ax.plot(i,j,'-b')
plt.show()



for k in range(100):
    
    rand = random()
    if i == L or i == 0 or j == L or j == 0:
        break
    else:
        #if random<0.5, moves in x direction
        if rand<0.5:
            randx = randrange(0,L)
            if randx>0:
                if randx>L-i-1:
                    i = randx
                    j=j
            if randx<0:
                if abs(randx)>i-1:
                    i = randx
                    j = j
            i_list.append(i)
            j_list.append(j)

        #if random>0.5, moves in y direction
        elif rand>0.5:
            randy = randrange(0,L)
            if randy>0:
                if randy>L-j-1:
                    j = randy
                    i = i
            if randy<0:
                if abs(randy)>j-1:
                    j = randy
                    i = i
            i_list.append(i)
            j_list.append(j)
    line[0].set_ydata(i)
    ax.set_title("iteration {0}".format(k))
    plt.draw()


'''
for k in range(500):
    
    rand = random()
    if i == L or i == 0 or j == L or j == 0:
        break
    else:
        #if random<0.5, moves in x direction
        if rand<0.5:
            randx = randrange(0,L)
            if randx>0:
                if randx>L-i:
                    i = randx
                    j=j
                    x_new =
                    y_new =
            if randx<0:
                if abs(randx)>i:
                    i = randx
                    j = j
                    x_new =
                    y_new =
            i_list.append(x_new)
            j_list.append(y_new)
    
        #if random>0.5, moves in y direction
        elif rand>0.5:
            randy = randrange(0,L)
            if randy>0:
                if randy>L-j:
                    j = randy
                    i = i
            if randy<0:
                if abs(randy)>j:
                    j = randy
                    i = i
            i_list.append(i)
            j_list.append(j)
    rate(1000)

'''
'''
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
'''

