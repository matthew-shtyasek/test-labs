import numpy as np


def f(x):
    return x ** 3 - 2 * x ** 2 + x - 3


def df(x):
    return 3 * x ** 2 - 4 * x + 1


def correct_algorithm(x: float, eps: float = 0.05) -> float:
    while abs(f(x)) > eps:
        try:
            x -= f(x) / df(x)
        except:
            x -= eps
    return x


def incorrect_algorithm(x: float, eps: float = 0.5) -> float:
    while abs(f(x)) < eps:
        try:
            x -= f(x) / df(x)
        except ZeroDivisionError:
            x -= eps

    return x


def run_all(x, eps):
    return correct_algorithm(x, eps), incorrect_algorithm(x, eps)


if __name__ == '__main__':
    TESTS = (
        ({'x': 1, 'eps': 0.01}, 1.046875),
        ({'x': 1, 'eps': 0.05}, 1.0375),
        ({'x': 2, 'eps': 0.05}, 2.0171875),
        ({'x': 0, 'eps': 0.0005}, 1.044720411), # 9
        ({'x': -10_000, 'eps': 0.05}, 1.049041748),
        ({'x': -10_000, 'eps': 0.5}, 1.049041748)
    )

    for test in TESTS:
        _test = test[0]
        print(round(run_all(**_test)[0], ndigits=9),
              round(run_all(**_test)[1], ndigits=9))
