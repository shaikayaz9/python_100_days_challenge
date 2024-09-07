#file method
import os as a

f = open("new.txt" , "r")
data = f.readline()
print(data)
print(type(data))


# data = f.read(5)             # reads only 5 words
data1 = f.read(8)
print(data1)

# data = f.read()             # reads all words
data2 = f.read() # its readed already data
print(data2)

# data = f.readline()             # reads one line at the time
data3 = f.readable()   # its show me True & false values
print(data3)
f.close()


    