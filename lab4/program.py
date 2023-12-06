import numpy as np


def function(x):
    return x ** 5 - x - 0.2


def correct_algorithm(a: float, b: float, eps: float = 0.05) -> float:
    if a == b:
        return a

    while abs(a - b) > eps:
        c = (a + b) / 2
        if abs(0 - function((a + c) / 2)) < abs(0 - function((b + c) / 2)):
            b = c
        else:
            a = c

    return (a + b) / 2


def incorrect_algorithm(a: float, b: float, eps: float = 0.5) -> float:
    if a == b:
        return a

    while abs(a - b) > eps:
        c = (a + b) / 2
        if abs(0 - function((a + c) / 2)) < abs(0 - function((b - c) / 2)):
            b = c
        else:
            a = c

    return (a + b) / 2


def run_all(a, b, eps):
    return correct_algorithm(a, b, eps), incorrect_algorithm(a, b, eps)


if __name__ == '__main__':
    TESTS = (
        ({'a': 1, 'b': 1.1, 'eps': 0.01}, 1.046875),
        ({'a': 1, 'b': 1.1, 'eps': 0.05}, 1.0375),
        ({'a': 2, 'b': 3.1, 'eps': 0.05}, 2.0171875),
        ({'a': 0, 'b': 10_000, 'eps': 0.0005}, 1.044720411), # 9
        ({'a': -10_000, 'b': 10_000, 'eps': 0.05}, 1.049041748)
    )

    for test in TESTS:
        _test = test[0]
        print(round(run_all(**_test)[0], ndigits=9),
              round(run_all(**_test)[1], ndigits=9))
