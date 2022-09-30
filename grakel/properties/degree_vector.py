def degree_vector(A):
    degrees = []
    for row in A:
        s = sum(row)
        degrees.append(s)
        
    return degrees

from tu dataset to nx graph
def degree_vector(A):
    degrees = []
    for row in A:
        row = np.array(row).flatten()
        s = sum(row)
        degrees.append(s)
        
    return degrees
