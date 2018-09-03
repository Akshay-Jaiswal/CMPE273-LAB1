import requests
# #import async
# import asyncio

# #r = requests.get('https://webhook.site/6e55c3c9-95eb-4b1d-bffe-6518321f70ae')
# #print(r.headers['Date'])
    
# import aiohttp
# import asyncio

# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         r = await fetch(session, 'https://webhook.site/6e55c3c9-95eb-4b1d-bffe-6518321f70ae')
#         print(r)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time;

url = 'https://webhook.site/c477a679-bd4a-4ada-9aa9-3df926edb965';

def getDate(url):
    #time.sleep(3)
    r = requests.get(url)
    return r.headers['Date']

pool = ThreadPool(5)

results = pool.map(getDate,[url,url,url,url,url,url])
print(results)
