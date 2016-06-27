class Shape:
    colour = ""
    numberOfSides = 0
    def area(self):
        return 0
    def describe(self):
        print("I am a generic shape")

class Rectangle(Shape):
    numberOfSides = 4
    height = 0
    width = 0
    def area(self):
        return self.height * self.width
    def describe(self):
        print("I am a rectangle with area " + str(self.area()))

class Square(Rectangle):
    def describe(self):
        print("I am a square. All my sides are the same.")

    
    
