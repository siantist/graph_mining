# load the dataset 
g_db2 = tud_to_networkx("ENZYMES")

graphs =[]
classes = []
adj_mats = {}

grakel_graphs = {}
grakel_array = []

grakel_array2 = []

# edge lists
edgelists = {}

i=0
for g in g_db2:
    # convert to adj mat or other graph object
    A = nx.to_numpy_matrix(g)
    # make the edge list from it? 
    elist = edge_dictionary(g)
    edgelists[i] = elist
    G = Graph(elist)
    
    grakel_graphs[i] = G
    grakel_array.append(G)
    
    adj_mats[i] = A
    
    c = g.graph['classes']
    classes.append(c)
    
    node_lab = g.n_labels #g_db2[0].nodes[1]['labels']
    # make the grakel graph 
    G2 = Graph(elist, node_lab)
    
    grakel_array2.append(G2)
    
    i+=1
    
