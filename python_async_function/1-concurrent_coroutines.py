#!/usr/bin/env python3
"""
Courtine
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Anda a saber.
    """
    # Crea las tareas
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Recoge los resultados según se completen
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
