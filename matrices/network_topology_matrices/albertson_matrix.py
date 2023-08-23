def albertson_matrix(elist, amat):
  am = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      if (i,j) in elist:
        am[i,j] = np.abs(deg(amat, i) - deg(amat,j))
  return am
