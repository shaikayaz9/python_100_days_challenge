# Dictionary in python

dict = {
    "name":"ayaz shaik",
    "age":23,
    "spoon": "object",
}

print(dict["name"])   #ayaz
print(dict.get("name"))  #ayaz

# print(dict["name2"]) #error 
print(dict.get("name2")) # not error

print(dict.keys())
print(dict.values())
print(dict)
x = dict.items()
print(type(x), x)