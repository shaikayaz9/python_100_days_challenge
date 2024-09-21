# Function Caching is used when a single function is running multiple times for the same valuein that case we use memoization technique.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5

# output will come after 3 sec
print(fx(5))
print("done for 5")
print(fx(6))
print("done for 6")
print(fx(2))
print("done for 2")

# 2nd time its will run fast becuose python alreday did & know the values
print(fx(5))
print("done for 5")
print(fx(6))
print("done for 6")
print(fx(2))
print("done for 2")