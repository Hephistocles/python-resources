examscores = {}
subjects = ["English", "French", "Geography", "Maths"]

for subject in subjects:
    examscores[subject] = int(input("What did the user get in %s?" % (subject)))
    if examscores[subject] > 50:
        print("They passed!")
    else:
        print("They failed")

if examscores["English"] > 50 and examscores["French"] > 50 and examscores["Geography"] and examscores["Maths"]:
    print("They passed overall!")
