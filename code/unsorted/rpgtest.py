health = 10
gold = 0

while True:
	print("\nYou currently have health = %d and gold = %d" % (health, gold))
	ans = input("Do you want to go home to rest, hunt beasts in the forest, or quit?\n")
	print("")
	if ans.lower() == "rest" or ans.lower() == "home":
		print("Zzzz")
		health = health + 1
		if health > 10:
			health = 10
	elif ans.lower() == "hunt" or ans.lower() == "forest" or ans.lower() == "beasts":
		print("You encounter a fierce beast!")
		health = health - 1
		if health < 1:
			print("You died!")
			break
		print("The beast is defeated")
		gold = gold + 1
	elif ans.lower() == "quit":
		print("The adventurer retires.")
		break

print("\nFinal gold: %d" % (gold))