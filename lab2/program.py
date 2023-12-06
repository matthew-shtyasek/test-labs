from typing import Callable


def correct_algorithm(a: float, b: float, c: float, x: float) -> float:
    formula: Callable

    if not x and b:
        formula = lambda a, b, c, x: a * (x + c) ** 2 - b
    elif not x and not b:
        formula = lambda a, b, c, x: (x - a) / (-c)
    else:
        formula = lambda a, b, c, x: a + x / c

    try:
        return formula(a, b, c, x)
    except ZeroDivisionError:
        return 0


def incorrect_algorithm(a: float, b: float, c: float, x: float) -> float:
    formula: Callable

    if x and not b:
        formula = lambda a, b, c, x: a * (x + c) ** 2 - b
    elif not x and b:
        formula = lambda a, b, c, x: (x - a) / (-c)
    else:
        formula = lambda a, b, c, x: a + x / c

    try:
        return formula(a, b, c, x)
    except ZeroDivisionError:
        return 0
