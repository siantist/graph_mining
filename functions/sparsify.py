def randomly_sparsify(A, num):
  n = len(A)
  for i in range(num):
    ri = np.random.randint(n)
    rj = np.random.randint(n)
    A[ri, rj] =0
    A[rj, ri] =0
  return A
