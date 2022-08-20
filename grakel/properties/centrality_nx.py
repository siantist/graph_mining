# centrality 
# https://networkx.org/documentation/stable/reference/algorithms/centrality.html

# ex 1 

import networkx as nx

G1 =nx.Graph()

G1.add_nodes_from([1,2,3,4,5])

G1.add_edges_from([(2,3),(1,3), (3,4), (3,5)])

# ex 2

G2 = nx.Graph()
G2.add_nodes_from([1,2,3,4,5])

G2.add_edges_from([(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)])
# ex 3

G3 = nx.Graph()

G3.add_nodes_from([1,2,3,4,5])

G3.add_edges_from([(1,2),(1,3),(3,4),(2,5), (3,5),(4,5)])

nx.degree_centrality(G1)
nx.eigenvector_centrality(G1)
nx.closeness_centrality(G1)
nx.current_flow_closeness_centrality(G1)
nx.betweenness_centrality(G1)
# also have the np version of the same functions
