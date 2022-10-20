# October 2022
# rw 3 : combine initialize and custom_initialize_parse


from grakel.kernels import Kernel

import networkx as nx

def idem(x):
    return x

# compute vector q:
def compute_q(G):
    # use nx
    q= nx.degree_centrality(G)
    return q

# define the weight, given input vector q (quantity assoc to node i)

def weights(A, q, beta):
    n = len(A)
    w = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            w[i,j] = np.pow(q[i]*q[j], beta)*A[i,j]
    
    return w

def edges_from_adjacency(A):
    
    # add edges
    edges= []
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i,j] == 1:
                edges.append((i,j))
    # take the unique
    
    return edges

def compute_walk(self, X, Y):
    
    walk1 = []
    walk2 = []
    
    # choose starting vertex 
    start1= 0
    start2 = 0
    
    n = len(A1)
    
    wts1 = np.array(weights(A1, q1, beta=2))
    wts2 = np.array(weights(A2, q2, beta=2))
    
    ar = np.arange(n)
    for i in range(k):
        # compute walk1 
        ver1 = A1[start1, :]
        ver2 = A2[start2, :]
        # choose with probability 
        
        # boolean 
        #bool1 = n*[False]
        #bool2 = n*[False]
        bool1 = [i in ver1 for i in ar]
        bool2 = [i in ver2 for i in ar]
        
        p1 = wts1[bool1]
        p2 = wts2[bool2]
        
        # sample with the probability ; idea: multiple walks?
        c1= np.random.choice(ver1 , p = p1)
        c2 = np.random.choice(ver2, p=p2)
        
        # jump to c1 
        walk1.append(c1)
        walk2.append(c2)
        
        start1 = c1
        start2 = c2
    
    return walk1, walk2

class RandomWalk3(Kernel):
    
    def __init__(self, n_jobs=None,
                 normalize=False, verbose=False,
                 lamda=0.1, beta=2, method_type="fast",
                 kernel_type="geometric", p=10):
        """Initialise a random_walk kernel."""
        
        super(RandomWalk3, self).__init__(
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
    
        self._initialized.update({"method_type": False, "kernel_type": False,
                                  "p": False, "lamda": False})
        
    
    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        super(RandomWalk3, self).initialize()
        
        if not self._initialized["method_type"]:
            self._initialized["method_type"] = True
            self.add_input_ = idem
            
        # custom init below:

        # p is the # of steps of the walk -> determine mu_
            
            
            
        
    # parse input returns The extracted adjacency matrices for any given input
    def parse_input(self, X):
        
        i = 0
        out = list()
        print("X is", X)
        
        # set the networkx graph and other parameters
        g1 = nx.Graph()
        
        for (idx, x) in enumerate(iter(X)):

            A = x.get_adjacency_matrix()
            
            # test this by printing
            print("parse input A is:", A)

            is_iter = isinstance(x, collections.Iterable)
            
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
            
            if is_iter:
                x = list(x)
            else:
                #A = Graph(x[0], {}, {}, self._graph_format).get_adjacency_matrix()
                pass

            i += 1
            out.append(self.add_input_(A))
        
        
        
        
        
        return out
    
    
    def pairwise_operation(self, X, Y):
        
        XY = np.kron(X, Y)
    
        # p = number of steps 
        if self.p:
            #S= pow(np.kron(w1.T, w2.T), ell)
            S= pow(np.kron(X, Y), self.p)
            
        print("p is ", self.p)
        
        print("X is ", X)
        print("Y is " , Y)
        
        S= pow(np.kron(X, Y), self.p)
        
        
        
        # if doing random walk manually
        if self.kernel_type == 'manual':
            walk1, walk2 = compute_walk(self, X, Y)
            
            # score the walks 
            

        return np.sum(S)
