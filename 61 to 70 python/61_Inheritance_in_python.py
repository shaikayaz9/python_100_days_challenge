# Inheritanc in python

#parent Class
class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"my name is {self.name} & my id is {self.id}")

a = person ("ayaz",653)
a.info()


# Inheritance --
# Child class
class Programmer(person):
    def Showlanguage(self):
        print("the defualt language is python")

b = Programmer("baba",123)
b.info()
b.Showlanguage()