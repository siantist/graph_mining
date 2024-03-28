import numpy as np
def degree_matrix(A):
  import numpy as np
  degs = []
  for row in A:
    degs.append(np.sum(row))
  return degs
  
def connectivity_index_matrix(A, edges, power=2): # adjacency matrix
  import numpy as np
  degrees = degree_matrix(A)
  a = connectivity_index_nodes(degrees, edges, power)
  # create diagonal matrix 
  dm = np.diag(a)
  return dm

def albertson_matrix(elist, amat):
  import numpy as np
  am = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      if (i,j) in elist:
        am[i,j] = np.abs(deg(amat, i) - deg(amat,j))
  return am

def first_zagreb_matrix(elist, amat): 
  import numpy as np
  zm = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      if (i,j) in elist:
        zm[i,j] = deg(amat, i) + deg(amat,j)
  return zm
