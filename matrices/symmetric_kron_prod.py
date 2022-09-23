# from On the Kronecker Product, Kathrin Schacke 

def svec(S):
  # the coefficient q 
  n = len(S)
  for i in range(n):
    for j in range(n):
      Sij = S[i,j]
      

def symm_kron_product(G,H, S): # S is symmetric 
  hsg = np.matmul(H, np.matmul(S, np.matrix.transpose(G))
  gsh = np.matmul(G, np.matmul(S, np.matrix.transpose(H))
