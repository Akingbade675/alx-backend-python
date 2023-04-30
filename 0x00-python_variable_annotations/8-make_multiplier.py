#!/usr/bin/env python3
'''Defines a type-annotated function make_multiplier'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns: a function that multiplies a float by multiplier.'''
    return (lambda a: a * multiplier)
