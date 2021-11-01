#!/usr/bin/env python3

"""
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator,
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ function that loops 10 times the async_generator function """
    return [number async for number in async_generator()]
