def kaczmarz(A, b, rand=False):
  n = len(A)
  m=n # number rows of A
  x0 = np.ones(n)
  xk = x0
  for k in range(30):
    # select i
    i = k % m
    # randomly select i <-> boolean
    if rand:
      i = np.random.rand(pow(A[i],2))
    q = (b[i] - np.dot(A[i], xk))/(pow(A[i],2))
    qi = q*A[i]
    xk = xk + qi

  return xk

# multi-column kaczmarz
def multicol_kaczmarz(A,B):
  # set X_0 as identity
  n = len(A)
  X = np.identity((n,n))
  xmap = {}
  # loop through columns of XB
  for j in range(n):
    b = B[:, j]
    x= kaczmarz(A,b)
    xmap[k] =x

  return xmap
