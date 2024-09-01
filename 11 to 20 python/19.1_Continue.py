j = int(input("Number : "))
for i in range(12):
    if(i == 5):
       continue
    elif(i ==10):
        continue
    print(j,"X",i+1,"=",j*(i+1))


    #skip the values after 5 & 10