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

def ff(x):
    if x<2:
        return 0
    else:
        return 1.

x_array = np.linspace(0.,4,20)
y_array = np.zeros(len(x_array))
for k in range(len(x_array)):
    y_array[k] = ff(x_array[k])

xvals   = np.linspace(0.01,3.99,30)



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
plt.plot(x_array,y_array,'b')
plt.plot(xvals,py_interp,'g')
plt.plot(xvals,yvals,'r')

plt.xlabel("x")
plt.ylabel("y")
plt.legend(("knots","Actual function","python interpolated values","my interpolated values"),loc='best')
plt.ylim(-1,2)
plt.title("Step Function")
plt.show()

