# note: how to speed up with python-graphblas
# reciprocal degree distance
def reciprocal_deg_dist(G, shortest_path_matrix):
  n = len(G)
  # compute the sum
  s =0 
  for i in range(n):
    for j in range(n):
      if i != j:
        ideg = sum(G[i])
        jdeg = sum(G[j])
        s= s+ (ideg+jdeg)/shortest_path_matrix[i,j]
  return 0.5*s 
