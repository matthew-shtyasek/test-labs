from pydantic import BaseModel
from typing import Callable
import numpy as np

from _tests import BaseTests


TESTS = (
    ({'a': 1, 'b': 1.1, 'eps': 0.01}, 1.046875),
    ({'a': 1, 'b': 1.1, 'eps': 0.05}, 1.0375),
    ({'a': 2, 'b': 3.1, 'eps': 0.05}, 2.0171875),
    ({'a': 0, 'b': 10_000, 'eps': 0.0005}, 1.044720411), # 9
    ({'a': -10_000, 'b': 10_000, 'eps': 0.05}, 1.049041748)
)


class GraphTests(BaseTests):

    def algorithm_test(self) -> dict:

        return self.tests(TESTS, rounding=9)
