def average_two_degree(A,i, deg): # deg holds the degrees of vertices 
  # sum over edges conn to i
  irow = A[i]
  num = 0
  j = 0
  for el in irow:
    if el != 0:
      num = num + deg[j]
    j = j+1
  
  den = deg[i]
  return num/den

# version from tu dataset to nx graph
def average_two_degree(A,i, deg): # deg holds the degrees of vertices 
  # sum over edges conn to i
    irow = A[i]
    # nx graph format 
    irow = np.array(irow).flatten()
    num = 0
    j = 0
    for el in irow:
        if el != 0:
            num = num + deg[j]
        j = j+1

    den = deg[i]
    return (num)/(den)
  
# average 2 transmission of vertex v_i and the signless Laplacian average 2-transmission 

# D(G) = (d_{ij}) where d_ij is distance btwn i and j (# edges of shortest path btwn them)
# D_i : transmission of v_i is sum of dist's btwn v_i and other vertices in G 
def two_transmission(i, D, d): # ask the authors what is diff of d and D ?
  # D is a distance based matrix
  di = d[i]
  num = 0
  n = len(D)
  for j in range(n):
    num =num+ di[j]*D[j]
  den = D[i]
  return num/den
