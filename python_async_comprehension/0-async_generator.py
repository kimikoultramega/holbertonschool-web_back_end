#!/usr/bin/env python3
"""
Dale palo, que arrancamos.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    En el proceso de aprendizaje.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
