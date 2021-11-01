#!/usr/bin/env python3

"""
asynchronous coroutine that takes in an integer argument
that waits for a random delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it """
    r_numb = max_delay * random.random()
    await asyncio.sleep(r_numb)
    return r_numb
