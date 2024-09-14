# method overriding : when we have a redefine a parent class method according to a child class method.
# its a very importent topic in OPPs consept

class Shape:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius , radius)

    def area(self):
        return 3.14 * super().area()

a = Shape(29,4)
print(a.area())

c = Circle(5)
print(c.area())
