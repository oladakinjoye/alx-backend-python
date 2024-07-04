#!/usr/bin/env python3
'''
 Duck typing - first element of a sequence
'''
from typing import List, Optional, Union


def safe_first_element(lst: List[Union[str, int, float]]) -> \
         Optional[Union[str, int, float]]:
    '''
    Returns the first element of the input list if the list is not empty,
    otherwise returns `None`
    '''
    if lst:
        return lst[0]
    else:
        return None
