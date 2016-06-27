class Country:
    population = 0
    capital = ""
    languages = []
    def migrate(self):
        print("Welcome to %s. Population: %d" % (self.capital, self.population))
        self.population = self.population + 1


england = Country()
england.population = 60000000
england.capital = "London"
england.languages.append("English")

egypt = Country()
egypt.population = 50000000
egypt.capital = "Cairo"
egypt.languages.append("French")
egypt.languages.append("Arabic")

# I now have two instances of the Country class 
england.migrate()
