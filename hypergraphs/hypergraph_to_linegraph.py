# topological simplification of hypergraphs
import numpy as np
def hypergraph_to_linegraph(vh, eh):
  # eh is array of arrays where vertices in each edge is an array
  # turn the edges into vertices 
  vline = {}
  ind=0
  for e in eh:
    vline[ind] = e
    ind=ind+1
  # add edges if intersect
  eline= []
  ind1 =0
  ind2 =0
  for v1 in vline:
    for v2 in vline:
      vals1 = vline[v1]
      vals2 = vline[v2]
      if len(np.intersect1d(vals1, vals2)) > 0: #len(vals1.intersection(vals2)) > 0:
        eline.append([v1, v2])
      ind2 = ind2+1
   ind1 = ind1+1
  
  return vline, eline
