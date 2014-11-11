import numpy as np
import matplotlib.pylab as plt
from   random import randrange,random
import time as tt

#number of iterations
N = 10000
#box size
L = 101

#initial values of i and j
i = L/2
j = L/2

xp = L/2
yp = L/2

###plotting part for animation
plt.ion()
fig  = plt.figure()
ax   = plt.axes()
line = ax.plot(i,j,'-b')
plt.show()

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



large_xlist = []
large_ylist = []

for n in range(2):
    x_list = []
    y_list = []
    x_list.append(xp)
    y_list.append(yp)

    print "new particle number",n
    for k in range(10000):
        print k
        x,y = move(xp,yp,L)
        while L<x or x<0 or L<y or y<0:
            x,y = move(xp,yp,L)
        x_list.append(x)
        y_list.append(y)

        xp,yp = x,y
        plt.plot(x,y,'bo')
        plt.xlim(0,L)
        plt.ylim(0,L)
        tt.sleep(0.15)
        plt.draw()
        plt.clf()
    large_xlist.append(x_list)
    large_ylist.append(y_list)




