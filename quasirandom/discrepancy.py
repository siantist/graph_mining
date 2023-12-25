# pg 90 of graph theory and additive combinatorics book
def discrepancy(Gn, n, X,Y, p): # Gn is sequence of graphs
  # copute all subsets X, Y in V(G) 
  G = Gn[n]
  # count number edges btwn sets
  exy = count_edges(X, Y) 
  # check condition for quasirandom graphs
  bool = exy == p*len(X)*len(Y)
  return exy, bool
