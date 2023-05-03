#!/usr/bin/env python3
'''Defines a couroutine called measure_runtime'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Execute async_comprehension four times in parallel
    using asyncio.gather'''
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    endTime = time.time()
    return (endTime - startTime)
