# import time
# import asyncio
#
# async def generate_number():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(1)
#
# async def check():
#     print("ASinxron ishladi")
#
# async def main():
#     task1 = generate_number()
#     task2 = check()
#     await asyncio.gather(task1,task2)
#
# asyncio.run(main())

# ---------------------------------------------------------------------------------------------------------------------

# import time
# import asyncio
#
# async def generate_number():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(1)
#
# async def check():
#     for i in range(10):
#         print("Asinxron ishladi")
#         await asyncio.sleep(1)
#
# async def main():
#     task1 = asyncio.create_task(generate_number())
#     task2 = asyncio.create_task(check())
#     await task1
#     await task2
#
# asyncio.run(main())

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------



import requests
import time
import asyncio
import aiohttp
from pprint import pprint

# cities = ['Fergana', 'Tashkent', 'London', 'Andijon', 'Namangan', 'Bukhara', 'Khiva']

async def weather(city_name):
    parameters = {
        'q': city_name,
        'appid': 'c60721aafdeba2d1ac86216158a6d288',
        'units': 'metric'
    }

    url = 'https://api.openweathermap.org/data/2.5/weather?'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params = parameters) as response:
            res = await response.json()
            city = res['name']
            temp = res['main']['temp']
            description = res['weather'][0]['description']
            print("\033[34m{}\033[0m".format(f"Hozir {city} shahrida havo harorati {temp} gradus. Havo: ""\033[37m{}\033[0m".format(f"{description}")))



async def main():
    # tasks = []
    # for city in cities:
    #     task = asyncio.create_task(weather(city))
    #     tasks.append(task)
    #
    # for task in tasks:
    #     await task
    while True:
        print("\033[37m {}".format("----------------------------------------------------------------------------"))
        cities = input("\033[32m {}".format("Shahar nomini kiriting: "))
        if cities == "stop":
            print("\033[31m {}".format("Dastur to'xtatildi!!!"))
            break
        try:
            cities
        except KeyboardInterrupt:
            print("Bunday shahar yo'q")
        get_weather = await weather(cities)

start = time.time()

try:
    asyncio.run(main())
except:
    print("\033[33m {}".format("Shahar nomi noto'gri kiritildi!!!"))
    asyncio.run(main())
end = time.time()




print("\033[31m {}".format(f"{round(end-start)} second vaqt davomida ishladi!!!"))
print("\033[37m {}".format("----------------------------------------------------------------------------"))

