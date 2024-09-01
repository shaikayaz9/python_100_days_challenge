#table in python
j = int(input("number : "))

i = 1
while(i <= 10):
    print(j, "X",i,"=",j*i)
    i +=1


for i in range(12):
    if(i == 10):
        break
    print(j,"X",i+1,"=",j*(i+1))