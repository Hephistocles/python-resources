class Cow:
    kind = "cow"
    name = ""
    milkiness = 0
    def make_noise(self):
        print("%s the %s says '%s'" % (self.name, self.kind, "moo"))
    def get_milk(self):
        print( "Milk! " * self.milkiness)
class Rabbit:
    kind = "rabbit"
    name = ""
    bounciness = 1
    def make_noise(self):
        print("%s the %s says '%s'" % (self.name, self.kind, "..."))
    def bounce(self):
        print("   __   " * self.bounciness)
        print("  /  \  " * self.bounciness)
        print("_/    \_" * self.bounciness)
class Frog:
    kind = "frog"
    name = ""
    tongue_length = 1
    def make_noise(self):
        print("%s the %s says '%s'" % (self.name, self.kind, "crooooak"))
    def eat_fly(self):
        print("( o)_" + "_"*self.tongue_length + "\"")


animals = []
animals.append(Frog())
animals[0].name = "Fred"
animals[0].tongue_length = 5
animals.append(Rabbit())
animals[1].name = "Rory"
animals[1].bounciness = 3
animals.append(Frog())
animals[2].name = "Fenella"
animals[0].tongue_length = 3
animals.append(Cow())
animals[3].name = "Cuthbert"
animals[3].milkiness = 3
animals.append(Rabbit())
animals[4].name = "Rupert"
animals[4].bounciness = 2

def enter_the_farm(animal_list):
    for a in animal_list:
        a.make_noise()
        if a.kind == "frog":
            a.eat_fly()
        elif a.kind == "cow":
            a.get_milk()
        elif a.kind == "rabbit":
            a.bounce()
        print("")

enter_the_farm(animals)

