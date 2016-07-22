# tuples is most pythonic, but we don't otherwise look at tuples
def quadratic_solver(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
	return x1, x2 

# alternatively, have two functions
def quadratic_solver1(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
	return x1
def quadratic_solver2(a, b, c):
	x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
	return x2 
