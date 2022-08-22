# define the class here

from grakel.kernels import Kernel

def idem(x):
    return x

class RandomWalk2(Kernel):
    
    def __init__(self, n_jobs=None,
                 normalize=False, verbose=False,
                 lamda=0.1, method_type="fast",
                 kernel_type="geometric", p=10):
        """Initialise a random_walk kernel."""
        
        super(RandomWalk2, self).__init__(
            n_jobs=n_jobs, normalize=normalize, verbose=verbose)

        # Setup method type and define operation.
        self.method_type = method_type
        self.kernel_type = kernel_type
        self.p = p
        self.lamda = lamda
        
        self._initialized.update({"method_type": False, "kernel_type": False,
                                  "p": False, "lamda": False})
        
    
    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        super(RandomWalk2, self).initialize()
        
        if not self._initialized["method_type"]:
            self._initialized["method_type"] = True
            self.add_input_ = idem
            
            
        
        # p is the # of steps of the walk -> determine mu_
        
        
    # parse input returns The extracted adjacency matrices for any given input
    def parse_input(self, X):
        
        i = 0
        out = list()
        print("X is", X)
        for (idx, x) in enumerate(iter(X)):

            A = x.get_adjacency_matrix()

            is_iter = isinstance(x, collections.Iterable)
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

        return np.sum(S)
    
    
        
