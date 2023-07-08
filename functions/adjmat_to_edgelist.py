def adjmat_to_edgelist(A):
  elist = []
  ind1 = 0
  for row in A:
    # add to
    # check permutation exists
    ind2 =0
    for el in row:
      pair1 = (ind1, ind2)
      pair2 = (ind2, ind1)
      if pair1 not in elist:
        if pair2 not in elist:
          # do not append duplicates ?
          if ind1 != ind2:
            elist.append(pair1)
      ind2 = ind2 + 1
    ind1 = ind1+1

  return elist
