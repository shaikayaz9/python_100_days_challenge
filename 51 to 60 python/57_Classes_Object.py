# Classes & Objects in Python

# A class is a blueprint of a template for creating objects, 
# providing initial values for state

class person: # its a Class
    name = "Harry"
    occupation = "Softwere Developer"
    networth = 1000
    def info(self):
        print(f"{self.name} is a {self.occupation}") 

a = person()  # its a Object
a.name = "ayaz"
a.occupation = "editor"

b = person() # its a Object
b.name = "Virat kohi"
b.occupation = "Cricketer"

c = person() # its a Object

# print(a.name , a.occupation)

a.info()
b.info()
c.info()