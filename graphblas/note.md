ideas
subsemimodule of cycle bases (pg 3 of "On the maximal solution of a linear system over tropical semirings")



lin_syst_trop_semiring_solution.py: 

AX = b over tropical semiring solution code

The positive determinant of matrix A is $|A|^+$ and is defined by $|A|^+ = \sum_{ \sigma \in \mathcal{A}_n} \Pi_{i=1}^n a_{i \sigma(i)}$ and $|A|^- = \sum_{\sigma \mathcal{S}_n \setminus \mathcal{A}_n} \Pi_{i=1}^n a_{i \sigma(i)}$. 

The $\epsilon$-determinant of $A$ can be rewritten as $det_{\epsilon}(A) = |A|^+ + \epsilon( |A|^-)$. 

Def. The $\epsilon$-determinant of $A$ is $det_{\epsilon}(A) = \sum_{\sigma \in S_n} \epsilon^{\tau(\sigma)}( a_{1 \sigma(1)} \cdots a_{ n \sigma(n)})$ which is also equal to $|A|^+ + \epsilon(|A|^-)$ 

Thm 4:solution $X* = (A^- b) = (d^{-1} d_1, d^{-1} d_2, \cdots, d^{-1} d_n)^T$ 
where $d = det_{eps}(A)$ and $d_j = det_{eps}(A_{[j]}), j \in [n]$. 

links:
https://github.com/Graphegon/pygraphblas

https://github.com/python-graphblas/graphblas-algorithms/blob/main/graphblas_algorithms/algorithms/shortest_paths/generic.py

https://github.com/python-graphblas
https://github.com/python-graphblas/python-graphblas
