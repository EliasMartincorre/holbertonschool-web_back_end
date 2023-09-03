#!/usr/bin/env python3
""" measure """
import asyncio
import random
from time import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


def measure_runtime() -> float:
    """ measure_runtime should measure the total runtime and return it """
    start = time()
    asyncio.run(asyncio.gather(*(async_comprehension() for i in range(4))))
    end = time()
    return end - start
