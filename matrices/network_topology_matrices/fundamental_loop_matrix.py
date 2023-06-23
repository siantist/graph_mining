# network topology matrices tutorialspoint
# same as cycle basis but in terms of incidence matrix and directed edges (+/- 1) 
def find_fund_loop_matrix(G):
  # select tree 
  tree = find_tree(G)
  # number the edges formed by the tree 
  tree_edges = {}
  # number non tree edges
  nontree_edges = {}
  ind = 0
  for t in tree:
    tree_edges[t] = ind
    ind = ind+1
  
  # include 1 link at a time to get f loop 
  B = np.zeros((len(tree), len(G)))
  for e in G.edges:
    if e not in tree:
      # non tree edge, add
      for e_edge in G[e]:
        # add to the row 
        if e_edge in tree:
          t_row = tree_edegs[e_edge]
          B[t_row, e] = 1     
