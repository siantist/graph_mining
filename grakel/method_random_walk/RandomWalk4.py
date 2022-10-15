# sept 13, 22 : define newer kernel 

def idem(x):
    return x

def edges_from_adjacency(A):
    
    # add edges
    edges= []
    
    return edges

class RandomWalk4(Kernel):
    
    def __init__(self, n_jobs=None,
                 normalize=True, verbose=False,
                 lamda=0.1, beta=2, method_type="fast",
                 kernel_type="geometric", p=10):
        """Initialise a random_walk kernel."""
        
        super(RandomWalk2, self).__init__(
            n_jobs=n_jobs, normalize=normalize, verbose=verbose)

        # Setup method type and define operation.
        self.method_type = method_type
        self.kernel_type = kernel_type
        self.p = p
        self.lamda = lamda
        
        self.beta = beta
        
        # save network x version of the graph
        self.networkx_graph = nx.Graph()
        
        self.numnodes = 0
        
        self.edge_list =[]
        
        self.weight_vec = [] # 
    
        self._initialized.update({"method_type": False, "kernel_type": False,
                                  "p": False, "lamda": False})

    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        super(RandomWalk2, self).initialize()
        
        if not self._initialized["method_type"]:
            self._initialized["method_type"] = True
            self.add_input_ = idem
        
        # p is the # of steps of the walk -> determine mu_

        g1 = nx.Graph()
        
        
        
        for (idx, x) in enumerate(iter(X)):

            A = x.get_adjacency_matrix()
            n = len(A)
            
            self.edge_list = edges_from_adjacency(A)
            
            nodes= np.arange(n)
            g1.add_nodes_from(nodes)

            g1.add_edges_from(self.edge_list) # [(2,3),(1,3), (3,4), (3,5)])
            
            self.networkx_graph = g1 
            
            q = compute_q(g1) # from nx
            
            self.weight_vec = weights(A, q, self.beta)
    
    # parse input returns The extracted adjacency matrices for any given input
    def parse_input(self, X):
        print("parse input")
        i = 0
        out = list()
        print("X is", X)
        for (idx, x) in enumerate(iter(X)):

            A = x.get_adjacency_matrix()
            
            print("idx is:", idx, "For A:", A)

            is_iter = isinstance(x, collections.Iterable)
            if is_iter:
                x = list(x)
            else:
                #A = Graph(x[0], {}, {}, self._graph_format).get_adjacency_matrix()
                pass

            i += 1
            out.append(self.add_input_(A))
        return out
        
        
    # replace pairwise operation with this
    def pairwise_operation(self, X, Y):
        #XY = np.kron(X,Y)
        
        # take the weight matrix 
        W1 = weights(X, self.q1, self.beta)
        W2 = weights(Y, self.q2, self.beta)
        
        W_XY = np.kron(W1, W2)
        
        # starting probabilities
        start_prob = np.kron(start1, start2)
        # stopping prob
        stop_prob  = np.kron(stop1, stop2)
        
        # (q_1 \otimes q_2) ( I - c W)^{-1} (p_1 \otimes p_2) 
        s= W_XY.shape[0]
        
        S = inv(np.identity(s) - self.lambda*W_XY).T
        
        return np.sum(S)
            
            
