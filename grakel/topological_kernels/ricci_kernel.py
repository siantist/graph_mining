# https://arxiv.org/pdf/1907.07129.pdf
"""
Use the edge curvature distribution to form a graph kernel which uses purely the
graph topology and thereby works for settings when node attributes are not available

Ollivier-Ricci curvature is 1 - W(u,v)/d(u,v) 

W is earth mover distance

https://github.com/saibalmars/GraphRicciCurvature

https://github.com/saibalmars/GraphRicciCurvature/blob/master/GraphRicciCurvature/OllivierRicci.py

!pip install GraphRicciCurvature
"""

import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.FormanRicci import FormanRicci


def ricci_kernel(G1, G2):
  orc1 = OllivierRicci(G1, alpha=0.5, verbose="INFO")
  orc2 = OllivierRicci(G2, alpha=0.5, verbose="INFO")
  orc1.compute_ricci_curvature()
  orc2.compute_ricci_curvature()
  c1 = orc1.G[0][1]["ricciCurvature"]
  c2 = orc2.G[0][1]["ricciCurvature"]
  return np.exp(-np.pow(c1 - c2, 2)/(2*np.pow(sigma,2)))
  

def curvature_distribution(G, m): # m is the distribution on nbd of nodes
  for edge in G.edges:
    # calculate W(u,v)
    W(u,v) = # cost is shortest path dist of moving mass from u_i of u to v_j of v
    # ricci curvature
    rc = 1 - W(u,v)/d(u,v)
