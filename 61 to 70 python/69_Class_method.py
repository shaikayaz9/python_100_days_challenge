# class method

class person:
    company = "APPLE"
    def show(self):
        print(f"the name is {self.name} & company is {self.company}")

    # @classmethod #if you used then child value overloading
    def ChangeC(self, newComp):
        self.company = newComp

p1 = person()
p1.name = "ayaz"
p1.show()
p1.ChangeC("google")
p1.show()
print(person.company)