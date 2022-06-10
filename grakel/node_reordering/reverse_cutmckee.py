# node reordering
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
            A = sort_adjacency_by_degrees(adjacency[Q])
            for b in A
                if b not in R:
                    R.append(b)
                end
            end
        else
            t = sort_adjacency_by_degrees(adjacency[R[i]])
            for T in t:
                if T not in R:
                    R.append(T)
                end
            end
        end
    end
    new_order = reverse(R)
    return new_order
end
