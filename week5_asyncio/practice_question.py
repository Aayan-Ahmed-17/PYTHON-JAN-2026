"""
01) Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay.
02) Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 seconds).
"""
import asyncio

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
async def display_name_with_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    tasks = [
        display_name_with_delay("Async func 1", 1),
        display_name_with_delay("Async func 2", 2),
        display_name_with_delay("Async func 3", 3),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())