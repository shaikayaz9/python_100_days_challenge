#short hand if elif else 


a = int(input("Enter : "))
b = 5
# print(f"{a} is greater the {b}")if a>b else print(f"{b} is greather the {a}") 
# if a == b print("Both arer smae")

print("A") if a>b else print("=") if a == b else print("B")

print(f"{a} is greater the {b}") if a>b else print("Both arer smae") if a == b else print(f"{b} is greather the {a}")