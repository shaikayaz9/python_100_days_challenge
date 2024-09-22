# Multithreading in python

# the frist one is the use case of multithreading that is when you want to download reasource parallelly from the internet if you want to downlaod 10 file its will be downlaod one by one 


import threading
import time

def func(second):
    print(f"sleeping for {second}")
    time.sleep(second)

#normal code
# func(4)
# func(2)
# func(1)

#same code using Thread
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1])

t1.start()
t2.start()
t3.start()