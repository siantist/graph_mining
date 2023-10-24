def rowwise_threshold(mat, num_thresholds):
  lislist =[]
  for row in mat:
    part = np.sum(row)/(num_thresholds)
    thresholds = part*[*range(num_thresholds)]
    lis= []
    for j in range(num_thresholds):
      # place each item in threshold
      #nw = np.where(row>thresholds)
      nw = np.where(row > j*part) and np.where(row <= (j+1)*part)
      lis.append(nw)
    lislist.append(lis)
  
  return lislist
