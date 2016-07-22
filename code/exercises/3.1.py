myFruit = ["apple", "banana", "pear"]
yours = input("What is your favourite fruit?\n")

found_fruit = False

i = 0
while i < len(myFruit):
	if (yours == myFruit[i]):
		found_fruit = True
	i = i + 1

if (found_fruit):
	print("I like " + yours + " too!")
else:
	print("I'm not a fan of " + yours)
