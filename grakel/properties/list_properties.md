 # graph properties
 
 RDD: $\frac{1}{2} \sum_{u,v} \frac{deg_G(u) + deg_G(v)}{dist_G(u,v)}$

Wiener index: $W(G) = \frac{1}{2} \sum_{u,v \in V} dist_G(u,v)$ 


 
 # vertex properties
 
 
 # edge properties
 communicability between nodes u and v is
$C(u,v) = \sum_{j=1}^n \phi_j (u) \phi_j(v) e^{\lambda_j}$

where $\phi_{j}(u)$ is the p-th element of the jth orthonormal eigenvector of the adjacency matrix associated with the eigenvalue $\lambda_{j}$.

https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.communicability_alg.communicability.html#networkx.algorithms.communicability_alg.communicability




Links:
rw_grakel_Sept2022.ipynb
