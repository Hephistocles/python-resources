# simple starter (counter) loop
x = 0
while x<10:
   print("I am on lap number " + str(x))
   x = x + 1


# infinite loop
while True:
	print("I am still going...")


# run-until loop
while True:
	ans = input("Keep going?")
	if ans == "no":
		break

# --- OR occasionally ---
# This is typically useful if we have multiple
# loops within one another, because we can't
# use break in this situation
keep_going = True
while keep_going:
	ans = input("Keep going?")
	if ans == "no":
		keep_going = False
