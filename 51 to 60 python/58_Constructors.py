# constructor 

# normal Class without Using Constructor

class person :
    name = "harry"
    occ = "Developer"

    def info(self):
     print(f"{self.name} is a {self.occ}")

a = person()
a.name = "panda"
a.occ = "HR"

a.info()
print( " ")

#Using Constructor

class human:
   def __init__(self,name,occ):
       print("HEY I AM A HUMAN")
       self.name = name
       self.occ = occ

   def info(self):
    print(f"{self.name} is a {self.occ}")


b = human("ayaz","WEB_DEVELOPER")
c = human("fasi", "Gamer")
b.info()
c.info()