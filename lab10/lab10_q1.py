import numpy as np
import matplotlib.pylab as plt
from   random import randrange,seed

#########################
#functions
#########################
def move(xp,yp,Lp):
    
    rand = randrange(1,5)
    
    if rand == 1:
        yp+=1
    
    elif rand==2:
        yp-=1
    
    elif rand==3:
        xp+=1
    
    elif rand==4:
        xp-=1

    else:
        print "Something is wrong!"

    return xp,yp

#number of iterations
N = 10000
#box size
L = 101

#initial values of i and j
i = L/2
j = L/2

#empty lists to hold i and j values
x_list = []
y_list = []
#initial condition
xp = L/2
yp = L/2
#appending the initial position values to the list
x_list.append(xp)
y_list.append(yp)

#looping over particle position
for j in range(N):
    print j
    x,y = move(xp,yp,L)
    #changes the random number until its inside the box so that particle does not go outside the box
    while L<x or x<0 or L<y or y<0:
        x,y = move(xp,yp,L)

    x_list.append(x)
    y_list.append(y)
    xp,yp = x,y

plt.ion()
plt.plot(L/2,L/2,'ro')
plt.plot(x_list,y_list,'b')
plt.plot([0, 0], [0, L], 'm-', lw=2) #4
plt.plot([0, L], [L, L], 'm-', lw=2) #3
plt.plot([L, L], [0, L], 'm-', lw=2) #2
plt.plot([0, L], [0, 0], 'm-', lw=2) #1
plt.xlim(-1,L+1)
plt.ylim(-1,L+1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Walk")
plt.show()
    
