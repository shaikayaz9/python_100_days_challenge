#map 

def cube(x):
    return x*x*x

print(cube(4))

l = [1,2, 3, 4, 6, 5, 8,2]

newl = list(map(cube , l)) #map
print(newl)


# filter

def f_list(a):
    return a>2

newl2 = tuple(filter(f_list , l))

print(newl2)



#reduce

def red(x):
    pass

newr = reduc