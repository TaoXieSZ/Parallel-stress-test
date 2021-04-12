# This class is to parallelly request apis and then send to Server (Server.py)
# helper functions we need:
# 1. GetApiList(file) -> List[<url: str, method: str, headers: dict, body: dict>]
# 2. Request
# 3. Send():
#   Use Queue to send message
from multiprocessing import Pool
from multiprocessing.connection import Client
from time import time, sleep
import time
import os

def GetApiList(file):
    """[summary]

    Args:
        file ([str]]): [path of file]

    Returns:
        [list]: [api_list]
    """
    apis = []
    return apis

def Request(api):
    """[summary]

    Args:
        api ([str]): [requesting api]

    Returns:
        [tuple]: [<api_name, start_time, end_time>]
    """
    record = ['api', 'start', 'end']
    return record

add = ('localhost', 6001)
def Send():
    """[summary]
    Demo of Send() function
    """
    with Client(add) as conn:
        start = time.time()
        end = time.time()
        print([os.getpid(), 'api', start, end])
        conn.send(['api', start, end])

if __name__ == '__main__':
    # 1. Call GetApiList()

    # 2. Initialization:
    #   2.1 processes
    #   2.2 Queue
    #
    # 3. Start process with Queue and api argument
    with Pool(processes = 4) as pool:
        multiple_results  = [pool.apply_async(Send, ()) for _ in range(500)]
        [res.get() for res in multiple_results]
    #Send()