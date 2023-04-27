# https://arxiv.org/pdf/1907.07129.pdf
"""
Use the edge curvature distribution to form a graph kernel which uses purely the
graph topology and thereby works for settings when node attributes are not available

Ollivier-Ricci curvature is 1 - W(u,v)/d(u,v) 

W is earth mover distance

https://github.com/saibalmars/GraphRicciCurvature

https://github.com/saibalmars/GraphRicciCurvature/blob/master/GraphRicciCurvature/OllivierRicci.py
"""
def curvature_distribution(G, m): # m is the distribution on nbd of nodes
  for edge in G.edges:
    # calculate W(u,v)
    W(u,v) = # cost is shortest path dist of moving mass from u_i of u to v_j of v
    # ricci curvature
    rc = 1 - W(u,v)/d(u,v)
