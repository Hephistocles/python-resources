def my_function(x):
	return x + 2

myFunction(0) # returns 2
myFunction(2) # returns 4

# sometimes for people with experience:
def my_function_adv(x):
	if (x%2 == 0):
		return x + 2
	else:
		# reject odds
		return x

# Part B

def my_function2(x):
	return x * 2


# Part C
def linear(m, x, c):
	return m*x + c

# Part C ii
def quadratic(a, b, c, x):
	return a*x**2 + b*x + c