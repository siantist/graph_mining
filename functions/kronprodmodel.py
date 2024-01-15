import numpy as np
def kronprodmodel(A, order):
  B = A
  for i in range(order):
    B = np.kron(B, A)
  return B
