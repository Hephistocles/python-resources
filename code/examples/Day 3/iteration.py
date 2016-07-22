my_list = [
	"leeks",
	"milk",
	"eggs",
	"butter"
]

# compare a while loop with a for loop so to see the benefit
i = 0
while i < len(my_list):
	item = my_list[i]
	print(item)
	i = i + 1

# much neater! Don't have to worry about counters, or var initialisation, or bounds
for item in my_list:
	print(item)