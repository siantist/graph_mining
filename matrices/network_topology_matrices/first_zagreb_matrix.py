def first_zagreb_matrix(elist, amat): 
  zm = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      if (i,j) in elist:
        zm[i,j] = deg(amat, i) + deg(amat,j)
