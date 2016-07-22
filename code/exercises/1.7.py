print("Think of a number!")
input("[Press Enter to continue]")
start_number = 5 # guessing the user's number is 5
x = start_number

print("Add 3 to it!")
input("[Press Enter to continue]")
x = x + 3

print("Add 10 to it!")
input("[Press Enter to continue]")
x = x + 10

print("Subtract the original number!")
input("[Press Enter to continue]")
x = x - start_number

print("Multiply by two!")
input("[Press Enter to continue]")
x = x * 2

print("You are thinking of %d!" % x)