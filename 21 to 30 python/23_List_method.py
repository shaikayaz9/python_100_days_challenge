l= [2,3,90,40,70,35]
print(l)

l.sort() #accending
print(l)

l.sort(reverse=True) #desending
print(l) 

l.reverse() #reverse data

print(l)

m = l.copy() # remove copy & see both list data well be changed
m[0] = 0
print(m)
print(l)
