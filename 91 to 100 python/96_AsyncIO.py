# Acync IO python
# before learning AsyncIO we frist have to understand that its neither Multi-threading nor Multi-processing, its jjust a way to run your code Concurrently


# normal way to run code

import time
print("after 2 second output come")
def function11():
    time.sleep(2)
    print("normal func 1")

def function22():
    time.sleep(2)
    print("normal func 2")


def function33():
    time.sleep(2)
    print("normal func 3")

function11()
function22()
function33()
# AsyncIO method
import asyncio
print("after 2 second output come AsyncIO")


async def function1():
    time.sleep(3)
    print("async func 1")

async def function2():
    time.sleep(3)
    print("async func 2")


async def function3():
    time.sleep(3)
    print("async func 3")

async def main():
    await function1()
    await function3()
    await function2()

asyncio.run(main())