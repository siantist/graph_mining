# nodeclass7
# measure / reorder the nodes for diagonal maximization

# algo for diagonal maximization:
def diag_sum(A):
  # principal and secondary
  principal = 0
  secondary =0
  n = len(A)
  for i in range(n):
    for j in range(n):
      if i == j:
        principal = principal + A[i,j]
      else:
        if (i+j) == (n-1):
          secondary = secondary + A[i,j]
  return principal, secondary

from scipy.optimize import minimize
# https://docs.scipy.org/doc/scipy/tutorial/optimize.html
# random array
import numpy as np
ra = np.random.rand(3,3)
ra1 = np.reshape(ra, (9,1))
res = minimize(diag_sum, ra1, jac='BFGS')

def sum_diag(A, j, eps):
  s = 0 
  n = len(A)
  for i in range(n):
    s = s+ A[i,i] +A[i-j, i] + A[i, i+j] 

  # compare to trace 
  t = np.matrix.trace(A)
  return s, t

#scale each row by the stationary dist?
def scale_by_stationary(A, pi):
  n = len(A)
  B = np.zeros(n,n)
  for i in range(len(pi)):
    p = pi[i]
    B[i] = p*A[i]
  return B

# turn stationary distribution into a diagonal matrix
def diag_mat(pi):
  n = len(pi)
  D = np.zeros((n,n))
  for i in range(n):
    D[i,i] = pi[i]
  return D
# determine the stationary dist based on diff graph invariants
def det_stat_dist(A):#, Ainvariant): # Ainvariant matrix is matrix of inv
  Atranspose = A.T
  eigenvals, eigenvects = np.linalg.eig(A)
  close_to_1idx = np.isclose(eigenvals, 1)
  target_eigenvect = eigenvects[:, close_to_1idx]
  target_eigenvec = target_eigenvect[:,0]
  stat_dist = target_eigenvec/sum(target_eigenvec)
  return stat_dist
