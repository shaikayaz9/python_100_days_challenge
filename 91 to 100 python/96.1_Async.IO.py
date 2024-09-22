# Acync IO python
# before learning AsyncIO we frist have to understand that its neither Multi-threading nor Multi-processing, its jjust a way to run your code Concurrently

import time
import asyncio
print("after 2 second output come AsyncIO")


async def function1():
    await asyncio.sleep(2)
    print("async func 1")

async def function2():
    await asyncio.sleep(2)
    print("async func 2")


async def function3():
    await asyncio.sleep(2)
    print("async func 3")

async def main():
    await function1()   #comment those 3 function then run the code 
    await function2()   #comment those 3 function then run the code 
    await function3()   #comment those 3 function then run the code 
    return 3


    L = await asyncio.gather(
    function1(),
    function2(),
    function3(),)
    print(L)

    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

asyncio.run(main())


