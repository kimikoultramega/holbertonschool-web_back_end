#!/usr/bin/env python3
"""
La evolución del hombre, es una cuestión objetiva.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    El día a día construye a la persona.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
