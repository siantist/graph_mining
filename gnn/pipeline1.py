from torch_geometric.nn import GAT
gat = GAT(input_sample_size, hidden_sample_size, num_message_passing_layers, output_size)

node_embedding = gat.forward()

# convert to grakel graph with node attributes
def prepare_grakel_input(edges, g): # node_embedding
        from grakel import Graph
        grakel_graphs = []
        node_attributes = {}
        edge_attributes = {}

        num_edges = len(edges)


        for i in range(num_graphs):

            node_embedding = gat.forward(g[i])
            num_nodes = len(g[i])

            node_attributes[i] = node_embedding[i]
            node_embedding_len = len(node_embedding)

            rel_action_len = len(self.relevant_actions)
            for i in range(rel_action_len):
                ilist = list(np.arange(rel_action_len))
                ilist.remove(i)
                edges[i] = ilist

            for i in range(num_nodes):
                for j in range(num_nodes):
                    # set edge attr
                    edge_attributes[(i,j)] = edges[i,j] # ?
            # G = Graph(edges, node_labels=node_attributes, edge_labels=edge_labels)
            ggraph = Graph(edges, node_labels= node_attributes, edge_labels = edge_attributes)
            grakel_graphs.append(ggraph)

        return grakel_graphs
