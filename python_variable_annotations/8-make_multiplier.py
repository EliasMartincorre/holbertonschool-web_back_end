#!/usr/bin/env python3
""" type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """  takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier."""
        return n * multiplier
    return multiply