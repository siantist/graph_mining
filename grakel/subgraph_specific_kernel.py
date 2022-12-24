
# To do: try determining subgraphs based on topology ?

import collections
import warnings

import numpy as np

from numbers import Real

from grakel.kernels import Kernel
from grakel.graph import Graph
from grakel.kernels._c_functions import sm_kernel # https://github.com/ysig/GraKeL/blob/master/grakel/kernels/_c_functions/functions.pyx

# Define default vertex, edge and lambda weight functions
def _dirac(a, b):
    """Calculate the dirac function for labels."""
    return int(a == b)


class SpecificSubgraphMatching(Kernel):
    
    def __init__(self, n_jobs=None, verbose=False,
                 normalize=False, k=5, kv=_dirac,
                 ke=_dirac, lw="uniform"):
        """Initialise a `subgraph_matching` kernel."""
        super(SubgraphMatching, self).__init__(
            n_jobs=n_jobs, verbose=verbose, normalize=normalize)

        self.k = k
        self.kv = kv
        self.ke = ke
        self.lw = lw
        self._initialized.update({"k": False, "kv": False, "ke": False, "lw": False})

    def pairwise_operation(self, x, y):
        """Calculate the `subgraph_matching` kernel.
        See :cite:`kriege2012subgraph`.
        Parameters
        ----------
        x, y : tuples
            *Vertex-set*, *edge-dictionary*, *node-label-dictionary*,
            *edge-labels-dictionary* tuple.
        Returns
        -------
        kernel : number
            The kernel value.
        """
        tv = sm_kernel(x, y, self.kv, self.ke, self.k)
        return np.dot(self.lambdas_, tv)
    
    def parse_input(self, X):
        """Parse and create features for the `subgraph_matching` kernel.
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
        if not isinstance(X, collections.Iterable):
            raise TypeError('input must be an iterable\n')
        else:
            i = 0
            out = list()
            for (idx, x) in enumerate(iter(X)):
                is_iter = False
                if isinstance(x, collections.Iterable):
                    is_iter = True
                    x = list(x)

                if type(x) is Graph:
                    g = Graph(x.get_adjacency_matrix(),
                              x.get_labels(purpose="adjacency"),
                              x.get_labels(purpose="adjacency",
                                           label_type="edge"),
                              self._graph_format)
                elif is_iter and len(x) in [0, 3]:
                    x = list(x)
                    if len(x) == 0:
                        warnings.warn('Ignoring empty element' +
                                      ' on index: '+str(idx))
                        continue
                    elif len(x) == 3:
                        g = Graph(x[0], x[1], x[2], "adjacency")
                        g.change_format(self._graph_format)
                else:
                    raise TypeError('each element of X must be either a ' +
                                    'graph object or a list with at least ' +
                                    'a graph like object and node, ' +
                                    'edge labels dict \n')
                n = g.nv()
                E = g.get_edge_dictionary()
                L = g.get_labels(purpose="dictionary", return_none=(self.kv is None))
                Le = g.get_labels(purpose="dictionary", label_type="edge",
                                  return_none=(self.ke is None))
                Er = set((a, b) for a in E.keys()
                         for b in E[a].keys() if a != b)

                i += 1
                out.append((n, Er, L, Le))

            if i == 0:
                raise ValueError('parsed input is empty')
            return out
