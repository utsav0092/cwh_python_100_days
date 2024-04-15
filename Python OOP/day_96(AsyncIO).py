# # import time
# import asyncio
#
#
# async def function_1():
#     # time.sleep(1)
#     await asyncio.sleep(2)
#     print("func 1")
#     return "Code"
#
#
# async def function_2():
#     # time.sleep(2)
#     await asyncio.sleep(1)
#     print("func 2")
#     return "With"
#
#
# async def function_3():
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("func 3")
#     return "Harry"
#
#
# # async def main():
#     # task = asyncio.create_task(function_1())
#     # # await function_1()
#     # await function_2()
#     # await function_3()
# # asyncio.run(main())
# async def main():
#     task = await asyncio.gather(
#         function_1(),
#         function_2(),
#         function_3(),
#     )
#     print(task)

import time
import asyncio
import requests


async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)

    return "Harry"


async def function2():
    print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)


async def main():
    """IT will run slow"""
    # await function1()
    # await function2()
    # await function3()
    # return 3
    
    """IT will run fast"""
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()


asyncio.run(main())
