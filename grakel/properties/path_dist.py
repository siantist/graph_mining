# from graph similarity and homomorphism densities
# path distance of graphs
def path_dist(G, H):
     vG = len(G)
     vH = len(H)
     denom = 1/(np.sqrt(vG*vH)) 
     num_iter = 10
     scores = []
     for i in range(num_iter):
     # monte carlo ? 
          X = random_matrix(vG, vH) 
          score = norm2(vH*np.matmul(A,X) - vG*np.matmul(X,B))
          scores.append(score)
     # keep trying X's
     
     return min(scores)
      
