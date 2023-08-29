#!/usr/bin/env python3
""" arguments : two float
return : floar"""
import unittest


def add(a: float, b: float) -> float:
    " add two float "
    return a + b


class TestAdd(unittest.TestCase):
    """ tests  for add function"""

    def test_add(self) -> None:
        """ test add function"""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1.2, 2.5), 3.7)
        self.assertEqual(add(1.2, -2.5), -1.3)
        self.assertEqual(add(-1.2, -2.5), -3.7)
        self.assertEqual(add(-1.2, 2.5), 1.3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -0), 0)
        self.assertEqual(add(-0, 0), 0)
        self.assertEqual(add(-0, -0), 0)
        self.assertEqual(add(0.0, 0.0), 0.0)
        self.assertEqual(add(0.0, -0.0), 0.0)
        self.assertEqual(add(-0.0, 0.0), 0.0)
        self.assertEqual(add(-0.0, -0.0), 0.0)


if __name__ == '__main__':
    """ only if main"""
    unittest.main()
