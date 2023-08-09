def prepare_grakel_input_edges(node_attributes, edge_attributes_array, a):
  ggraph = Graph(initialization_object=a, node_labels= node_attributes, edge_labels= edge_attributes)
  return ggraph
