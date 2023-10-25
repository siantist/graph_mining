import kaczmarz
b = B[:,1]
c= kaczmarz.Cyclic.solve(A, b) # cyclic selection rule
c1 = kaczmarz.MaxDistance.solve(A, b) # max dist selection rule
