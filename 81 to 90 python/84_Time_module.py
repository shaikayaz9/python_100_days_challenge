# time Module in Python

import time
# print(time.ctime())
# print(time.daylight)
# print(time.altzone)
# print(time.asctime())

# init = time.time()
# print(time.time() - init)



t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(t)
print(formatted_time)

print(4)
time.sleep(3)
print("this is printed after 3 seconds") # wait for 3 sencods