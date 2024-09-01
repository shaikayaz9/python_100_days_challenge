#wap to say Good Moorning

import time
t = time.strftime(' %H:%M:%S')
print(t)
H = int(time.strftime('%H'))
print(H)
M = int(time.strftime('%M'))
print(M)
S = int(time.strftime('%S'))
print(S)


if(H< 12):
    print("Good Morning")
else:
    print("Good night")