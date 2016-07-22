import sys
class Player:
	has_key = False
	strength = 1
	health = 3

def start(player):
	print("You wake up in a house. How did you get here? You need to get home.")
	main_room(player)

def main_room(player):
	ans = input("    Do you go outside (A), go upstairs (B) or into the basement (C)?\n").lower()
	if (ans == "a"):
		if (player.has_key):
			print("The door unlocks and you step outside")
			outside(player)
		else: 
			print("The front door is locked.")
			main_room(player)
	elif (ans == "b"):
		print("You cautiously step upstairs")
		upstairs(player)
	elif (ans == "c"):
		print("You carefully tread down to the basement")
		basement(player)
	else:
		print("That is not a valid choice")
		main_room(player)

def outside(player):
	print("You see your house across the street. You are so close!")
	print("A big brute is blocking your path.")
	brute_health = 5
	while True:
		attack = input("    Do you attack him?\n").lower()
		if (attack == "yes"):
			print("You hurt him, but he hits you back!")
			if (player.health < brute_health//player.strength):
				print("You're not strong enough!")
			brute_health = brute_health - player.strength
			player.health = player.health - 1
			print("Brute health: %d      Your health: %d" % (brute_health, player.health))
			if (player.health <= 0):
				print("He knocks you to the ground.")
				return gameover(player)
			if (brute_health <= 0):
				print("He falls down!")
				print("You run across the street to your house.")
				return win(player)
		else:
			print("You decide to retreat into the house.")
			return main_room(player)
			
def basement(player):
	print("You see some weights.")
	while True:
		ans = input("   Do you go back upstairs (A) or pump some iron (B)?\n").lower()
		if (ans == "b"):
			player.strength = player.strength + 1
			print("You feel stronger! (Player strength %d)" % (player.strength))
		else:
			break
	main_room(player)

def upstairs(player):
	print("You found a key! It looks like it might open the front door.")
	player.has_key = True
	print("You see nothing else of interest and return downstairs")
	input("    [Press Enter to continue]")
	main_room(player)

def gameover(player):
	print("You have died")
	sys.exit()

def win(player):
	print("You win!")

start(Player())