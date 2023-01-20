def K_mat(A):
  n = len(A)
  # look for max 
  k = 0
  for i in range(n):
    for j in range(n):
      for k in in range(n):
        for l in range(n):
          entry = np.sqrt(a[i,j]*a[k,l]/(a[i,l]*a[k,j]))
          if entry > k:
            k = entry
            indices = (i,j,k,l)
  return k, indices
