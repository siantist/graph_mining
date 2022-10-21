def neighbors(i, G):
  irow = G[i]
  n = len(G)
  ns = []
  for j in range(n):
    if irow[j] == 1:
      ns.append(j)
    j+=1
  return ns

def cuthillmckee_variant1(G, properties): # adjacency matrix G
  # find obj with minimum property
  imin = properties.index(min(properties))
  ordering= []
  # add
  ordering.append(imin)
  # add neighbors 
  nlist= neighbors(imin, G)
  npairs =[]
  for ne in nlist:
    npairs.append((ne, properties[ne]))
  # order them
  nlist.sort(key= sort_key)
  ordering.extend(nlist)

  return ordering
  

