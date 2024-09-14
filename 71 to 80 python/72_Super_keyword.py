# Super keyword
# Sometimes we need to call parent class methods from child class methods

class ParentClass:
    def parent_method(self):
        print("this is the parent method.")

class ChildClass(ParentClass):
    def Child_method(self):
        print("this is a child method")
        super().parent_method()

Child_obg = ChildClass()
Child_obg.Child_method()
# Child_obg.parent_method()