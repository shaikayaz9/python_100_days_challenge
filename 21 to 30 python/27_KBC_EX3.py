print("KBC")
user = input("Enter your name : ") 
marks = int(0)
r = "Right"
w = "Wrong"
print(f"your marks {marks}")
print("Q 1:- height of mount Everest" )
print("1 : 9068m")
print("2 : 8048m")
print("3 : 8928m")
print("4 : 7768m")

a1 = int(input(f"{user} your answer :"))
if(a1 == 2):
    print(r)
    marks = marks +1
else:
    print(w)
    print()

print(f"[{user} your marks : {marks}]")
print()

# #Q2 

print("Q 2:Calculate the value 5*6/3" )
print("1 : 15")
print("2 :10")
print("3 : 5")
print("4 : 12")

a2 = int(input(f"{user} your answer :"))
if(a2 == 2):
    print(r)
    marks = marks +1
else:
    print(w)
    print()

print(f"[{user} your marks : {marks}]")
print()

# #Q3

print("Q3 : ( 4+4 )/ 2" )
print("1 : 4")
print("2 :10")
print("3 : 6")
print("4 : 12")

a3 = int(input(f"{user} your answer :"))
if(a3 == 1):
    print(r)
    marks = marks +1
else:
    print(w)
    print()

print(f"[{user} your marks : {marks}]")
print()

# Q4

print("Q 4 :mrBeast rank in youtube ? " )
print("1 : only in india top 1")
print("2 : under rankLAST")
print("3 :  under TOP 5")
print("4 : Wrolds no 1 rank")

a4 = int(input(f"{user} your answer :"))
if(a4 == 4):
    print(r)
    marks = marks +1
else:
    print(w)
    print()

print(f"[{user} your marks : {marks}]")
