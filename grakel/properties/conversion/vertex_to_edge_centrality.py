# aggregate : v -> e property

# flow, centrality of edge?

def vertex_to_edge_centrality(cent_list, edge_mat):
    # for each edge, take the average of the 2 vertices it connects 
    n = len(edge_mat)
    edge_cent = []
    edge_cent_mat = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            # look up centrality of i and j
            ci = cent_list[i]
            cj = cent_list[j]
            av = np.mean(ci, cj)
            edge_cent_mat[i,j] = av
    
    return edge_cent_mat

            
