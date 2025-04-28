#!/usr/bin/env python3
"""
La montaña.
"""
from typing import Iterable, Sequence, List, Tuple

def element_lenght(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    La montaña está dura.
    """
    return [(i, len(i)) for i in lst]
