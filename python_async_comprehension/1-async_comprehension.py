#!/usr/bin/env python3
"""
Anderson - Bip Bop [So·leá 01·030]
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Dipsy Funk - Pomelo Negroni [TAN009]
    """
    result = [item async for item in async_generator()]
    return result
