# solution of Exercise 5

#snake Water Gun game in python
import random
user = input("Chosee ( Snake | Water | Gun ) : ")
computer = ["water", "gun", "snake"]

a = random.randint(0,2)
comp = computer[a]

if(user == comp):
    result = ".. DROW .."
elif (user == "water" and comp == "gun"):
    result = ".. You Win .."
elif (user == "gun" and comp == "snake"):
    result = ".. You Win .."
elif (user == "snake" and comp == "water"):
    result = " .. You Win .."
else:
    result = " .. You Lose .."


print(f"user : {user}, Computer : {comp}")
print(f"RESULT : {result}")

#make by ayaz shaik Without Watched any tetorial &  its a semilar example of ( rock peper sisor )