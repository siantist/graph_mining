def degree_matrix(A):
  degs = []
  for row in A:
    degs.append(np.sum(row))
  return degs
    
