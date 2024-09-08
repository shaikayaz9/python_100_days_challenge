# Lambda function is exactly work like annomunuse function

#normal function with argu
def sum(x):
    return x*2

a = sum(5)
print("normal function :",a)


# lamba function 
lam = lambda y : y*2

print("lambda function :",lam(5))



#examples

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y: (x+y)/2

print(double(5))
print(cube(5))
print(avg(46,80))

def app(fx, value):
    return 6 +fx(value)

print(app(lambda x :x*x, 2))

# without name work lambda

print(lambda x: x*x)