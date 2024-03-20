# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from pylab import *
import numpy as np 
from numpy import *


#%% 
A = np.array([7, 2, 1, 3, 4, 6, 8, 1, 9])
B = np.array([3, -2, 11, 7, 9, 36, -8, 0, 5])
#%% 
# Exercice 1 

print("a)", B[5])
print("b)", B[2:7])
print("c)", B[:4])
print("f)", B[1:-1:2])
print("g)", B[-1:1:-1])


# %% 


#%%
A = np.array(
    [[9,-2, 2],
     [0,7,3],
     [7,3,-4]])

B = np.array(
    [[-3,4,-2],
     [0,1,3],
     [11,0,5]])

b = np.array([[10,11,12]])


#%% 
#exercice 3

print("3A + 2B\n", 3*A+2*B)
print("A^2\n", A@A)
print("A^3\n", A@A@A)
print("A^T x B^T\n", A.T @ B.T)
print("(AxB)^T\n", (A@B).T)

print("a)\n",B[:2,:2])
print("b)\n", B[1])
print("c)\n", B[:,-1])
print("d)\n",B[::2,:-1])

#%% 
# Exercice 4 
b = array([-3,4,-2])

print(delete(A,0,1)) # A[:,1:]
print(delete(A, -1, 0)) # A[:-1,:]
print(insert(A,3, b[::-1], 1))
print(insert(A,0,b, 0)) # concatenate((b,A))
print(diag(A))
print(diag(b))