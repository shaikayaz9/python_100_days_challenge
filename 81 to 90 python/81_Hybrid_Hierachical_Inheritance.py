# Hybrid Heirachical Inheritance

# when we use more then one  Inheritance we call it Hybrid Inheritance

# Example of Hybrid Inheritance
class BaseClass:
    pass

class Derived(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived , Derived2):
    pass


# Herichical Inheritance is a type of Inheritance Where multiple subclasses inherit from a single base class.
# Example of Herichical Inheritance


class BClass:
    pass

class D1(BClass):
    pass

class D2(BClass):
    pass

class D3(D1):
    pass