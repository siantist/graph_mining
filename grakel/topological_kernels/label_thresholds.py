# graph kernel on topological invariants

# (1) label based:  create label based on threshold ( A = 0 to 10, B = 10 to 20, etc)
def label_threshold(A):
  # find the average / std deviation / normalize between 0 and 1
  av_list = average_calc(A)
  std_list = std_calc(A)
  norm_list = norm_calc(A)

# row-wise threshold 
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

# whole matrix threshold
def place_threshold(mat, num_thresholds, thres):
  part = np.linalg.norm(mat)
  #mask = np.where(num_array > thres)
  lislist =[]
  for row in mat:
    lis =[]
    for j in range(num_thresholds):
      nw = np.where(row > j*part) and np.where(row <= (j+1)*part)
      lis.append(nw)
    lislist.append(lis)
  return lislist

def std_calc(A, num_thresholds):
  sd =np.std(A)

def norm_calc(A, num_thresholds):
  nA = normalize_rows(A)

def average_calc(A, num_thresholds):
  avs = []
  for row in A:
    # label the node based on row
    av_row = np.mean(row)
    avs.append(av_row)
  thres = np.mean(avs)/(num_thresholds)
  # calculate labels / thresholds
  labs = []
  for i in range(num_thresholds):
    # place in threshold


# (2) subgraph based : after find (community) partition that maximizes modularity

par = find_partition(A)

# (3) Random walk based (including propagation kernel) <- normalize row to have (stoch) transition matrix

def normalize_rows(mat):
  n = len(mat)
  mat2 = [] #np.zeros((n,n))
  for row in mat:
    s = np.sum(row)
    mat2.append(row/s)
  return mat2


mat = np.zeros((n,n))
for i in range(n):
  for j in range(n):
    mat[i,j] = G(i,j) # communicability function

nmat = normalize_rows(mat)

# (4) fractional isomorphism calculation (X can be determined by sequence alignment algorithm)
def frac_isom_calc(A, X, B):
  c = np.matmul(A, X) - np.matmul(X, B)
  return np.linalg.norm(c)
