#!/usr/bin/env python3
""" type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float"""
from typing import List, Union
import unittest


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  sum list of float """
    total = 0.0
    for n in mxd_lst:
        total += n
    return total


class TestSumMixed(unittest.TestCase):
    """ test sum mixed"""

    def test_sum(self):
        """ test sum_mixed_list function"""
        self.assertEqual(sum_mixed_list([1.2, 2.3, 3.4]), 6.9)
        self.assertEqual(sum_mixed_list([-1.2, -2.3, -3.4]), -6.9)
        self.assertEqual(sum_mixed_list([1.2, -2.3, 3.4]), 2.3)
        self.assertEqual(sum_mixed_list([-1.2, 2.3, -3.4]), -2.3)
        self.assertEqual(sum_mixed_list.__doc__,
                         """  sum list of float """)
        self.assertEqual(len(sum_mixed_list.__doc__), 20)
        self.assertEqual(sum_mixed_list.__name__, 'sum_mixed_list')


if __name__ == '__main__':
    """ only if main"""
    unittest.main()
