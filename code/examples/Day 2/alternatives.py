# say we are reporting the score
# aiming to hit a bulseye of 5

# Without alternatives, several branches are taken
# also we can't say "for all other results, print("you're rubbish")"
result = 5
if (result == 5):
	print("Bullseye!")
if (4 < result and result < 7):
	print("Close!")
if (0 < result and result < 10):
	print("You can do better")


# with alternatives, we can
result = 5
if (result == 5):
	print("Bullseye!")
elif (4 < result and result < 7):
	print("Close!")
elif (0 < result and result < 10):
	print("You can do better")
else:
	print("You're rubbish.")
