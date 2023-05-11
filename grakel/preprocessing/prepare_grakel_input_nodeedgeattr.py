def prepare_grakel_input(node_attributes_array, edge_attributes_array, num_graphs): # array of vectors
  from grakel import Graph
  grakel_graphs = []
        
  for i in range(num_graphs):
      node_attributes = node_attributes_array[i]
      edge_attributes = edge_attributes_array[i]
      ggraph = Graph(edges, node_labels= node_attributes, edge_labels = edge_attributes)
      grakel_graphs.append(ggraph)

  return grakel_graphs
