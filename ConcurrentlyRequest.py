from multiprocessing import Queue, Process
# from time import time, sleep
import datetime
import os
import time
import aiohttp
from aiohttp_requests import requests
import asyncio
import aiofiles


def GetApiList(file):
    apis = ["https://www.baidu.com/", "http://www.google.com"]
    return apis


def Write(queue):
    
    with open('responses.txt', 'a') as f:
        while True:
            f.write(queue.get() + '\n')


async def request_url(url, queue):
    start = datetime.datetime.now()
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            end = datetime.datetime.now()
            #print([response.status, start, end])
            queue.put(",".join([str(response.status), str(start), str(end)]))
    
async def Main(queue):
    while True:
        try:
            url="http://www.baidu.com"
            tasks = [request_url(url, queue) for _ in range(3000)]
            await asyncio.gather(*tasks)
        except:
            continue

def RequestProcess(queue):
    
    asyncio.run(Main(queue))

if __name__ == '__main__':
    # apis = GetApiList(None)
    q = Queue()
    request_process = []
    for _ in range(10):
        p1 = Process(target=RequestProcess, args=(q,))
        p1.start()
        request_process.append(p1)

    p2 = Process(target=Write, args=(q,))
    p2.start()
    

    
    
    # queue = Queue()
    # for _ in range(2):
    #     p = Process(target=Request, args=(apis[0], queue))
    #     p.start()
    
    # Process(target=Write, args=(queue,)).start()
