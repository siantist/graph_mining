# columnwise then rowwise (face-splitting) Khatri Rao product

def column_row_mult(A,B):
  col = linalg.khatri_rao(A, B)
  row = linalg.khatri_rao(np.transpose(A), np.transpose(B))
  return np.matmul(col, row)
