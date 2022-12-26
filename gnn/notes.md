in fit_graph_to_vector_data.py:

Their question: given collection of vectors, 'what is the right graph to fit to this set of vectors'?

https://www.cs.yale.edu/homes/spielman/PAPERS/icml_final.pdf Loss function,
$f(w) = \sum_i ||d_i x_i - \sum_j w_{ij} x_j ||^2$

or $f(w) = || LX||_F^2$ where $L$ is the graph laplacian. 

Idea: change laplacian with other kinds of Laplacians 

pg. 4:
They solve for the vector that minimizes 
$x^T L x = \sum_{(i,j) \in E} w_{ij}(x_i - x_j)^2$
