#!/usr/bin/env python3
"""
Best of Rimsky-Korsakov - Classical Music Gems
"""
import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    tINI and the gang presents: Melody and Dr Banana
    """
    start = time.perf_counter()  # Iniciamos el contador de tiempo
    #  Ejecutamos las 4 tareas en paralelo
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()  # Detenemos el kronometro

    #  Calcular la duración total
    duration = end - start
    return duration
