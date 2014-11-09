import numpy as np
import matplotlib.pylab as plt
from   random import randrange,random

###############################################
##calculating integral using mean value method
###############################################

#defining function f(x)
def f(x):
    integrand = (x**-0.5)/(np.exp(x) +1)
    return integrand

#start and end point of integration
a    = 0
b    = 1
N    = 10000
#sums = 0

I_list = []
for j in range(100):
    sums = 0
    for i in range(N):
        rand = random()
        sums += f(rand)
    I = (float(b-a)/N)*sums
    I_list.append(I)

plt.ion()
plt.hist(I_list,10,range=[0.8, 0.88])
plt.ylabel("number")
plt.xlabel("I")
plt.show()
