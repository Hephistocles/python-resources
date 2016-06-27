score = 0
if (int(input("What is 5 + 5?\n")) == 10):
	score += 1
	print("Correct!")
else:
	print("I'm afraid not! The correct answer was 10.")
if (input("What the biggest animal?\n") == "blue whale"):
	score += 1
	print("Correct!")
else:
	print("I'm afraid not! The correct answer is the blue whale")

print("Your final score was %i"%(score))
if (score<3):
	print("Better luck next time!")
else:
	print("Great work!")