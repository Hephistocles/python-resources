my_list = ["bananas", "apples", "pears"]
user_list = []

while True: 
	new_fruit = input("What fruit do you like?")
	user_list.append(new_fruit)
	quit_question = input("Would you like to continue?")
	if (quit_question != "yes"):
		break

# Two lists of fruit - user_list and my_list

for user_fruit in user_list:
	if user_fruit in my_list:
		print("We both like " + user_fruit)