# nodeclass7
def homophily(G, Y):
  factor = 1/(num_edges)
  s =0
  for e in edges:
    (u,v) = e
    s = s + bool_check(u,v)
  return s

# relate to the determinant ? determinant(label_i)
def homophily_label(G, label, nodelabels):
  # check which nodes have label
  nodes_label = nodes_with_label(nodelabels, label)
# calculate homophily from kronecker products

# node's first order homophily (https://www.nature.com/articles/s41598-021-92719-6)
# fraction of i's neighbors that are same type as i
def homophily_node(G, labels, v):
  vlabel = labels[v]
  rowv = G[v,:]
  frac = 0
  n = len(G)
  for el in rowv:
    if labels[el] == vlabel:
      frac= frac+1
  return frac/n
