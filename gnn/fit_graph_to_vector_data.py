# sum over the set of vectors

def loss_fn(w,x,d):
  s =0 
  n = len(x)
  m = n
  for i in range(n):
    sj = 0
    for j in range(m):
      sj = sj + w[i,j]*x[j]

    s = s + np.pow(d[i]*x[i] - sj,2)
  return s


# want to minimize
def minimize_it(w, x):
  n= len(x)
  s =0
  for i in range(n):
    for j in range(n):
      s = s+ w[i,j]*np.pow(x[i]- x[j], 2)
  
  return s
