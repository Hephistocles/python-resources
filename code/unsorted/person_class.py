import random
random.randint(0,10)
class Human:
	hair_colour = None
	height      = None
	name        = None
	number_of_legs = 2
	def walk(self):
		print(self.name + " says 'Plod plod plod'")
	def grow(self):
		self.height = self.height + 0.1
		print(self.name + " is now " + str(self.height) + "m tall")
people = []

person = Human()
person.name = "Bruce"
person.hair_colour = "Brown"
person.height = 1.60
person.walk()
people.append(person)

person = Human()
person.name = "Fiona"
person.hair_colour = "Blonde"
person.height = 1.40
people.append(person)

print(people)