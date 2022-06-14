# node reordering

def sort_adjacency_i(alist, degrees): # degrees is dictionary
    degs = []
    
    for v in alist:
        vdeg = degrees[v]
        degs.append(vdeg)
        
    sted_degs = degs.argsort()
    
    sted_list = alist[sted_degs]
    
    return sted_list


# adjacency is dictionary: int -> vector(int)
# degrees is dict: int -> int
#p, q are int's

def RCM(adjacency, degrees, P, Q):
    n = len(adjacency)
    R = []
    #step 1 
    for i in range(1, n):
        if i > len(R):
            R.append(Q) 
            #push!(R, Q)
            A = sort_adjacency_i(adjacency[Q])
            for b in A:
                if b not in R:
                    R.append(b)
                
        else:
            t = sort_adjacency_i(adjacency[R[i]])
            for T in t:
                if T not in R:
                    R.append(T)

    new_order = reverse(R)
    return new_order
