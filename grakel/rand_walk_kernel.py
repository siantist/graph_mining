import collections
import warnings

import numpy as np

from itertools import product

from numpy import ComplexWarning
from numpy.linalg import inv
from numpy.linalg import eig
from numpy.linalg import multi_dot
from scipy.linalg import expm
from scipy.sparse.linalg import cg
from scipy.sparse.linalg import LinearOperator

from grakel.kernels import Kernel
from grakel.graph import Graph

def preferential_navigation_stationary_i(A, q, beta,i):
    n = len(A)
    new_adj_mat = np.zeros((n,n))
    x_ind = 0
    numerator = 0
    for ell in range(n):
        numerator = numerator+ np.pow(q[i]*q[ell], beta)*A[i,ell]
    denominator =0 
    for ell in range(n):
        for m in range(n):
            denominator= denominator+ np.pow(q[ell]*q[m], beta)*A[ell, m]
    return (numerator)/(denominator)

class RandomWalkPreferential(Kernel):
    def __init__(self, n_jobs=None,
                 normalize=False, verbose=False,
                 lamda=0.1, method_type="fast",
                 kernel_type="geometric", p=None):
        super(RandomWalkPreferential, self).__init__(
            n_jobs=n_jobs, normalize=normalize, verbose=verbose)
        self.method_type = method_type
        self.kernel_type = kernel_type
        self.p = p
        self.lamda = lamda
    
    def parse_input(self,X):
        if not isinstance(X, collections.Iterable):
            raise TypeError('input must be an iterable\n')
        else:
            i = 0
            out = list()
            for (idx, x) in enumerate(iter(X)):
                is_iter = isinstance(x, collections.Iterable)
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
                elif type(x) is Graph:
                    A = x.get_adjacency_matrix()
                else:
                    raise TypeError('each element of X must be either a ' +
                                    'graph or an iterable with at least 1 ' +
                                    'and at most 3 elements\n')
                i += 1
                out.append(self.add_input_(A))

            if i == 0:
                raise ValueError('parsed input is empty')

            return out

    def pairwise_operation(self, X, Y):
        if self.method_type == "baseline":
            # calculate the product graph
            XY = np.kron(X, Y)
            
            # set trans matrix S (p is int)  
            S = preferential_navigation_stationary_i(XY, q, beta,i)
            
            if self.kernel_type == "geometric":
                # Baseline Algorithm as presented in
                # [Vishwanathan et al., 2006]
                Id = np.identity(s)
                S = inv(Id - self.lamda*XY).T
            if self.kernel_type == 'preferential':
                # k(G,G') = q_X^T ( I - T_X)^{-1} p_X
                
                # T_X = vec(P) vec(P')^T * ( phi(X) x phi(X') ) 
                