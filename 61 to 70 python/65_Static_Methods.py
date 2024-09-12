# Static Method's in python
# Static method'a are the methods which neither belongs to instance nor to class .


class Math:
    def __init__(self, num):
        self.num = num
   
    def addnum(self, n):
        self.num = self.num + n 

    @staticmethod
    def add(a,b):
        return a +b
    
# result = Math.add(4,80)
# print(result)

a = Math(5)
print(a.num)
a.addnum(6)
print(a.num)

print(a.add(60,6))

