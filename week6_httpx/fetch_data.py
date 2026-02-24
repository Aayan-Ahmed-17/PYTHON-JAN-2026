import asyncio
import httpx

async def call_api():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
            print(response.status_code)
            print(response.json())
    except Exception as e:
        print("Error:", e)

asyncio.run(call_api())