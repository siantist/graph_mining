# map back to an adjacency (weighted edge) matrix 
# vector is of topological indices
def map_to_edgemat(vector, degrees, edge_list): 
  wts = []
  for e in edge_list: 
    s = vector[e[0]]/(degrees[e[0]]) + vector[e[1]]/(degrees[e[1]])
    wts.append(s)
  #reshape into adj mat nx.adjacency_matrix(G)
  nvertices = np.max(edge_list)
  a = edgelist_to_adjmat(edge_list, wts, nvertices)
  return a 
