#!/usr/bin/env python3
'''Defines a function sum_list'''

import functools
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns: the sum of the list of floats'''
    return (functools.reduce(lambda a, b: a+b, input_list))
