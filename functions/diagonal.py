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
