# First find X using node labels and first order neighbor labels



# Find X , S, T with graphon limits



def tree_distance(G, S, T, X):

     term1= 1/(len(G) len(H))

    Term2= cut_distance(H, G)

   return term1*term2



def cut_distance(H,G):

    Cd= cut_norm( len(H)*np.matmul(H, X) - len(G)*np.matmul(X,G)) 



def cut_norm(A, S,T):

    s=0

    for I in S:

        for j in T:

            s=s+ A[i,j]

    Return np.abs(s) 
