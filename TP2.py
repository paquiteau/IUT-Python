#!/usr/bin/env python3
"""Fonctions et boucles for."""

from numpy import *
#%% Exercice Préparatoire
diag([1,2,3])

linspace(1,4,4)

A = ones(4) + diag([1,2,3,4])

A = ones((10,10)) * 5 - 2* diag(ones((10)))



















#%% Exemple 1 

def f(x):
    y = x**2 +1 
    return y 



def matrice(a,b):
    print("dans matrice")
    A = a * ones([1,2])
    B = b * ones([1,2])
    C = concatenate((A,B))
    return C 

def matrice2(a,b):
    print("dans matrice2")

    return array([[a,a],
                  [b,b]])








#%% Exercice 2 

def g(x):
    y = x ** 2 + 3*x + 1 
    return y 






















#%% Exercice 3 

def moyenneUE23(anglais, maths, culture_com):
    
    return (anglais * 2 + math * 3 + culture_com * 2)/7
    

#%% Exercice 4 
def twos(n,p):
    """renvoie une matrice de taille n × p 
    et dont tous les coefficients valent 2."""
    return ones((n,p)) * 2
    

def identite(n):
    """renvoie la matrice identité de taille n × n
    (avec des 1 sur la diagonale et des 0 ailleurs).
    """
    # methode 1 
    I = eye(n) 
    # methode 2 
    I = diag(ones(n))
    return I
    
def matrice1(n):
    """
    renvoie une matrice carrée de taille n × n telle que 
    les n − 1 premières lignes sont composées de 2 
    et la dernière ligne est composée de zéros.   
     """
    mat = twos(n,n)
    mat[-1,:] = 0
    
    concatenate(concatenate([twos(n-1), zeros((1,n-1)]), ones(n, 1)*2)])
    return mat

# %% boucle for 

a = 0
for i in range(10):
    print("a= ", a)
    print("i=", i)
    a=a+i
print("a=",a)

print("====")

a = 0
for i in range(3,10,2):
    print("a= ", a)
    print("i=", i)
    a=a+i
print("a=",a)




#%%
def somme(N):
    s = 0
    for i in range(1,N+1):
        s += i # s = s +i 
    return s 



def somme2(N):
    return N * (N+1)/2

# %% Exercice 6 


def get_A(n,p):
    """A[i,j] = i +j"""
    A = zeros((n,p))
    for i in range(n):
        for j in range(p):
            A[i,j] = i+j 
    return A 

def get_B(n,p):
    """B[i,j] = 2**i * 3 **j"""
    B = zeros((n,p))
    for i in range(n):
        for j in range(p):
            B[i,j] = 2**i * 3**j 

def get_B2(n,p):
    """B[i,j] = 2**i * 3 **j"""
    B = zeros((n,p))
    for i in range(n):
        B[i,:] = 2 ** i
        for j in range(1,p):
            B[i,j] = B[i,j-1] * 3


# %% Exercice 7 

def factoriel(n):
    """Calcule n*(n-1)*(n-2) *.... *1 """
    f=1
    for i in range(1,n+1):
        f *= i
    return f

def factoriel2(n):
    """Calcule n*(n-1)*(n-2) *.... *1 """
    
    if n <= 1:
        return 1 
    return factoriel2(n-1) *n 



#%%  Exercice 9 

def get_A(n):
    """A[i,j] = i+j si i< j i-j sinon """
    
    A= zeros(n)
    for j in range(n):
        for i in range(j):
            A[i,j] = i+j+1+1
        for i in range(j,n):
            A[i,j] = i-j 
    return A 
