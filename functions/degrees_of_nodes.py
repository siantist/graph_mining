# input : adj matrix
def degrees_of_nodes(A):
  degs =[]
  for row in A:
    d = sum(row)
    degs.append(d)
  return degs
