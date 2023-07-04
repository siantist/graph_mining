# from On the maximal solution of a linear system over tropical semirings
# pos determinant

# input: set of permutations, matrix A
# tropical determinant 
def pos_determinant(A, permutations):
    tot_sum = 0
    for p in permutations:
      tot_prod = 1
      for ind in range(len(A)):
        pi = permutations[ind]
        aij = A[ind, pi]
        #mult 
        tot_prod = tot_prod*aij 
      tot_sum = tot_sum + tot_prod
    
    return tot_sum
