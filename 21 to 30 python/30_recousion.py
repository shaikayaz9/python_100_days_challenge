# recousion in python

def Factorial(n):
    if(n ==0 or n == 1):
        return 1
    else:
        return n * Factorial(n-1)

print(Factorial(3))
print(Factorial(4))
print(Factorial(5))
print(Factorial(6))


print(0*1)
print(1*2)
print(2*3)
print(6*4)
print(24*5)
print(1*2*3*4)