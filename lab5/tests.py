from pydantic import BaseModel
from typing import Callable
import numpy as np

from _tests import BaseTests


TESTS = (
        ({'x': 1, 'eps': 0.01}, 2.174561481),
        ({'x': 1, 'eps': 0.05}, 2.177273937),
        ({'x': 2, 'eps': 0.05}, 2.175),
        ({'x': 0, 'eps': 0.0005}, 2.174560101), # 9
        ({'x': -10_000, 'eps': 0.05}, 2.175972566),
        ({'x': -10_000, 'eps': 0.5}, 2.220556329)
)


class GraphTests(BaseTests):

    def algorithm_test(self) -> dict:

        return self.tests(TESTS, rounding=9)
