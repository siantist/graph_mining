# program the common nbd product 

def common_nbd_product(A, B, v_labels1, v_labels2):
    
    # vertices V(A) x V(B)
    n = len(A)
    
    vertices1x2 = {}
    inverse_vertices1x2= {}
    ind=0
    
    v1 = 0
    for lab1 in v_labels1:
        v2 = 0
        for lab2 in v_labels2:
            
            if lab1 == lab2:
                
                pair = (v1, v2)

                vertices1x2[ind] = pair
                inverse_vertices1x2[pair] = ind
            ind= ind+1
            v2 +=1
        v1+=1
    
    # make vertices as pairs of all v(A) x v(B)
    n1 = len(A)
    n2 = len(B)
    
    v3 = []
    
    list1 = np.range(n1)
    list2 = np.range(n2)
    # generate all unique pairs 
    for i in itertools.product(list1, list2):
        
        print(i)
        v3.append(i)
        
    
    for ver1 in v3:
        
        for ver2 in v3:
        
            a1 = ver1[0]
            a2 = ver1[1]
            
            b1 = ver2[0]
            b2 = ver2[1]
            # check the edges here
            e1 = np.nonzero(A[a1]) #np.where(A[i1] != 0 )

            e2 = np.nonzero(B[a2]) #np.where(A[i2] != 0)
            # add the id's where there exists an edge in A 
            
            e3 = np.nonzero(A[b1])
            e4 = np.nonzero(B[b2])

            # two vertices (a,b) and (c,d) are adjacent if:
            # (a,c) in E(G) and (b,h), (d,h) in E(H)
            # or (b,d) in E(H) and (a,g), (c,g) in E(G)

            a = a1
            c = b1
            b = a2
            d = b2
            # if a,c in E(G)
            
        
        
        
        
    
  
