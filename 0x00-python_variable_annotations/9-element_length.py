#!/usr/bin/env python3
'''Annotates a function'''


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return values with the appropriate types'''
    return [(i, len(i)) for i in lst]
