ep1 = {122:45, 334:89, 567:74, 349:90}
ep2 = {222:76 , 566:59}
# print(ep1)
ep1.update(ep2)
print(ep2)
print(ep1)
# ep2.clear()

print(ep1.pop(122)) #remove manually item
print(ep1.popitem()) #remove last item
print(ep1)