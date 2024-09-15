# Single Inheritance in python

#most of the Inheritance is a single Inheritance

class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print(f"sound made by the {self.name}")

# 2nd class 


class Dog(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")




a = Animal("Dog", "dog")
a.make_sound()

b = Dog("Dog", "doggerman")
b.make_sound()


# Quick Quiz : Implement a cat class by using the animal class .add


class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        return super().make_sound()
    
c = Cat("cat", "billi")
c.make_sound()