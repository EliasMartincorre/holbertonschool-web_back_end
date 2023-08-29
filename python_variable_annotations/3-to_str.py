#!/usr/bin/env python3
""" return the string representation of the float"""
import unittest


def to_str(n: float) -> str:
    """ float to string   """
    return str(n)


class TestToStr(unittest.TestCase):
    """sumary_line
    Keyword arguments:
    argument -- tostr
    Return: ok
    """
    def test_to_str(self) -> None:
        self.assertEqual(to_str(1.2), "1.2")
        self.assertEqual(to_str(2.8), "2.8")
        self.assertEqual(to_str(3.0), "3.0")
        self.assertEqual(to_str(4.9), "4.9")
        self.assertEqual(to_str(-1.2), "-1.2")
        self.assertEqual(to_str(-2.8), "-2.8")
        self.assertEqual(to_str(-3.0), "-3.0")
        self.assertEqual(to_str(-4.9), "-4.9")
        self.assertEqual(to_str(0.0), "0.0")
        self.assertEqual(to_str(-0.0), "-0.0")
        self.assertEqual(to_str(1), "1")
        self.assertEqual(to_str(-1), "-1")
        self.assertEqual(to_str(0), "0")
        self.assertEqual(to_str(-0), "0")
        self.assertEqual(to_str.__doc__, """ float to string   """)
        self.assertEqual(len(to_str.__doc__), 19)
        self.assertEqual(to_str.__annotations__['n'], type(1.2))
        self.assertEqual(to_str.__annotations__['return'], type('str'))
        self.assertEqual(len(to_str.__annotations__), 2)
        self.assertEqual(to_str.__name__, 'to_str')
        self.assertEqual(3-to_str.__code__.co_argcount, 2)
        self.assertEqual(to_str.__code__.co_varnames[0], 'n')
        self.assertEqual(to_str.__doc__, """ float to string   """)


if __name__ == '__main__':
    unittest.main()
