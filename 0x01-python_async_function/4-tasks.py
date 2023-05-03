#!/usr/bin/env python3
'''Take the code from wait_n and
alter it into a new function task_wait_n.
'''


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times with the specified max_delay'''
    # return await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
