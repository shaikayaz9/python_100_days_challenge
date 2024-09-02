# list in python

marks = [2,3,5,True , "ayaz",9]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

marks.append(60)
print(marks)
marks[0] = 200
print(marks)


print(marks[-3]) #5
print(marks[len(marks)-3]) #5
print(marks[5-3]) #5
print(marks[2]) #5


if 0 in marks:
    print("yes")
else:
    print("NO")