def askQuestion(question, answer):
	userans = input(question)
	if userans.lower() == answer.lower():
		print("That's right!")
		return 1
	else:
		print("I'm afraid the correct answer was %s" % (answer))
		return 0

score = 0
score = score + askQuestion("What is the capital of England?", "London")
score = score + askQuestion("What is the capital of France?", "Paris")
score = score + askQuestion("What is the capital of Spain?", "Madrid")
score = score + askQuestion("What is the capital of Italy?", "Rome")
score = score + askQuestion("What is the capital of Greece?", "Athens")

print("Your score was %d" % (score))
if score>=3:
	print("Great work!")
