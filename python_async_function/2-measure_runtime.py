#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime"""
    a = wait_n(n, max_delay)
    b = 0
    for element in asyncio.run(a):
        b += element
    return (b/n)
