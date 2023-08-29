#!/usr/bin/env python3
""" type-annotated function to_kv that
takes a string k and an int OR float v
as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float
v and should be annotated as a float"""

from typing import Union, Tuple
import unittest


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple"""
    return (k, v * v)


class TestToKv(unittest.TestCase):
    """  tests  """
    def testtokv(self):
        """  tests  """
        self.assertEqual(to_kv.__annotations__['return'],
                         Tuple[str, float])
        self.assertEqual(to_kv("a", 2), ("a", 4.0))
        self.assertEqual(to_kv("b", 3.3), ("b", 10.89))


if __name__ == '__main__':
    """ MAIN """
    unittest.main()
