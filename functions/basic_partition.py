import numpy as np
# basic partition of given ordering of vertices
def basic_partition(G, m): # m is number of sets
  n = len(G)
  vertex_sets =[]
  vertex_sets_map = {}
  s = np.floor(n/m)
  for i in range(m):
    ilist= np.arange(i*s, i*s+s)
    vertex_sets.append(ilist)
    vertex_sets_map[i] = ilist

  return vertex_sets, vertex_sets_map
  
def ed(X, Y, A): # adj matrix 
  # count the num edges between X, Y
  num= 0
  for i in X:
    for j in Y:
      Aij = A[i,j]
      if Aij ==1 and i!=j and i<j: # only count once
        num =num+1
  denom = len(X)*len(Y)
  return num/(denom)
