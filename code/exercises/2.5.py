s = int(input("How tall would you like the pyramid to be?\n"))
n = 0

print("Here is your pyramid!")
while (s>0):
	print((" " * s) + ((1 + 2* n) * "*"))
	n += 1
	s -= 1