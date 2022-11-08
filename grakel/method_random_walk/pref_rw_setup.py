# compute vector q:
def compute_q(G):
    # use nx
    q= nx.degree_centrality(G)
    
    # use custom function here : 
    
    return q

# define the weight, given input vector q (quantity assoc to node i)

def weights(A, q, beta):
    n = len(A)
    w = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            w[i,j] = np.pow(q[i]*q[j], beta)*A[i,j]
    
    return w

 # take the kronecker product of the weight matrices


np.kron(w1, w2)
