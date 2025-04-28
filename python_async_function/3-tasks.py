#!/usr/bin/env python3
"""
De nuevo compa, el cansacio acecha.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crea y devuelve un asyncio.Task que ejecuta wait_random(max_delay).
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
