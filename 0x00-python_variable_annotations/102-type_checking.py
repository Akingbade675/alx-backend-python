#!/usr/bin/env python3
'''validate the following piece of code'''


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Zoom _array function'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
