fruits = ["apple", "banana", "pear"]
userfruit = input("What is your favourite fruit?\n")

# need to check whether userfruit is equal to any item in fruits
x = 0
found = False
while x <= 2:
    if userfruit == fruits[x]:
        print("I like %s too!" % (userfruit))
        found = True
    x = x + 1

if found == False:
    print("I don't like %s" % (userfruit))
