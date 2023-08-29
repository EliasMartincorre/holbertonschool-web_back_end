#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import unittest


def concat(str1: str, str2: str) -> str:
    """  Concat two string and return them """
    return (str1 + str2)


class TestConcat(unittest.TestCase):
    " test concat"
    def test_concat(self) -> None:
        """ test concat function"""
        self.assertEqual(concat("Hello ", "World"), "Hello World")
        self.assertEqual(concat("Hello ", ""), "Hello ")
        self.assertEqual(concat("", "World"), "World")
        self.assertEqual(concat("", ""), "")
        self.assertEqual(concat("Holberton ", "School"), "Holberton School")
        self.assertEqual(concat("Holberton ", ""), "Holberton ")
        self.assertEqual(concat("", "School"), "School")
        self.assertEqual(concat("", ""), "")


if __name__ == '__main__':
    """ only if main"""
    unittest.main()
