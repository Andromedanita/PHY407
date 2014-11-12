import numpy as np
import matplotlib.pylab as plt
from   random import randrange,random
import time as tt

#number of iterations
N = 10000
#box size
L = 25

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

all_x = []
all_y = []

#while x==L/2 and y==L/2 :

for n in range(30):
    particle = 'True'
    x,y = xp,yp
    print "particle number",n
    while particle=='True':
        x,y = move(x,y,L)
        if x==L or x==0 or y==L or y==0 :
            all_x.append(x)
            all_y.append(y)
            particle = 'False'
        
        for i in range(len(all_x)):
            if (x+1==all_x[i] and y==all_y[i]) or (x-1==all_x[i] and y==all_y[i]) or (x==all_x[i] and y+1==all_y[i]) or (x==all_x[i] and y-1==all_y[i]):
                
                all_x.append(x)
                all_y.append(y)
                print "hit another particle!"
                particle = 'False'

        #xp,yp = x,y
        #plt.plot(x,y,'bo')
        #plt.xlim(0,L)
        #plt.ylim(0,L)
        #tt.sleep(0.001)
        #plt.draw()
        #plt.clf()




