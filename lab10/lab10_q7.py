import numpy            as np
import matplotlib.pylab as plt
from   random import random,randrange,seed
import gaussxw as g

#number of iterations for calculating the integral each time
N      = 10000
N_hist = 100
seed(42)


#function indicating simplified form of f(x)/w(x)
def fw(x):
    return 1./(np.exp(x) + 1.)

#an epmty array holding all the values of integrals in
sum_list = []
#looping over N_hist times to generate the histogram
for j in range(N_hist):
    z  = np.random.uniform(size=N) #uniform random number
    xx = z**2     #squaring z since the form is:  x(z) = z^2

    print "j is:",j
    sums = 0
    #looping over N times
    for i in range(N):
        sums += fw(xx[i])
    sum_list.append(sums)

sum_list = np.array(sum_list)

'''
###### gaussian quadrature for w(x)
N = 5000
a = 0.0
b = 1.0
x,w = g.gaussxwab(N,a,b)

#performing th integration
s = 0.0
N_intg = 100
for i in range(N_intg):
    s += w[i] * fw(x[i])
'''

#value of the integral of w
s = 2.

#value of the whole integral
I = (1./N) * sum_list * s

#plotting histogram
plt.ion()
plt.hist(I,10,range=[0.8, 0.88]) #10 bins
plt.show()

