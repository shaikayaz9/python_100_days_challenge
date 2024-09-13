#  Instance Varaible Vs Class Vairables

class person:
    company = "Apple"
    def __init__(self, name):
        self.name = name

    def ShowInfo(self):
        print(f"my name is a {self.name},& working at {self.company}")


p1 = person("panda")
p1.name = "ravi"
p2 = person("ayaz")

p1.ShowInfo()
p2.ShowInfo()
person.ShowInfo(p1)