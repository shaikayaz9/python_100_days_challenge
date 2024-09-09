#map 

def cube(x):
    return x*x*x

print(cube(4))
l = [1,2, 3, 4, 6, 5, 8,2]

newl = list(map(lambda x :x*x*x, l))

# newl = list(map(cube , l)) #map
print(newl)


# filter

def f_list(a):
    return a>2

newl2 = tuple(filter(f_list , l))

print(newl2)



#reduce 

from functools import reduce

number = [1,2,3,4,5]
sum = reduce(lambda x,y :x+y,number)
print(sum)
