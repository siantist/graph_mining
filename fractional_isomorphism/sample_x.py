# sample X for AX = XB to find min || AX - XB ||
#n is size of matrix 
#k = n/2
perm_mats = {}
diffs = {}
for k in range(n/2): # k is # of 1's in X 
  # quantum search for permutation matrix ? 
  # random permutation matrix generation 
  perm_mat = []
  for j in range(k):
    coord1 = randint(0, n)
    coord2 = randint(0,n) 
    # set matrix 
    perm_mat[coord1, coord2] = 1
  
  # calc dist 
  diff = np.abs( np.matmul(A, perm_mat) - np.matmul(perm_mat, B))
  perm_mats[k] = perm_mat
  diffs[k] = diff

return perm_mats, diffs
