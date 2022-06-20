def centrality(v, sp_mat):
    row = sp_mat[v]
    mn = np.mean(row)
    recip = 1/(mn)
    return recip
