#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:08:39 2024

@author: Pierre-Antoine Comby
"""

from numpy import *
# %% Exercice 1 

A = zeros((3,4))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i,j] = (j+1)* 2**(i+1)
print(A)

# %% Exercice 2 

s = 0 
for i in range(0,158,2):
    s+=i
print(s)

def sommeLigne(A, i):
    """Calcul la somme d'une ligne de A"""
    s = 0 
    for j in range(A.shape[1]):
        s += A[i,j]
    return s 

def sommeLigne2(A,i):
    s=0
    for a in A[i,:]:
        s += a
    return s 

def sommeLigne3(A,i):
    return sum(A[i,:])

print(sommeLigne(A,1))
print(sommeLigne2(A,1))
print(sommeLigne3(A,1))


# %% Exercice 3 

def carre(A):
    return A.shape[0] == A.shape[1]

A = arange(16).reshape(4,4)
B = arange(16).reshape(2,8)
print(A, carre(A))
print(B, carre(B))

# %% Exercice 4 

def h(x):
    if x < -1:
        return 2*x+1 
    elif -1 <= x <= 1: 
        return x**2-2
    else:
        return -x 
    
    
import matplotlib.pyplot as plt

X = linspace(-3,3, 100)
Y = zeros_like(X)
for i in range(len(X)):
    Y[i] = h(X[i])
    
plt.plot(X, Y)
# %% Exercice 5 

def produitEtoile(A,B):
    """equivalent à  A * B"""
    NA, PA = A.shape
    NB, PB = B.shape 
    #if NA != NB or PB != PA: 
    if not(NA==NB and PA==PB):
    #if A.shape != B.shape 
        raise ValueError("Erreur de dimension de matrices")
               
    C = zeros(A.shape)
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i,j] = A[i,j] * B[i,j]
    return C 

A = array([[1,3],[4,6],[3,9]])
B = array([[1,2],[2,6],[6,9]])

C = produitEtoile(A,B) 
print(C)
print(A *B)
# %% Exercice 6 
A=array([[1,2,3],[2,4,5]])
B=array([[-1,2],[-2,5],[3,0]])
i=1
j=1
n=3
coeff=0
for k in range(n) :
    coeff=coeff+A[i,k]*B[k,j]
print(coeff)
print(dot(A,B))

# %% Produit Matriciel  
def produitMatriciel(A,B):
    
    NA, PA = A.shape
    NB, PB = B.shape 
    if PA!= NB:
        raise ValueError("nb colonne de A != nb ligne B")
    C = zeros(NA, PB)
    for i in range(NA):
        for j in range(PB):
            for k in range(NB):
                C[i,j] += A[i,k]*B[k,j]
    return C

