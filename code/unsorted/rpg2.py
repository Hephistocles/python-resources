health = 10
gold = 0

while True:

    # gameplay stuff
    userans = input("Go home, fight in the forest or quit the game?")
    if userans == "fight" or userans == "forest":
        print("A monster appears!")

        monsterwounds = 0
        # repeatedly attack the monster until they have five wounds
        while monsterwounds < 5:
            userans = input("Do you want to stab or run away?")
            if userans == "stab":
                print("You stab the monster but get hurt")
                monsterwounds = monsterwounds + 1
                health = health - 1
                if health == 0:
                    break
            else:
                print("You run away")
                break
        
        if health == 0:
            print("Game over")
            break
        if monsterwounds == 0:
            gold = gold + 1
        
    elif userans == "home" and health < 10:
        health = health + 1
    elif userans == "quit":
        break

    print("\nYour health is now %d and you have %d gold\n" %(health, gold))


print("Your final health was %d and you had %d gold" % (health, gold))
