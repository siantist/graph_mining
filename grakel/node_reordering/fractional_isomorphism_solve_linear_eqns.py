# AX = XB
# find fractional change to make it closer 

a = np.array(a)
b = np.array(b)

k=2
Q = np.zeros((k*k,k*k))
# set Q matrix 

# find the diagonal blocks
diag_blocks = {}
for i in range(k):
    # subtract b_ii I from A 
    bii = b[i,i]
    identity = np.identity(k)
    bi = bii*identity
    block = np.subtract(a, bi)
    # set the block 
    #print(block)
    diag_blocks[i] = block

# find the off diag blocks
off_diag_blocks={}
for i in range(k):
    for j in range(k):
        if i=!j:
            bji_minus = -b[j,i]
            identity = np.identity(k)
            block = bji_minus*identity
            off_diag_blocks[(i,j)] = block
            
            
