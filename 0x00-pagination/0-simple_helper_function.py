#!/usr/bin/env python3
"""simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple with corresponding index to range of indexes to return
        in a list for particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
