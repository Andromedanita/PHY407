import numpy as np
import matplotlib.pylab as plt
from   scipy import interpolate


#--------------------------------------------------------------
#                           Function
#--------------------------------------------------------------
def bilinear(x,y,points):

    '''
    The value of the points entered should be increasing
    points should be entered in the following format:
    [(x1,y1,Q11),(x1,y2,Q12),(x2,y1,Q21),(x2,y2,Q22)]
    If this is not the order the points are entered, it is also fine.
    The code will sort the points as needed.
    '''
    
    #sorting points
    points = sorted(points)
    #assigning values of points
    (x1,y1,Q11),(x1,y2,Q12),(x2,y1,Q21),(x2,y2,Q22) = points
    
    value = ( Q11 * (x2 - x) * (y2 - y) +
              Q21 * (x - x1) * (y2 - y) +
              Q12 * (x2 - x) * (y - y1) +
              Q22 * (x - x1) * (y - y1)
              ) / ((x2-x1) * (y2-y1))

    return value

#--------------------------------------------------------------
#                     Code Starts Here
#--------------------------------------------------------------
Q11 = 0.
Q12 = 1.
Q21 = 1.
Q22 = 0.5
x1  = 0.
y1  = 0.
x2  = 1.
y2  = 1.

n = 10
points = [(x1,y1,Q11),(x1,y2,Q12),(x2,y1,Q21),(x2,y2,Q22)]

xvals = np.linspace(0.,1.,n)
yvals = np.linspace(0.,1.,n)

table = np.zeros([n,n])

for i in range(n):
    for j in range(n):
        table[i][j] = bilinear(xvals[i],yvals[j],points)


xx = [0.,1.]
yy = [0.,1.]
z = [[0.5,1.],[1.,0.5]]
py_interp = interpolate.interp2d(xx,yy,z)

#mean value between my interpolation and scipy interpolation values
np.mean(abs(w(xvals,yvals)-table))

#--------------------------------------------------------------
#                           Plotting
#--------------------------------------------------------------
plt.ion()
plt.subplot(211)
plt.contourf(xvals,yvals,table,100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("My Interpolated values in a unit square")
plt.colorbar()
plt.subplot(212)
plt.contourf(xvals,yvals,py_interp(xvals,yvals),100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scipy Interpolated values in a unit square")
plt.colorbar()
plt.show()


