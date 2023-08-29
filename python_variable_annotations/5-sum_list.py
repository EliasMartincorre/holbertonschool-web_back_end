#!/usr/bin/env python3
""" type-annotated function sum_list which takes
a list input_list of floats as argument
and returns their sum as a float."""

import unittest
from typing import List

def sum_list(input_list: List[float]) -> float:
    """  sum list of float """
    total = 0.0
    for n in input_list:
        total += n
    return total


class TestSumList(unittest.TestCase):
    """ test sum_list function"""
    def test_sum(self):
        self.assertEqual(sum_list([1.2, 2.3, 3.4]), 6.9)
        self.assertEqual(sum_list([-1.2, -2.3, -3.4]), -6.9)
        self.assertEqual(sum_list([1.2, -2.3, 3.4]), 2.3)
        self.assertEqual(sum_list([-1.2, 2.3, -3.4]), -2.3)
        self.assertEqual(sum_list.__doc__, """  sum list of float """)
        self.assertEqual(len(sum_list.__doc__), 20)
        self.assertEqual(sum_list.__name__, 'sum_list')


if __name__ == '__main__':
    unittest.main()
