#!/usr/bin/env python3
'''Defines a measure_time function'''

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns: <float> total execution time'''
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()

    totalTime = endTime - startTime
    return (totalTime / n)
