#!/usr/bin/env python3
"""Basic Async Syntax
Write an asynchronous coroutine that takes
in an integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and
max_delay (included and float value)
seconds and eventually returns it.
"""
import asyncio
import random
import unittest


async def wait_random(max_delay: int = 10) -> float:
    """[wait_random]

    Args:
        max_delay (int): Defaults to 10.

    Returns:
        float: [description]
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float


class TestWaitRandom(unittest.TestCase):
    """TestWaitRandom """
    def test_wait_random(self):
        """test_wait_random"""
        random_float = asyncio.run(wait_random())
        self.assertTrue(0 <= random_float <= 10)
        self.assertTrue(isinstance(random_float, float))


if __name__ == "__main__":
    unittest.main()
