# tu dataset 
# call on each nx graph object

def edge_dictionary(g):
    
    es =np.array(g.edges)
    d = {}
    n = len(es)

    for i in range(n):
        pair = np.array(g.edges)[i]
        #print(pair)

        p0 = pair[0]
        p1 = pair[1]
        #print(p0)

        if d.get(p0) != None:
            current = d[p0]
            current.append(p1)
            d[p0] = current
        else:
            d[p0] = [p1]
    return d
