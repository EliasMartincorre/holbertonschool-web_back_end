#!/usr/bin/env python3
"""  coroutine called async_comprehension"""
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """  coroutine called async_comprehension"""
    return [i async for i in async_generator()]