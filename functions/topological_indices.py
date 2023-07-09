# copied/edited from mathchem library github.com/hamster3d/mathchem-package/blob/master/mathchem/mathchem.py
# topological index calculation here
# use topological incidence matrices
def zagreb_m1_index(degrees):
    """ Zagreb M1 Index """
    return sum(map(lambda d: d**2, degrees))

#equal to the sum of the products of the degrees of pairs of adjacent vertices.
# map() expects a function and a list
def zagreb_m2_index(degrees, edges):
  s = 0
  for e in edges:
    s = s+ degrees[e[0]]*degrees[e[1]]

  return s
  #return sum( map(lambda (e1, e2): degrees[e1]*degrees[e2] , edges) )

def connectivity_index(degrees, edges, power):
  """ Connectivity index (R)"""
  E = edges # E - all edges
  if len(E) == 0: return 0
  s = 0
  for e in edges:
    s = s + pow(degrees[e[0]]*degrees[e[1]], power)
  return s
  #return np.float64(np.sum( map(lambda (e1 ,e2): ( degrees[e1]*degrees[e2] ) ** power , E) , dtype=np.longdouble))

def augmented_zagreb_index(edges, degrees):
    """ Augmented Zagreb Index"""
    E = edges # E - all edges
    d = degrees
    if len(E) < 2: return 0
    s = 0
    for e in edges:
      s = s+ pow(degrees[e[0]]*degrees[e[1]] / (degrees[e[0]]+ degrees[e[1]]-2),3)
    
    return s
    #return np.float64(np.sum( map(lambda (e1 ,e2): (np.longdouble(d[e1]*d[e2]) / (d[e1]+d[e2]-2)) **3, E) , dtype=np.longdouble))

def eccentric_connectivity_index(degrees, eccentricity):
  """ Eccentric Connectivity Index
  The molecuar graph must be connected, otherwise the function Return False"""
  if not self.is_connected(degrees, eccentricity):
      return False
  return sum( map( lambda a,b: a*b, degrees, eccentricity ) )
