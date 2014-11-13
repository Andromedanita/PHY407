import numpy as np
import matplotlib.pylab as plt
from   random import randrange,random
import time as tt


N = 10000 #number of iterations
L = 101  #box size

#initial position of particles (center)
xp = L/2
yp = L/2

###plotting part for animation
plt.ion()
fig  = plt.figure()
ax   = plt.axes()
line = ax.plot(xp,yp,'-b')
plt.show()

#########################
#functions
#########################
def move(xp,yp,Lp):
    
    #random integer (1,2,3,4)
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

#empty lists to hold final position of each particle
all_x = []
all_y = []

r = True
while r == True:
    particle = 'True'
    x,y = xp,yp
    #runs until the particle hits boundary or another particle
    while particle=='True':
        x,y = move(x,y,L)  #moving particle randomly
        #if particles hit the boundary of the box it will stop
        
        if x==L or x==0 or y==L or y==0 :
            all_x.append(x)
            all_y.append(y)
            particle = 'False'
        
        for i in range(len(all_x)):
            #if adding 1 to the position of particles would cause the particle to hit another particle, it would append that position to the list as the final position and makes the particle to be False so that it breaks out of the while loop
            if (x+1==all_x[i] and y==all_y[i]) or (x-1==all_x[i] and y==all_y[i]) or (x==all_x[i] and y+1==all_y[i]) or (x==all_x[i] and y-1==all_y[i]):
                
                all_x.append(x)
                all_y.append(y)
                particle = 'False'
                #checking if the particle position is at center then it stops the whole loop (the outer while loop) since it makes r to be False
                if x == xp and y == yp:
                    r = False
        
        #plotting
        plt.clf()
        plt.plot(x,y,'bo')
        plt.plot(all_x,all_y,'ro')
        plt.xlim(-1,L+1)
        plt.ylim(-1,L+1)
        #tt.sleep(0.001)
        
    plt.draw()







