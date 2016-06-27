########################################
## THE NEW AND IMPOROVED QUIZ GAME!!! ##
########################################

def ask(question,answer):
    yourAnswer = input(str(question) + "\n").lower()
    if yourAnswer == answer:
        print("Correct!")
        return 1
    else:
        print("Wrong, the answer was %s" %(answer))
        return 0
    
score = 0

score = score + ask("What is 5 + 5?","10")
score = score + ask("What is the biggest animal?","blue whale")
score = score + ask("What is the capital of the UK?","london")


print("Well done, you scored %s out of 3!" %(score))
