# edit the whole graph functions from above to apply to each node

# for edges input, refer to incidence matrix to apply to nodes that are in edge

# July 9 code :

def zagreb_m1_index_nodes(degrees):
    """ Zagreb M1 Index """
    return map(lambda d: d**2, degrees)

# incidence list: edges connected to each node ?
def zagreb_m2_index_nodes(degrees, edges): # incidence list: the nodes connected to each edge? <= apply topological incidence list
  node_map = {}
  #print("edges are ", edges)
  s = 0
  for e in edges:
    s = degrees[e[0]]*degrees[e[1]]
    if node_map.get(e[0]) == None:
      node_map[e[0]] = s 
    if node_map.get(e[1]) == None:
      node_map[e[1]] = s 
    
    if node_map.get(e[0]) != None:
      n1 = node_map[e[0]]
      node_map[e[0]] = n1 + s
    
    if node_map.get(e[1]) != None:
      n2 = node_map[e[1]]
      node_map[e[1]] = n2 + s
  
  node_arr = [] # list(node_map.values())
  for i in node_map.values():
    node_arr.append(i)
  
  return node_arr

def connectivity_index_nodes(degrees, edges, power):
  node_map = {}
  for e in edges:
    s = pow(degrees[e[0]]*degrees[e[1]], power)
    if node_map.get(e[0]) == None:
      node_map[e[0]] = s 
    if node_map.get(e[1]) == None:
      node_map[e[1]] = s 
    
    if node_map.get(e[0]) != None:
      n1 = node_map[e[0]]
      node_map[e[0]] = n1 + s
    
    if node_map.get(e[1]) != None:
      n2 = node_map[e[1]]
      node_map[e[1]] = n2 + s
    #n1 = node_map[e[0]]
    #n2 = node_map[e[1]]
    #node_map[e[0]] = n1 + s
    #node_map[e[1]] = n2 + s
  
  #node_arr = node_map.values()
  node_arr = [] # list(node_map.values())
  for i in node_map.values():
    node_arr.append(i)
  return node_arr

def augmented_zagreb_index_nodes(edges, degrees):
    """ Augmented Zagreb Index"""
    E = edges # E - all edges
    d = degrees
    if len(E) < 2: return 0
    s = 0
    node_map = {}
    for e in edges:
      s = pow(degrees[e[0]]*degrees[e[1]] / (degrees[e[0]]+ degrees[e[1]]-2),3)
      if node_map.get(e[0]) == None:
        node_map[e[0]] = s 
      if node_map.get(e[1]) == None:
        node_map[e[1]] = s 
      
      if node_map.get(e[0]) != None:
        n1 = node_map[e[0]]
        node_map[e[0]] = n1 + s
      
      if node_map.get(e[1]) != None:
        n2 = node_map[e[1]]
        node_map[e[1]] = n2 + s

    #node_arr = node_map.values()
    node_arr = [] # list(node_map.values())
    for i in node_map.values():
      node_arr.append(i)
    return node_arr

def eccentric_connectivity_index_nodes(edges, degrees, eccentricity):
  node_map = {}
  for e in edges:
    s1 = degrees[e[0]]*eccentricity[e[0]]
    s2 = degrees[e[1]]*eccentricity[e[1]]
    if node_map.get(e[0]) == None:
      node_map[e[0]] = s 
    if node_map.get(e[1]) == None:
      node_map[e[1]] = s 
    
    if node_map.get(e[0]) != None:
      n1 = node_map[e[0]]
      node_map[e[0]] = n1 + s
    
    if node_map.get(e[1]) != None:
      n2 = node_map[e[1]]
      node_map[e[1]] = n2 + s
  #node_arr = node_map.values()
  node_arr = [] # list(node_map.values())
  for i in node_map.values():
    node_arr.append(i)
  return node_arr # return sum( map( lambda a,b: a*b, degrees, eccentricity ) )
