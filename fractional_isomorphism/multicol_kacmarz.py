# multi-column kaczmarz
import kaczmarz
def multicol_kaczmarz(A,B):
  # set X_0 as identity
  n = len(A)
  X = np.identity(n)
  xmap = {}
  # loop through columns of XB
  for j in range(n):
    b = B[:, j]
    x= kaczmarz.Cyclic.solve(A, b) #kaczmarz(A,b)
    xmap[j] =x

  return xmap
