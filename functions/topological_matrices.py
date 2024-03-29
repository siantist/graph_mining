from graph_mining.functions.topological_indices_nodes import zagreb_m1_index_nodes, zagreb_m2_index_nodes, connectivity_index_nodes, augmented_zagreb_index_nodes, eccentric_connectivity_index_nodes
from graph_mining.functions.degrees_of_nodes import degrees_of_nodes

import numpy as np
def degree_matrix(A):
  import numpy as np
  degs = []
  for row in A:
    degs.append(np.sum(row))
  return degs


def deg_sum_matrix(A):
  import numpy as np
  n = len(A)
  degsums = np.zeros((n,n))
  degrees = degrees_of_nodes(A)
  for i in range(n):
    for j in range(n):
      degsums[i,j] = degrees[i] + degrees[j]
  return degsums
  
def connectivity_index_matrix(A, edges, power=2): # adjacency matrix
  import numpy as np
  degrees = degrees_of_nodes(A)
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
  n = len(amat)
  import numpy as np
  zm = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      if (i,j) in elist:
        zm[i,j] = deg(amat, i) + deg(amat,j)
  return zm
