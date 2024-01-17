import numpy as np
def kronprodmodel(A, order):
  B = A
  ord = order - 2
  for i in range(ord):
    B = np.kron(B, A)
  return B
