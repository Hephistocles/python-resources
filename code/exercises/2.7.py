def start():
	print("You wake up in a house. How did you get here? You need to get home.")
	main_room()

def main_room():
	ans = input("    Do you go outside (A), go upstairs (B) or into the basement (C)?\n").lower()
	if (ans == "a"):
		print("The door opens and you step outside")
		outside()
	elif (ans == "b"):
		print("You cautiously step upstairs")
		upstairs()
	elif (ans == "c"):
		print("You carefully tread down to the basement")
		basement()
	else:
		print("That is not a valid choice")
		main_room()

def outside():
	print("You see your house across the street. You skip across and are free!")
	win()
			
def basement():
	print("You see some weights, but nothing more interesting")
	while True:
		ans = input("   Do you go back upstairs (A) or keep looking (B)?\n").lower()
		if (ans == "b"):
			print("You don't see anything interesting.")
		else:
			break
	main_room()

def upstairs():
	print("You see nothing else of interest and return downstairs")
	input("    [Press Enter to continue]")
	main_room()

def gameover():
	print("You have died")

def win():
	print("You win!")

start()