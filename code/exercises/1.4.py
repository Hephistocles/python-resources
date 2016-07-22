print("My name is Christopher")
print("I am 23")
print("I am 1.86m")


# Part B
name = "Christopher"
age = 23
height = 1.86

print("My name is " + name)
print("I am " + str(age))
print("I am " + str(height) + "m")



# Part C
name = input("What is your name?")
age = int(input("What is your age?"))
height = float(input("What is your height?"))

print("My name is " + name)
print("I am " + str(age))
print("I am " + str(height) + "m")




# Part D
print("My name is " + name
		+ "\nI am " + str(age)
		+ "\nI am " + str(height) + "m")

# --- OR ---
print("My name is %s\nI am %d\nI am %.2fm" % 
	(name, age, height))