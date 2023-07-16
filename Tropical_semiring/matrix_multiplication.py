# mat mult for square matrices
# procedure to find the tropical eigenvalues requires matrix multiplication
# A otimes v = lambda otimes v means that lambda is eigenvalue with eigenvector v
# mult is add, add is min 
def mult_tropical_min(A, B): # matrix A, B 
	n = len(A)
	C = np.zeros((n,n ))	
	for i in range(n):
		for j in range(n):
			arow = A[i,:]
			bcol = B[:,j]
			cvec = arow + bcol 
			C[i,j] = min(cvec)
	
	return C 

# for A times vector x in (n,1) 
def mult_tropical_min_vec(A, x): 
	n = len(A)
	C = np.zeros((n,1))
	for i in range(n):
		arow = A[i,:]
		avec = []
		for j in range(n):
			xj = x[j]
			avec.append(arow[j] + xj) 
		C[i] = min(avec) 
	return C
			

# mult is add, add is max 
def mult_tropical_max(A, B):
	n = len(A)
	C = np.zeros((n,n ))	
	for i in range(n):
		for j in range(n):
			arow = A[i,:]
			bcol = B[:,j]
			cvec = arow + bcol 
			C[i,j] = max(cvec)
	
	return C 
