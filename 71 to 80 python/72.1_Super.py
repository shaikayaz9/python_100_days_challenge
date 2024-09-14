class Employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id

    def Show(self):
        print(f"my name is {self.name} id is a {self.id}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("rohan", 34).Show()
ayaz = Programmer("ayaz",90, "python")

print(ayaz.name)
print(ayaz.id)
print(ayaz.lang)