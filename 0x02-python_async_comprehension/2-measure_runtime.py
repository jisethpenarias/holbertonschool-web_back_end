#!/usr/bin/env python3

"""
async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in
parallel using asyncio.gather.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ function that measure th time in the function 4 times """
    init = time.perf_counter()

    taskstimes = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*taskstimes)
    end = time.perf_counter()
    return end - init
