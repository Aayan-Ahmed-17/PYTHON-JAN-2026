# Exploring the structure code and the need of asyncio module

"""
asyncio.run() == runs the main async function
asyncio.gather() == runs multiple async function
await == pause the execution of async func
coroutine == aka async defined function
create_task == assigns task in backgroung, whenever python gets time it move to ward that function and start executing that
futures == placeholder for future vals of currently executing task
"""

import asyncio


async def say_hello_async():
    await asyncio.sleep(2)  # Simulates waiting for 2 seconds
    print("Hello, Async World!")


async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulates doing something else for 1 second
    print("Finished another task!")


async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )


asyncio.run(main())
