#tuple Operations

#here we are changed our tuple into list & after changed our list & then we changed list to tuple
Countries = ("spain", "india", "pakistan","England" , "italy")
print(Countries)
print(type(Countries))
temp = list(Countries)
print(temp)
print(type(temp))

temp.append("America")
temp.pop(2)
temp[3] = "USA"
Countries = tuple(temp)

print()
print(Countries)
print(type(Countries))