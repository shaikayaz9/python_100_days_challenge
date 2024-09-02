#solution of exercise 2

import time
t = time.strftime("%H , %M , %S")
# H = int(time.strftime("%H"))
H = int(input("ENTER HOURS BETWEEN RANGE 0 to 24 : "))

if(H >0 and H <= 12):
    print("GOOD MORNING SIR !")
elif(H >=12 and H <17):
    print( "GOOD AFTERNOON Sir !!")
else:
    print("GOOD NIGHT !!!")


print(f"time now is : {H}")