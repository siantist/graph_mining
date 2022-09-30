def degree_vector(A):
    degrees = []
    for row in A:
        s = sum(row)
        degrees.append(s)
        
    return degrees
