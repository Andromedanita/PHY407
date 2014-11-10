import numpy as np
import matplotlib.pylab as plt
#from   visual import *
from   random import randrange,random
import time as tt

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
'''
##### third trial
for k in range(100):
    print k
    rand = random()
    if i == L or i == 0 or j == L or j == 0:
        break
    else:
        #if random<0.5, moves in x direction
        if rand<0.5:
            randx = randrange(0,L)
            
            i = randx
            j=j
            
            i_list.append(i)
            j_list.append(j)
            plt.plot(i,j,'go')
            plt.ylim(0,101)
            plt.xlim(0,101)
            
            tt.sleep(0.5)
            plt.draw()

        #if random>0.5, moves in y direction
        elif rand>0.5:
            randy = randrange(0,L)
        
            j = randy
            i = i

            i_list.append(i)
            j_list.append(j)
            plt.plot(i,j,'mo')
            plt.ylim(0,101)
            plt.xlim(0,101)
            
            tt.sleep(0.5)
            plt.draw()
'''

##### trial for adding more particles in
for n in range(5):
    print "new particle number",n
    for k in range(100):
        print k
        rand = random()
        if i == L or i == 0 or j == L or j == 0:
            break
        else:
            #if random<0.5, moves in x direction
            if rand<0.5:
                randx = randrange(0,L)
            
                i = randx
                j=j
            
                i_list.append(i)
                j_list.append(j)
                plt.plot(i,j,'go')
                plt.ylim(0,101)
                plt.xlim(0,101)
            
                tt.sleep(0.5)
                plt.draw()
        
            #if random>0.5, moves in y direction
            elif rand>0.5:
                randy = randrange(0,L)
            
                j = randy
                i = i
            
                i_list.append(i)
                j_list.append(j)
                plt.plot(i,j,'mo')
                plt.ylim(0,101)
                plt.xlim(0,101)
            
                tt.sleep(0.5)
                plt.draw()



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

