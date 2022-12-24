# wiener index
def wiener_index(G, shortest_path_matrix):
  s= 0
  for i in range(n):
    for j in range(n):
      if i != j:
        s =s + shortest_path_matrix[i,j]
  
  return 0.5*s
