# 2-av-row-sum normalized random walk 

def generate_2avrowsum_rw(s):
    arr = np.zeros((s,s))
    
    
# make a different kronecker product based on properties

# try the shortest path matrix first 

def kron_prod_prop(X, Y, xprop, yprop):
    # first populate X and Y with the edge weight values , take np kron, then filter out values based on cap
    z = np.kron(X,Y)
    n = len(z)
    for i in range(n):
        for j in range(n):
            # check prop 
            xp = xprop[i]
            yp = yprop[j]
    return
