"""
Code to compute the confidence intervals of asymmetric histograms.

Written by Nicolas Garavito-Camargo
University of Arizona

03/14/16

To-do:

Implement int main.
Finish doc strings.

"""

import numpy as np
from scipy import interpolate


def interpolate_data(x, y, npoints):
    dx = np.abs(x[1]-x[0])
    f = interpolate.interp1d(x[:-1]+dx/2., y, kind='cubic')
    xnew = np.linspace(min(x[:-1]+dx/2.), max(x[:-1]+dx/2.), 100)
    ynew = f(xnew)
    return xnew, ynew

def y_range(xmin, xmax, x, y):
    """
    Returns an array with the variable y corresponding
    to the values of x in a given range of [xmin, xmax]
    """

    index = np.where((x<xmax) & (x>xmin))
    return y[index]

def confidence_interval(x, y, int_conf=0.68, npoints=100):
    """
    Compute the confidence interval from a histogram
    distribution following this procedure:

    1. Find the maximum of the histogram
    2. Compute the likelihood

    """

    assert(len(x)+1==len(y), "The lenght of the bins array have to be greater by 1 to the len of heights of the histogram")

    xnew, ynew = interpolate_data(x, y, npoints)

    # 1. Finding the median.
    index_max = np.where(ynew == max(ynew))
    x_median = xnew[index_max]

    dx = abs(xnew[1]-xnew[0]) 
    total_area = sum(ynew * dx)

    #2. Find the values of x and y bellow and above x_median
    index_low = np.where(xnew<x_median)
    index_high = np.where(xnew>x_median)

    y_low = ynew[index_low]
    y_high = ynew[index_high]

    x_low = xnew[index_low]
    x_high = xnew[index_high]

    #3. Make a dy interval by the default 100 --> what is best?
    y_steps = np.linspace(min(ynew), max(ynew), 100)

    #4. iterate to find the %area.
    i=1
    p_area = 0
    while p_area <= int_conf:
        delta_y_low = abs(y_low - y_steps[-i])
        delta_y_high = abs(y_high - y_steps[-i])
        #print('y_steps:', y_steps[-i-1])
        min_low = np.argmin(delta_y_low)
        min_high = np.argmin(delta_y_high)
        x_min_low = x_low[min_low]
        x_min_high = x_high[min_high]
        #print(x_min_low, x_min_high)
        y_area = y_range(x_min_low, x_min_high, xnew, ynew)
        p_area = sum(y_area*dx)/total_area
        i+=1

    return x_median, x_min_low, x_min_high

