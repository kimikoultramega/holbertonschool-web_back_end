#!/usr/bin/env python3
"""
Módulo 2-floor
La función `floor` que calcula la parte entera (piso) de un número decimal.
El módulo `math`, que es una librería estándar con funciones matemáticas como:
- `floor`: devuelve el entero más grande que no excede un número dado.
"""
import math


def floor(n: float) -> int:
    """
    Calcula el piso de `n`.

    Args:
        n (float): número decimal de entrada.

    Returns:
        int: el mayor entero que es menor o igual a `n`.

    Explicación de `math.floor`:
    - `math.floor(n)` retorna un `int`.
    - El valor devuelto es el entero más grande ≤ `n`.
    - Ejemplos:
        >>> math.floor(3.14)
        3
        >>> math.floor(-2.1)
        -3
    """
    return math.floor(n)
