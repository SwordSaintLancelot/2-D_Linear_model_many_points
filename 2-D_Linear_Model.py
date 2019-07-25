# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:16:08 2019

@author: GHOST
"""
import numpy as np
import matplotlib.pyplot as plt

def linfit(x,y):
    n = len(x)                  # length of one array
    x1 = np.mean(x)                 # calculate mean for both the vectors to simplify the equations
    y1 = np.mean(y)
    a = (np.sum(x1*y1)-n*x1*y1)/(np.sum(x1**2)-(n*x1*x1))       #Linear Regression Equation. To be derivated using Least Square method
    b = y1-a*x1
    return a,b


def plotting(x,y,a,b):
    plt.scatter(x,y,marker = "x", color = 'red')
    # Plot the first scatter graph with initial values of arrays provided
    pred_val = b+a*x
    #predict the values
    plt.plot(x,pred_val, marker = "o", color="blue")
    #plot the predicted linear regression line
    plt.show()
    

if __name__ =="__main__":
    #n = int(input ('number of coordinates: '))
    x = np.array([0,1,2,3,4,5])
    y = np.array([0,1,2,3,4,5])
    a,b = linfit(x,y)
    plotting(x,y,a,b)