import aiohttp
import asyncio
import time

PING_INTERVAL = 10 # In Minutes

# List of URLs to ping
urls = [
    'https://mbape-backend.onrender.com',
    'https://www.app.mbape.xyz',
]

async def ping_url(session, url):
    try:
        async with session.get(url) as response:
            print(f"Pinged {url} with status {response.status}")
    except Exception as e:
        print(f"Failed to ping {url}: {e}")

async def ping_urls():
    async with aiohttp.ClientSession() as session:
        tasks = [ping_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

async def main():
    while True:
        print("Pinging URLs...")
        await ping_urls()
        print("Sleeping for 10 minutes...")
        await asyncio.sleep(PING_INTERVAL * 60)  # 10 minutes

if __name__ == '__main__':
    asyncio.run(main())

