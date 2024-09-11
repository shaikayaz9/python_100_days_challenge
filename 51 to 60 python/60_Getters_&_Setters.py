# Getters & Setters in python

class MyClass :
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"{self._value}")

    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


    
obg = MyClass(10)
print(obg.ten_value)
obg.ten_value =67
obg.show()