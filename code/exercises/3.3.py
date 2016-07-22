n = int(input("How many students are there?\n"))
subjs = ["English", "Geography", "French"]
scores = {}
for i in range(n):
	name = input("What's the name of student #" + str(i+1) + "\n")
	scores[name] = []
	for s in range(len(subjs)):
		score = input("What did " + name + " get in " + s + "?\n")
		if (score>50):
			print("They passed!")
		scores[name][s] = score

allSubj = ""
for subj in subjs:
	allSubj += " | " + subj
print("        " + allSubj)
print("--------------------")
for peep in scores.keys():
	allScore = peep
	for score in scores[peep]:
		allScore += " | " + score
	print(allScore)
		
