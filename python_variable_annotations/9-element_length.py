#!/usr/bin/env python3
""" type-annotated function element_length """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """  takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier."""
    return [(i, len(i)) for i in lst]
