# for loops in python

#for loops in string
name = " Codear With Harry"

for i in name:
    print(i )
    if(i == "a"):
        print("Something is special")

#for loops in list

colors = ["red" , "green" , "yellow" , "orange"]

for i in colors:
    print(i)
    for j in i:
        print(j)

# range prohram to print numbers

for i in range(0,20,2): #start = 1 , stop = 20 , step = 2
    print(i)