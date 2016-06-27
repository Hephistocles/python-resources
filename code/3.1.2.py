myFruit = ["apple", "banana", "pear"]
y = True
while (y):
	yours = input("What is your favourite fruit?")
	if (yours in myFruit):
		print("I like " + yours + " too!")
	else:
		print("I'm not a fan of " + yours)
	y = input("Would you like to continue (y/n)") == "y"