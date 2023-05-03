#!/usr/bin/env python3
'''Defines a function wait_n'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times with the specified max_delay'''
    # return await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    tasks = [wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]