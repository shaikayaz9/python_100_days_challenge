# in set you cant have duplicate values in arry if you have then its consider into 1 value's
# set in unordered list
a = [40,40,50,50,60,60,70,80,"ayaz"]
d = {40,40,50,50,60,60,70,80,"ayaz"}
a.append("fayaz")
print(a)

#for empty set use set()

b = set()
print(type(b)) 
# change list into set
c = set(a)
for i in c:
    print(i)

print(type(c))