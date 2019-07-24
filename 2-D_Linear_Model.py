# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:16:08 2019

@author: GHOST
"""
import numpy as np
import matplotlib.pyplot as plt

def linfit(x,y):
    n = len(x)
    a = (sum(x*y)-1/n*sum(x)*sum(y))/ ((sum(x**2))-1/n*(sum(x)**2))
    b = sum(y)/n-sum(x)/n*a
    return a,b


if __name__ =="__main__":
    n = int(input ('number of coordinates: '))
    x,y = [],[]
    for i in range(n):
        x.append( int(input("enter the x coordinates: ")))
        y.append(int( input("enter the y coordinates: ")))
    a,b = linfit(x,y)
    nx = [np.arange(-20,2,50)]
    ny = a*nx+b
    plt.scatter(nx,ny)
    plt.show()