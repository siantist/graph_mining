# check if partition is equitable
def check_equitable(partition, A):
    # check intersections of partition
    m = len(partition)
    for i in range(n):
        for j in range(n):
            Si = partition[i]
            Sj = partition[j]
            di = deg_v_in_S(i, Si, A)
            dj = deg_v_in_S(j, Sj, A)

"""
set intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)"""

def deg_v_in_S(v,S, A): # A adj mat
    nv = A[v] # nbrs of v
    intersect = nv.intersect(S)
    return intersect
