def edgelist_to_adjmat(edge_list, weight_list, nvertices):
  
  adj_mat = np.zeros((nvertices,nvertices))

  nedges = len(edge_list) # same length as weight list
  for i in range(nedges):
    e1 = edge_list[i][0]
    e2 = edge_list[i][1]
    w = weight_list[i]
    adj_mat[e1, e2 ]= w
  return adj_mat
