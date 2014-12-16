import numpy as np
import matplotlib.pylab as plt


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