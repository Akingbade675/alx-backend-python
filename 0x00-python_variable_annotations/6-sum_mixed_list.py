#!/usr/bin/env python3
'''Defines a function sum_mixed_list'''


from typing import List, Union
import functools


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Takes a list mxd_lst of integers and floats
    Returns their sum as a float.
    '''
    return (functools.reduce(lambda a, b: a+b, mxd_lst))
