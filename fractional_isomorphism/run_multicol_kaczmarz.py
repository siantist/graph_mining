import kaczmarz
b = B[:,1]
c= kaczmarz.Cyclic.solve(A, b) # cyclic selection rule
c1 = kaczmarz.MaxDistance.solve(A, b) # max dist selection rule

# test frac isomorphism <-> complete graphs? (what does self edges do? / deleting diagonal?)
A = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
B = [[1,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
import numpy as np
X = np.identity(4)

ax = np.matmul(A,X)
bx = np.matmul(B,X)

A = np.array(A)
B = np.array(B)

C = multicol_kaczmarz(A,B)

#https://pypi.org/project/kaczmarz-algorithms/
