import networkx as nx
from sknetwork.clustering import Louvain
from sklearn.metrics.cluster import normalized_mutual_info_score
import numpy as np
# Here, we create a stochastic block model with 4 clusters for evaluation
sizes = [150, 150, 150, 150]        
probs = [[0.20, 0.05, 0.02, 0.03], [0.05, 0.30, 0.07, 0.02],[0.02, 0.07, 0.30, 0.05], [0.03, 0.02, 0.05, 0.50]]
G = nx.stochastic_block_model(sizes, probs, seed=0)
adj = nx.adjacency_matrix(G)
n_clusters = 4
node_labels = [G.nodes[n]['block'] for n in np.sort(G.nodes)]
louvain = Louvain()    
clusters = louvain.fit_transform(adj)
# Get the result
nmi = normalized_mutual_info_score(clusters, node_labels)
print("nmi:", nmi)
