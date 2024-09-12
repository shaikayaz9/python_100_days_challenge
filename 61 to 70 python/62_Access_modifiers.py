# Access modifiers in python

# everything in python accesseble in Opps Consept & its alwyas public in python 

# if you use ( self.__name) its a private access modifier you cant use that after the function
class person:
    def __init__(self):
        # self.name = "ayaz"  #public
        self.__name = "ayaz"  #private

a = person()
# print(a.name) #ayaz    #public

print(a._person__name)  #using private 
#cannot be accessed inDirectly

print(a.__dir__())