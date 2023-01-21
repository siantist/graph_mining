In progress:

- bipartite flow matching on kronecker product

To try out:
- use av-2-deg of vertex as property in graph mining
- translate vertex properties into edge properties
- DNA sequences to word representable graphs ( read https://learngenomics.dev/docs/biological-foundations/cells-genomes-dna-chromosomes ) and then graph analysis
- try doing the to do in https://github.com/siantist/graph_mining/blob/main/grakel/subgraph_specific_kernel.py

To Do:
 - tu dataset , test with randomwalk3 or randomwalk4 

- graph kernel score in GNN

- code the algorithm https://arxiv.org/pdf/1904.13169.pdf with graphblas

Notes on grakel:

https://ysig.github.io/GraKeL/0.1a8/documentation/core_concepts.html

fit method extracts kernel dependent features from an input graph collection.

The fit_transform method does the same job as fit, but also computes the kernel matrix emerging from the input graph collection.

The transform method calculates the kernel matrix between a new collection of graphs and the one given as input to fit or to fit_transform.
