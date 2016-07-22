mode = input("What mode would you like? (plus, minus, multiply or divide)\n")
x = int(input("What is the first number?\n"))
y = int(input("What is the second number?\n"))

if (mode == "plus"):
	print("The answer is " + str(x + y))
if (mode == "minus"):
	print("The answer is " + str(x - y))
if (mode == "multiply"):
	print("The answer is " + str(x * y))
if (mode == "divide"):
	print("The answer is %.1f"%(x / y))