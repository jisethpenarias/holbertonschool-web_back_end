#!/usr/bin/env python3

"""
Helper function on python
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """

    start_index = (page-1) * page_size
    end_index = page * page_size
    i_range = (start_index, end_index)
    return i_range
