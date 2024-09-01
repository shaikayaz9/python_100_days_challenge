# String slicing in python

names = "Ayaz Harry"

print("total names :") #str = Ayaz Harry
print(len(names)) # length of str = 10
print(names[0:5]) #ayaz
print(names[:5]) #ayaz
print(names[5:]) #harry & rest of str length
print(names[2:5]) #az
print(names[6: len(names)]) #arry
print(names[:]) #total lenth of str = Ayaz Harry


#negative slicing in python

str1 = "Code with Harry"
print()
print(str1[0:-3]) #Code with Ha
print(str1[0:len(str1)-3]) #Code with Ha
print(str1[0:-10]) #Code
print(str1[5:-3]) #with Ha
print(str1[1:-4]) #ode with H
print(str1[-10:-5]) # with

mn = "Ayaz"
print(mn[-3:-2]) #y


#day 12 in python (ayaz)