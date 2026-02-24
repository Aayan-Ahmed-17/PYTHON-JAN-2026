import httpx
import asyncio

async def fetch_page():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://books.toscrape.com/")
        
        print(response.status_code)  # 200 matlab OK
        print(response.text)         # HTML content
        return response.text
    
asyncio.run(fetch_page())