For preferential random walk:
beta > 0 means tendency to hop to nbrs with large values of q , beta< 0 hops to nodes with lower values of q
beta =0 means normal random walk 

transition matrix of pref rw is $pi_{i -> j}$ and weights is $\Omega_{ij}$

*Examine the weights of the edges within the kronecker product of the graphs.

*grakel Documentation:*

The normalized kernel value between 2 graphs is $k (G_1, G_2) / \sqrt{ k(G_1, G_1) k (G_2, G_2)}$ 

The normalize function is in https://github.com/ysig/GraKeL/blob/master/grakel/kernels/kernel.py

The fit method extracts kernel dependent features from an input graph collection.

The fit_transform method does the same job as fit, but also computes the kernel matrix emerging from the input graph collection.

The transform method calculates the kernel matrix between a new collection of graphs and the one given as input to fit or to fit_transform.
It calls the parse input on Y and then calls the calculate_kernel_matrix which calls the pairwise operation function. Parse input is just parsing the input data.

The diagonal method is used for normalizing kernel matrices. It returns the self-kernel values of all the graphs given as input to fit along with those given as input to transform, provided that this method has been called.

The pairwise_operation method computes the kernel between two graphs. This method is used by the calculate_kernel_matrix method which generates kernel matrices from collections of graphs. pairwise operation calls parse input.

https://ysig.github.io/GraKeL/0.1a8/documentation/core_concepts.html

https://github.com/ysig/GraKeL/blob/master/grakel/graph_kernels.py. (has transform, fit transform, fit functions)

https://github.com/ysig/GraKeL/blob/master/grakel/utils.py
