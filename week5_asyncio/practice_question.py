<<<<<<< HEAD
"""
01) Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
"""
import asyncio
=======
"""
01) Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
02) Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).
03) Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each.
04) Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken.
"""
import asyncio
import time
>>>>>>> 4c83c988cd38bcd82606605fd9ab27e0a39dd0d9

<<<<<<< HEAD
async def welcome():
    await asyncio.sleep(2) 
    print("Python Exercises!")

asyncio.run(welcome())
=======
"""01"""
# async def print_delayed_message():
#     await asyncio.sleep(2)  # Wait for 2 seconds
#     print("Python Exercises!")

# # Create an event loop and run the asynchronous function
# async def main():
#     await print_delayed_message()

# # Run the event loop
# asyncio.run(main())

"""02"""
# async def display_name_with_delay(name, delay):
#     await asyncio.sleep(delay)
#     print(name)

# async def main():
#     tasks = [
#         display_name_with_delay("Async func 1", 1),
#         display_name_with_delay("Async func 2", 2),
#         display_name_with_delay("Async func 3", 3),
#     ]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

"""03"""
# async def display_numbers():
#     for r in range(1,8):
#         await asyncio.sleep(1) 
#         print(r)

# asyncio.run(display_numbers())

"""04"""
async def task1():
    print("Task-1 started")
    await asyncio.sleep(4)
    print("Task-1 completed")

async def task2():
    print("Task-2 started")
    await asyncio.sleep(3)
    print("Task-2 completed")

async def task3():
    print("Task-3 started")
    await asyncio.sleep(2)
    print("Task-3 completed")

async def main():
    start_time = time.time()
    await asyncio.gather(task1(), task2(), task3())
    end_time = time.time()
    time_taken = end_time - start_time
    print("/n All function taken time {:.2}".format(time_taken))

asyncio.run(main())

>>>>>>> 4c83c988cd38bcd82606605fd9ab27e0a39dd0d9