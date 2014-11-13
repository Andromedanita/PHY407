import numpy as np
import matplotlib.pylab as plt
from   random import randrange,random

'''
This code uses the function f that calculates the distance of a 
point in a sphere to the centre. Then, it loops over N times 
and checks the value of the function for 10 random numbers.
If the value is less than or equal to 1, it will add 1 to 
the sum and if its bigger than one it adds 0. Then we can 
calculate the volume (inntegral) value using V/N * sums
'''

L = 2       #length of side of the cube
n = 10      #number of dimensions
V = L**n    #volume of the cube with side L
N = 1000000 #number of times to run the loop for calculating integral
a = -1.     #lower bound
b = 1.      #upper bound

#distance of a point in a 10 dimensional hypersphere
def f(r):
    vals = r
    vals_sq = r**2
    sum_val = np.sum(vals_sq)
    return sum_val

sums = 0
#looping over N times
for i in range(N):
    #an array of random numbers with size 10
    r = (np.random.uniform(size=10)*2) - 1
    #if the f of array of random numbers is <=1, it adds 1 to the sums
    if f(r) <=1:
        sums += 1
    #if the f of array of random numbers is >1, it adds nothing to the sums
    elif f(r) >1:
        sums+=0

#variance of f
var = (float(sums)/N)-((float(sums)**2)/(N**2))

#integral value
I     = float(V)/N * sums
#error in integral
error = (b-a)*(np.sqrt(var)/np.sqrt(N))
print "The volume of a 10 dimensional hypersphere is:",I,"+/-", error
