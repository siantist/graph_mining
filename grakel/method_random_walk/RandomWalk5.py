# edit RandomWalk3 -> other properties of nodes such as 2-av-degree

# try: replace kronecker product with (common nbd ) product

# arxiv.org/pdf/1901.05609.pdf
from numpy.linalg import inv

from grakel.kernels import Kernel
from grakel.graph import Graph

class RandomWalk5(Kernel):
    
    def __init__(self, n_jobs=None,
                 normalize=True, verbose=False,
                 lamda=0.1, beta=2, method_type="fast",
                 kernel_type="geometric", p=10):
        """Initialise a random_walk kernel."""
        
        super(RandomWalk5, self).__init__(
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
        
        self.weight_vec = []
        
        print("init")
    
        self._initialized.update({"method_type": False, "kernel_type": False,
                                  "p": False, "lamda": False})
        
    
    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        super(RandomWalk5, self).initialize()
        
        if not self._initialized["method_type"]:
            self._initialized["method_type"] = True
            self.add_input_ = idem
            
        # custom init below:

        # p is the # of steps of the walk -> determine mu_
            
            
            
        
    # parse input returns The extracted adjacency matrices for any given input
    def parse_input(self, X):
        
        i = 0
        out = list()
        #print("X is", X)
        
        # set the networkx graph and other parameters
        g1 = nx.Graph()
        
        
        """if len(X) == 1:
            X = X[0]
            
            print("len X is 1")
            print("X is ", X)
            A = X.get_adjacency_matrix()"""
        is_iter = isinstance(X, Iterable)
        
        
        print("is iter :", is_iter)
        
        if not is_iter:
            A = X.get_adjacency_matrix()
            n = len(A)

            nodes= np.arange(n)
            g1.add_nodes_from(nodes)

            edge_list = edges_from_adjacency(A)
            self.edge_list = edge_list

            g1.add_edges_from(edge_list) # [(2,3),(1,3), (3,4), (3,5)])

            q = compute_q(g1) # from nx

            self.weight_vec = weights(A, q, self.beta)

            self.networkx_graph = g1
            self.numnodes = n
            
            
        if is_iter:
            for (idx, x) in enumerate(iter(X)): # only parse 0-th element (others are labels)

                #print(x)

                x_is_iter = isinstance(x, Iterable)
                
                if x_is_iter:
                    x = list(x)
                    A = grakel.Graph(x[0], {}, {}).get_adjacency_matrix()

                #gx = grakel.Graph(x)
                #A = gx.get_adjacency_matrix()

                # test this by printing
                #print("parse input A is:", A) Note: PRinted this Before!


                A = x.get_adjacency_matrix()
                # custom init
                n = len(A)

                nodes= np.arange(n)
                g1.add_nodes_from(nodes)

                edge_list = edges_from_adjacency(A)
                self.edge_list = edge_list

                g1.add_edges_from(edge_list) # [(2,3),(1,3), (3,4), (3,5)])

                q = compute_q(g1) # from nx

                self.weight_vec = weights(A, q, self.beta)

                self.networkx_graph = g1
                self.numnodes = n

                # end custom init

                """if is_iter:
                    x = list(x)
                else:
                    #A = Graph(x[0], {}, {}, self._graph_format).get_adjacency_matrix()
                    pass"""

                i += 1
                out.append(self.add_input_(A))
        
        
        
        
        
        return out
    
    
    def pairwise_operation(self, X, Y):
        
        print("pairwise op rw5")
        
        XY = np.kron(X, Y)
    
        # p = number of steps 
        if self.p:
            #S= pow(np.kron(w1.T, w2.T), ell)
            S= pow(np.kron(X, Y), self.p)
            
        #print("p is ", self.p)
        
        #print("X is ", X)
        #print("Y is " , Y)
        
        S= pow(np.kron(X, Y), self.p)
        s = XY.shape[0]
        
        
        # if doing random walk manually
        if self.kernel_type == 'manual':
            walk1, walk2 = compute_walk(self, X, Y)
            
            # score the walks 
        if self.kernel_type == "geometric":
            S = inv(np.identity(s) - self.lamda*XY).T
            
        print("S sum is", np.sum(S))
        return np.sum(S)
