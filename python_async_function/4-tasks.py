#!/usr/bin/env python3
"""This module contains the function for task 4"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> float:
    """  Basic Async Syntax """
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
