# multiple Inheritance is called when a class inherits from from then on parent classes

class Employee:
    def __init__(self,name):
        self.name = name 

    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"the dance is {self.dance}")

class Dancer_Employee(Employee , Dancer):
    def __init__(self, name,dance):
        self.name = name
        self.dance = dance


a = Dancer_Employee("ayaz","classic")
a.show()

print(Dancer_Employee.mro())
