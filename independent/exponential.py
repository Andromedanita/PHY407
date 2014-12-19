'''
Anita Bahmanyar
Comparing linear and cubic interpolation methods using my and scipy module for an exponential function.
'''
import numpy as np
import matplotlib.pylab as plt
from   scipy import interpolate
from   linear import lin_interp
from   cubic_spline import start_point,end_point,mid_points,b_vals,solver,ab,q,t


#-----------------------------------------------------------
#                           Function
#-----------------------------------------------------------
#step function
def f_exp(x):
    vals = np.exp(-4.*(x**2.))
    return vals

#-----------------------------------------------------------
#                       Code Starts Here
#-----------------------------------------------------------
N       = 15 #length of x,y array
x_array = np.linspace(-1.0,4.,N)
y_array = np.zeros(len(x_array))

#-----------------------------------------------------------
#                    Linear Interpolation
#-----------------------------------------------------------
#giving y_array step function values
for k in range(len(x_array)):
    y_array[k] = f_exp(x_array[k])

#number of points between knots
num   = 100
xvals = np.linspace(-0.99,3.99,num)
N     = len(xvals)
yvals = np.zeros(N)

#assigning interpolated values to yvals
for h in range(len(xvals)):
    print h
    m = 0
    while m<len(x_array):
        if xvals[h]>x_array[m] and xvals[h]<x_array[m+1]:
            yvals[h] = lin_interp(xvals[h],x_array[m],y_array[m],x_array[m+1],y_array[m+1])
        m+=1


#scipy linear interpolation function
f  = interpolate.interp1d(x_array,y_array,kind='linear')
#scipy cubic interpolation function
ff = interpolate.interp1d(x_array,y_array,kind='cubic')
#scipy linear interpolation values
py_interp_lin = f(xvals)
#scipy cubic interpolation values
py_interp_cub = ff(xvals)


#-----------------------------------------------------------
#                            Plotting
#-----------------------------------------------------------
plt.ion()
plt.plot(x_array,y_array,'bo')
plt.plot(x_array,y_array,'b')
plt.plot(xvals,py_interp_lin,'g')
plt.plot(xvals,yvals,'r')
plt.plot(xvals,py_interp_cub,'m')

#-----------------------------------------------------------
#                   Cubic Spline Interpolation
#-----------------------------------------------------------

n = 5
points = np.array([[x_array[0],y_array[0]],[x_array[1],y_array[1]],[x_array[2],y_array[2]],[x_array[3],y_array[3]],[x_array[4],y_array[4]],[x_array[5],y_array[5]],[x_array[6],y_array[6]],[x_array[7],y_array[7]],[x_array[8],y_array[8]],[x_array[9],y_array[4]]])

#a and b arrays
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

N = 15
#an array of x values to get the y values out
x_array = np.linspace(-0.99,3.99,N)
y_array = np.zeros(N)

#generating y array to hold interpolated values
for h in range(len(x_array)):
    print h
    m = 1
    while m<n:
        if x_array[h]>points[m-1][0] and x_array[h]<points[m][0]:
            y_array[h] = q(points[m-1][1],points[m][1],ai[m],bi[m],t(x_array[h],points[m-1][0],points[m][0]))
        m+=1


#-----------------------------------------------------------
#                            Plotting
#-----------------------------------------------------------
plt.plot(x_array,y_array,'c')
plt.xlabel("$x$",fontsize=15)
plt.ylabel("$y$",fontsize=15)
plt.legend(("knots","Actual function","python linear interpolation","my linear interpolation","python cubic interpolation","my cubic interpolation"),loc='best')
plt.title("$e^{(-4x^2)}$",fontsize=20)
plt.show()

