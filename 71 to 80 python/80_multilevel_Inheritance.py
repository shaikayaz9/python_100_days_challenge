# multilevel  Inheritance

# multilevel Inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class.

class Animal:
    def __init__(self ,name , species):
        self.name = name
        self.species = species

    def show(self):
        print(f"name : {self.name}")
        print(f"species : {self.species}")

class Dog(Animal):
    def __init__(self, name,breed):
       Animal.__init__(self , name , species="Dog")
       self.breed = breed

    def Show(self):
        print(f"name : {self.name}")
        print(f"breed : {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self , name ,breed="GoldenRetriever")
        self.color = color

    def show(self):
        print(f"name : {self.name}")
        print(f"color : {self.color}")


# a = Animal("Tiger" , "wild")
# a.show()

# b =Dog("Kutta", "lofi")
# b.show()

c = GoldenRetriever("Tommy" , "black")
c.show()