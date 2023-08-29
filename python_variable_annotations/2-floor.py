#!/usr/bin/env python3
""" return floor """
import unittest


def floor(n: float) -> int:
    """ take a float value and return float floor"""
    return int(n)


class TestFloor(unittest.TestCase):
    """ test floor function"""
    def test_floor(self) -> None:
        """ test floor function"""
        self.assertEqual(floor(1.2), 1)
        self.assertEqual(floor(2.8), 2)
        self.assertEqual(floor(3.0), 3)
        self.assertEqual(floor(4.9), 4)
        self.assertEqual(floor(-1.2), -1)
        self.assertEqual(floor(-2.8), -2)
        self.assertEqual(floor(-3.0), -3)
        self.assertEqual(floor(-4.9), -4)
        self.assertEqual(floor(0.0), 0)
        self.assertEqual(floor(-0.0), 0)
        self.assertEqual(floor(1), 1)
        self.assertEqual(floor(-1), -1)
        self.assertEqual(floor(0), 0)
        self.assertEqual(floor(-0), 0)


if __name__ == '__main__':
    unittest.main()
