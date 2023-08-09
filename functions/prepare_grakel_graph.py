def prepare_grakel_graph(node_attributes, a): # add edge attributes?
  from grakel import Graph
  ggraph = Graph(initialization_object=a, node_labels= node_attributes)
  return ggraph
