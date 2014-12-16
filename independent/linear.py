import numpy as np
import matplotlib.pylab as plt
from   scipy import interpolate


#-----------------------------------------------------------
#                           Function
#-----------------------------------------------------------
def lin_interp(x,x0,y0,x1,y1):
    '''
    linear interpolation between points (x0,y0) and (x1,y1)
    '''

    y = y0 + (y1-y0)*((x-x0)/(x1-x0))

    return y


#-----------------------------------------------------------
#                       Code Starts Here
#-----------------------------------------------------------
x_array = np.linspace(0.,6.5,10)
y_array = np.sin(x_array)
xvals   = np.linspace(0.1,6.4,20)



n = len(xvals)
yvals = np.zeros(n)


for h in range(len(xvals)):
    print h
    m = 0
    while m<len(x_array):
        if xvals[h]>x_array[m] and xvals[h]<x_array[m+1]:
            yvals[h] = lin_interp(xvals[h],x_array[m],y_array[m],x_array[m+1],y_array[m+1])
        m+=1


f = interpolate.interp1d(x_array,y_array,kind='linear')
py_interp = f(xvals)

#plotting
plt.ion()
plt.plot(x_array,y_array,'bo')
plt.plot(xvals,yvals,'r')
plt.plot(xvals,py_interp,'m')
plt.plot(xvals,np.sin(xvals),'g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("knots","my interpolated values","python interpolated values","Actual function"),loc='best')

plt.show()
