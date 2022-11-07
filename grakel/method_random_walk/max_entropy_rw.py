# max entropy rw's
# trans prob defined in terms of components of eig centrality of node i 
# e_i is i-th component of normalized eigenvector corresponding to max eigenval of A

def max_entropy_rw(A, e, chi):
    n = len(A)
    w = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            w[i,j] = (e[j]/(chi*e[i]))*A[i,j]
    
    return w
