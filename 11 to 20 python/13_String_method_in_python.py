# STring methods in python

# strings are immutable's


a = "ayAZ ShaiK !!!!!!!!!!!!!" #ignore the uppercase & lowercase 

#length function
print(len(a)) # 10

#length uppercase
print(a.upper())  # AYAZ SHAIK

#length lowercase
print(a.lower()) # ayaz shaik

#length capitalize
print(a.capitalize())  #Ayaz shaik

# rstrip
print(a.rstrip("!")) # ! ignored

#replace
print(a.replace("a", "p")) # pyAZ ShpiK !!!!!!!!!!!!!

b = a.lower()
print(b)
print()

print(b.replace("ayaz", "Harry"))

# split make a list & saprete with value
print(b.split(" "))

# center
print(b.center(50)) #space before content

# count
print(b.count("a")) #3

# find
print(b.find("s")) #5 index

# islower
print(b.islower()) #True

#swapcase()
print(a.swapcase())

str2 = "His name is dan, Dan is a driver at university"
print(str2.title())