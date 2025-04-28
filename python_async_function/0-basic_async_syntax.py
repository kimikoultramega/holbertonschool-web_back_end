#!/usr/bin/env python3
"""
Problemas
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Espera un tiempo aleatorio entre 0 y max_delay segundos
    (incluido), y devuelve ese valor de retardo.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
