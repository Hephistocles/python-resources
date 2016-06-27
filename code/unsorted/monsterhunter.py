import random, sys
health = 10

lf = input(" -- Do you have a save file? -- \n")
if (lf == "yes"):
	fn = input(" -- What is your save file called? -- \n")
	f  = open("/home/christoph/dev/firetech/game/" + fn, "r")
	health = int(f.read())

while (health > 0):
	print(" -- You see a monster. Your health is " + str(health) + ". -- ")
	fight = input(" -- Do you fight it, or run away? -- \n")
	if (fight == "fight"):
		while (fight == "fight"):
			monsterWins = random.randint(0,1)
			if (monsterWins):
				print(" -- The monster fights back! Your health is now " + str(health-1) + " -- ")
				health = health - 1
				if (input(" -- Continue? -- \n") != "yes"):
					fight = "no"
					print(" -- Retreat! -- ")
			else:
				print(" -- You defeat him! -- ")
				fight = "no"
	if (health > 0):
		cont = input(" -- Would you like to continue hunting? -- \n")
		if (cont != "yes"):
			fn = input(" -- Where do you want to save your game? -- \n")
			f  = open("/home/christoph/dev/firetech/game/" + fn, "w")
			f.write(str(health))
			sys.exit()

print(" -- You died! -- ")