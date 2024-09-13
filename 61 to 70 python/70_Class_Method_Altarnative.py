# Class Methods as ALternative

class employee:
    def __init__(self, name ,salery):
        self.name = name
        self.salery = salery

    def Show(self):
        print(f"name: {self.name} & my salery {self.salery}")

    @classmethod
    def fromStr(self,string):
        return self(string.split("-")[0],int(string.split("-")[1]))
    


e1 = employee("ayaz",12000)
e1.Show()

string = "Jhon-18000"
e2 = employee.fromStr(string)
e2.Show()