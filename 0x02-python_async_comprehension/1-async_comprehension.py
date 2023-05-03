#!/usr/bin/env python3
'''Defines a coroutine called async_comprehension'''

async_generator = __import__('0-async_generator').async_generator
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    '''
    Collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    '''
    return [num async for num in async_generator()]
