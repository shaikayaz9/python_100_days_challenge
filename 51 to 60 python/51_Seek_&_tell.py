#seek & tell function in python

with open("newData.txt", "r") as f:
 print(type(f))

 f.seek(10) #Move to the 10th byte in the file

 print(f.tell()) #return the current location 
 data = f.read(5) # read the next 5 bytes

print(data)