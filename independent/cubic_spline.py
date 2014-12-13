import numpy as np
import matplotlib.pylab as plt

#----------------------------------------------------------------
#                         Functions
#----------------------------------------------------------------

#function to calculate start point
def start_point(x0,y0,x1,y1):
    '''
    generating equation for k0
    '''
    a11 = (2./(x1-x0))              #a matrix
    a12 = (1./(x1-x0))              #a matrix
    b   = (3.*(y1-y0)/((x1-x0)**2)) #b matrix
    return a11,a12,b

#function to calculate end point
def end_point(xn_1,yn_1,xn,yn):
    '''
    generating equation for kn
    '''
    a1n_1 = (1./(xn-xn_1))                #a matrix
    a1n   = (2./(xn-xn_1))                #a matrix
    b     = (3.*(yn-yn_1)/((xn-xn_1)**2)) #b matrix
    return a1n_1,a1n,b


#function to calculate middle points
def mid_points(xi_1,yi_1,xi,yi,xip1,yip1):
    '''
    generating equations for k1-kn-1
    '''
    aki_1 = (1./(xi-xi_1))                    #a matrix
    aki   = ((1./(xi-xi_1))+(1./(xip1-xi)))*2 #a matrix
    akip1 = (1./(xip1-xi))                    #a matrix
    return aki_1,aki,akip1

#function to return b values for mid points
def b_vals(xi_1,yi_1,xi,yi,xip1,yip1):
    '''
    generating equations for k1-kn-1
    '''
    b =   3.*(((yi-yi_1)/((xi-xi_1)**2)) + ((yip1-yi)/((xip1-xi)**2)))
    return b


#function to solve the n+1 equations
def solver(a,b):
    '''
    solves n equations using numpy solver module
    '''
    val = np.linalg.solve(a,b)
    return val

#function to calculate a_i and b_i
def ab(xi_1,yi_1,xi,yi,ki_1,ki):
    '''
    returns a and b coefficients using k values from the matrix solving
    '''
    ai = ki_1*(xi-xi_1) - (yi-yi_1)
    bi = -ki*(xi-xi_1)  + (yi-yi_1)
    return ai,bi

#function to calculate q_i
def q(yi_1,yi,ai,bi,t):
    qi = ((1-t)*yi_1) + t*yi + t*(1-t)*(ai*(1-t) + bi*t)
    return qi

#function to find t
def t(x,xi_1,xi):
    tval = (x-xi_1)/(xi-xi_1)
    return tval

#----------------------------------------------------------------
#                        Code Starts Here
#----------------------------------------------------------------

#number of points
n      = 5
points = np.array([[-1.,0.5],[0.0,0.0],[1.0,0.5],[2.0,-0.3],[3.0,3.0]])
a      = np.zeros([n,n])
b      = np.zeros(n)

#generating first and last row of the a matrix
a11,a12,b1    = start_point(points[0][0],
                            points[0][1],points[1][0],points[1][1])
a1n_1, a1n,bn = end_point(points[n-2][0],
                          points[n-2][1],points[n-1][0],points[n-1][1])

#first and last row of matrix a
a[0][0]     = a11
a[0][1]     = a12
a[n-1][-2]  = a1n_1
a[n-1][-1]  = a1n

#first and last component of matrix b
b[0]   = b1
b[n-1] = bn

#generating a and b matrices
for i in range(1,n-1,1):
    print i
    a[i][i-1:i+2]   = mid_points(points[i-1][0],points[i-1][1],points[i][0],points[i][1],points[-+1][0],points[i+1][1])
    b[i] = b_vals(points[i-1][0],points[i-1][1],points[i][0],points[i][1],points[-+1][0],       points[i+1][1])

#solving for k values
k = solver(a,b)

#ai and bi arrays
ai = np.zeros(n)
bi = np.zeros(n)

#computing ai and bi arrays
for j in range(1,n,1):
    ai[j], bi[j] = ab(points[j-1][0],points[j-1][1],points[j][0],points[j][1],k[j-1],k[j])

#number of points in xarray
N = 25
#an array of x values to get the y values out
x_array = np.linspace(-0.9,2.9,N)
y_array = np.zeros(N)


for h in range(len(x_array)):
    print h
    m = 1
    while m<n:
        if x_array[h]>points[m-1][0] and x_array[h]<points[m][0]:
            y_array[h] = q(points[m-1][1],points[m][1],ai[m],bi[m],t(x_array[h],points[m-1][0],points[m][0]))
        m+=1


plt.ion()
plt.plot(x_array,y_array)
plt.plot(points.T[0],points.T[1],'go')
plt.xlim(-1.5,3.5)
plt.ylim(-0.5,3.5)

plt.show()

