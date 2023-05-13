# https://cs.stanford.edu/~jure/pubs/kronecker-jmlr10.pdf Kronecker Graphs: An Approach to Modeling Networks
def kg_model(g1, num_iter):
  kg1 = g1 
  for i in range(num_iter):
    kg1 = np.kron(g1,kg1)
  
  return kg1 
