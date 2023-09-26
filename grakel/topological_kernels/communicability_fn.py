# communicability function between pair of nodes p,q 
def G(p,q):
	s = 0
	for mu in range(n):
		s = s+ exp(lambda[mu])*phi[mu][p]*phi[mu][q]
	return s 
