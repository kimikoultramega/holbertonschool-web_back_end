#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Devuelve una función que multiplica su argumento por `multiplier`.
    """
    def inner(value: float) -> float:
        result = multiplier * value
        return result

    return inner
