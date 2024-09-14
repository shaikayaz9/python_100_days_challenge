# __dir __dict help()

# __dir__
x = (1,2,3)
print(dir(x))
print(type(x))

# dict

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def show(self):
        print(f"my name is {self.name} & my age is {self.age}")

p1 = person("harry",23)
p1.show()
print(p1.__dict__)


#help()

# print(help(str))
print(help(person))