# pseudo inverse of system matrix (sec 4.1)


def pos_det(A):
    
def neg_det(A):
    
def det_eps(A, eps):
    return pos_det(A) + eps*neg_det(A)

def submat(A, i, j):
    Ai = np.delete(A, (i), axis=0)
    Aij = np.delete(Ai, (j), axis=1)
    return Aij

def adj_eps(A, eps): # eps-adjoint matrix
    # (n-1)(n-1) submatrix of A remove i-th row and j-th column 
    A_n1 = submat(A, i, j)
    eps_ij = np.pow(eps, i+j)
    prod= eps_ij*A_n1
    return np.transpose(prod)

def pseudo_inv(A, eps):
    A_deteps = det_eps(A, eps)
    A_deteps_inv = np.inv(A_deteps)
    return np.matmul(A_deteps_inv, adj_eps(A, eps))
    
# solution is A^- * b where A^- is pseudoinverse
