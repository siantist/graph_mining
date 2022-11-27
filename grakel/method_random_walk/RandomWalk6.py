# from randomwalk5 : fix the normalization problem (?)

class RandomWalk6(Kernel):
    """The random walk kernel class.
    p : int or None
        If initialised defines the number of steps.
    Attributes
    ----------
    mu_ : list
        List of coefficients concerning a finite sum, in case p is not None.
    """

    _graph_format = "adjacency"

    def __init__(self, n_jobs=None, beta=2,
                 normalize=True, verbose=False,
                 lamda=0.1, method_type="fast",
                 kernel_type="baseline", p=None):
        """Initialise a random_walk kernel."""
        # setup valid parameters and initialise from parent
        
        super(RandomWalk6, self).__init__(
            n_jobs=n_jobs, normalize=normalize, verbose=verbose)

        # Setup method type and define operation.
        self.method_type = method_type
        self.kernel_type = kernel_type
        self.p = p
        self.lamda = lamda
        
        # my args
        self.beta = beta
        # save network x version of the graph
        self.networkx_graph = nx.Graph()
        self.numnodes = 0
        self.edge_list =[]
        self.weight_mat = []
        
        print("init")
        self._initialized.update({"method_type": False, "kernel_type": False,
                                  "p": False, "lamda": False})

    def initialize(self):
        """Initialize all transformer arguments, needing initialization."""
        super(RandomWalk6, self).initialize()

        if not self._initialized["method_type"]:
            # Setup method type and define operation.
            if (self.method_type == "baseline" or
                    (self.method_type == "fast"
                     and self.p is None
                     and self.kernel_type == "geometric")):
                self.add_input_ = idem
            """
            elif self.method_type == "fast":
                # Spectral Decomposition if adjacency matrix is symmetric
                self.add_input_ = sd
            else:
                raise ValueError('unsupported method_type')
            self._initialized["method_type"] = True

        if not self._initialized["kernel_type"]:
            if self.kernel_type not in ["geometric", "exponential"]:
                raise ValueError('unsupported kernel type: either "geometric" '
                                 'or "exponential"')
        """
        # initialize 
        g1 = nx.Graph()
        n = len(A)
        nodes= np.arange(n)
        g1.add_nodes_from(nodes)
        edge_list = edges_from_adjacency(A)
        g1.add_edges_from(edge_list)
        q = compute_q(g1)
        weight_mat = weights(A, q, self.beta)
        # save self 
        self.networkx_graph = g1
        self.numnodes=n
        self.edge_list = edge_list
        self.weight_mat = weight_mat


    def parse_input(self, X):
        """Parse and create features for random_walk kernel.
        Parameters
        ----------
        X : iterable
            For the input to pass the test, we must have:
            Each element must be an iterable with at most three features and at
            least one. The first that is obligatory is a valid graph structure
            (adjacency matrix or edge_dictionary) while the second is
            node_labels and the third edge_labels (that correspond to the given
            graph format). A valid input also consists of graph type objects.
        Returns
        -------
        out : list
            The extracted adjacency matrices for any given input.
        """
        
        print("parse input")
        g1 = nx.Graph()
        
        if not isinstance(X, Iterable):
            raise TypeError('input must be an iterable\n')
        else:
            i = 0
            out = list()
            for (idx, x) in enumerate(iter(X)):
                is_iter = isinstance(x, Iterable)
                if is_iter:
                    x = list(x)
                if is_iter and len(x) in [0, 1, 2, 3]:
                    if len(x) == 0:
                        warnings.warn('Ignoring empty element' +
                                      ' on index: '+str(idx))
                        continue
                    else:
                        A = Graph(x[0], {}, {},
                                  self._graph_format).get_adjacency_matrix()
                        n = len(A)
                        nodes= np.arange(n)
                        g1.add_nodes_from(nodes)
                        edge_list = edges_from_adjacency(A)
                        g1.add_edges_from(edge_list)
                        q = compute_q(g1)
                        weight_mat = weights(A, q, self.beta)
                        

                elif type(x) is Graph:
                    A = x.get_adjacency_matrix()
                    n = len(A)
                    nodes= np.arange(n)
                    g1.add_nodes_from(nodes)
                    edge_list = edges_from_adjacency(A)
                    g1.add_edges_from(edge_list)
                    q = compute_q(g1)
                    weight_mat = weights(A, q, self.beta)
                    
                else:
                    raise TypeError('each element of X must be either a ' +
                                    'graph or an iterable with at least 1 ' +
                                    'and at most 3 elements\n')
                i += 1
                out.append(weight_mat) #(self.add_input_(weight_mat))

            if i == 0:
                raise ValueError('parsed input is empty')

            return out

    def pairwise_operation(self, X, Y):
        """Calculate the random walk kernel.
        Fast:
        Spectral demoposition algorithm as presented in
        :cite:`vishwanathan2006fast` p.13, s.4.4, with
        complexity of :math:`O((|E|+|V|)|E||V|^2)` for graphs witout labels.
        Baseline:
        Algorithm presented in :cite:`kashima2003marginalized`,
        :cite:`gartner2003graph` with complexity of :math:`O(|V|^6)`
        Parameters
        ----------
        X, Y : Objects
            Objects as produced from parse_input.
        Returns
        -------
        kernel : number
            The kernel value.
        """
        print("pairwise operation")
        if self.method_type == "baseline":
            # calculate the product graph
            XY = np.kron(X, Y)

            # algorithm presented in
            # [Kashima et al., 2003; Gartner et al., 2003]
            # complexity of O(|V|^6)

            # XY is a square matrix
            s = XY.shape[0]

            if self.p is not None:
                P = np.eye(XY.shape[0])
                S = self.mu_[0] * P
                for k in self.mu_[1:]:
                    P = np.matmul(P, XY)
                    S += k*P
            else:
                if self.kernel_type == "geometric":
                    S = inv(np.identity(s) - self.lamda*XY).T
                elif self.kernel_type == "exponential":
                    S = expm(self.lamda*XY).T

            return np.sum(S)
