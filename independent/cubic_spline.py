import numpy as np
import matplotlib.pylab as plt


#define a function to calculate start point
def start_point(x0,y0,x1,y1):
    '''
    generating equation for k0
    '''
    val = (2./x1-x0)*k0 + (1./x1-x0)*k1 - (3.*(y1-y0)/((x1-x0)**2))
    return val

#define a function to calculate end point
def end_point(xn-1,yn-1,xn,yn):
    '''
    generating equation for kn
    '''
    val = (1./xn-xn-1)*kn-1 + (2./xn-xn-1)*kn - (3.*(yn-yn-1)/((xn-xn-1)**2))
    return val


#define a function to calculate middle points
def mid_points(xi-1,yi-1,xi,yi,xi+1,yi+1):
    '''
    generating equations for k1-kn-1
    '''
    vals = (ki-1/xi-xi-1) + ((1./xi-xi-1)+(1./xi+1-xi))*2*ki + (ki+1/(xi+1-xi)) - (3.*((yi-yi-1/((xi-xi-1)**2)) + (yi+1-yi/((xi+1-xi)**2))))
    return vals

#define a function to solve the n+1 equations
def solver(a,k):
    '''
    solves n equations using numpy solver module
    '''
    val = np.linalg.solve(a,k)
    return val

#define a function to calculate a_i and b_i
def ab():
    '''
    returns a and b coefficients using k values from the matrix solving
    '''
    ai = ki-1*(xi-xi-1) - (yi-yi-1)
    bi = -ki*(xi-xi-1)  + (yi-yi-1)
    return ai,bi

#define a function to calculate q_i
def q(t):
    qi = ((1-t)*yi-1) + t*yi + t*(1-t)*(ai*(1-t) + bi*t)
    return qi

#define a function to find t
def t(x1,x2):
    tval = x-x1/x2-x1
    return tval

#test it with normal sine function and also step function
x = np.linspace(0.0,10.0,5)
y = np.sin(x)

