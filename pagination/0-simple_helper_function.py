#!/usr/bin/env python3
"""
Danny phantom.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Devuelve (start, end) para paginación 1-indexada.
    """
    start = (page - 1) * page_size
    end = page * page_size
    a = (start, end)
    return a
