def connectivity_index_matrix(A): # adjacency matrix
  
  a = connectivity_index_nodes(degrees, edges, power)
  # create diagonal matrix 
  dm = np.diag(a)
  return dm
