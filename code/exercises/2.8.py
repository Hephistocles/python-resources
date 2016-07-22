has_key = False
strength = 1
health = 3

def start(has_key, strength, health):
	print("You wake up in a house. How did you get here? You need to get home.")
	main_room(has_key, strength, health)

def main_room(has_key, strength, health):
	ans = input("    Do you go outside (A), go upstairs (B) or into the basement (C)?\n").lower()
	if (ans == "a"):
		if (has_key):
			print("The door unlocks and you step outside")
			outside(has_key, strength, health)
		else: 
			print("The front door is locked.")
			main_room(has_key, strength, health)
	elif (ans == "b"):
		print("You cautiously step upstairs")
		upstairs(has_key, strength, health)
	elif (ans == "c"):
		print("You carefully tread down to the basement")
		basement(has_key, strength, health)
	else:
		print("That is not a valid choice")
		main_room(has_key, strength, health)

def outside(has_key, strength, health):
	print("You see your house across the street. You are so close!")
	print("A big brute is blocking your path.")
	brute_health = 5
	while True:
		attack = input("    Do you attack him?\n").lower()
		if (attack == "yes"):
			print("You hurt him, but he hits you back!")
			if (health < brute_health//strength):
				print("You're not strong enough!")
			brute_health = brute_health - strength
			health = health - 1
			print("Brute health: %d      Your health: %d" % (brute_health, health))
			if (health <= 0):
				print("He knocks you to the ground.")
				return gameover(has_key, strength, health)
			if (brute_health <= 0):
				print("He falls down!")
				print("You run across the street to your house.")
				return win(has_key, strength, health)
		else:
			print("You decide to retreat into the house.")
			return main_room(has_key, strength, health)
			
def basement(has_key, strength, health):
	print("You see some weights.")
	while True:
		ans = input("   Do you go back upstairs (A) or pump some iron (B)?\n").lower()
		if (ans == "b"):
			strength = strength + 1
			print("You feel stronger! Player strength %d)" % (strength))
		else:
			break
	main_room(has_key, strength, health)

def upstairs(has_key, strength, health):
	print("You found a key! It looks like it might open the front door.")
	has_key = True
	print("You see nothing else of interest and return downstairs")
	input("    [Press Enter to continue]")
	main_room(has_key, strength, health)

def gameover(has_key, strength, health):
	print("You have died")

def win(has_key, strength, health):
	print("You win!")

start(has_key, strength, health