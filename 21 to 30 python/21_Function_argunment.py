# function argument

def avg(a=10,b=4):
    return a + b

print(avg(150,3))

sum = 0
def averge(*numbers):
    print(type(numbers))
    for i in numbers:
        sum =+i
    print(sum)
    print("Avrage is :",sum/len(numbers))



averge(90,78,90,70,66.80)
print()

#marks avg
sum = 0
m = [ 70,60,90,80,73]
for i in m:
   sum = sum + i
   print(i, sum)


print(sum / len(m))

