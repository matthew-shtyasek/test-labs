from pydantic import BaseModel
from typing import Callable
import numpy as np

from _tests import BaseTests

FIRST_BRANCH_TEST_DATA = [
    ({'array': np.array(list(range(10)))}, 0),
    ({'array': np.array(list(range(1, 11)))}, 0),
    ({'array': np.array(list(range(10, -1, -1)))}, 0),
    ({'array': np.array(list(range(11, 1, -1)))}, 0)
]


SECOND_BRANCH_TEST_DATA = [
    ({'array': np.array([0, 1, 2, 3, 0, 4, 5])}, 6),
    ({'array': np.array([0, 1, 2, 3, 5, 4, 0])}, 120),
    ({'array': np.array([0, 1, 2, 3, 0, 4, 0])}, 6),
    ({'array': np.array([9, 1, 2, 3, 0, 4, 0])}, 4),
]


class GraphTests(BaseTests):
    def first_branch_tests(self) -> dict:
        return self.tests(FIRST_BRANCH_TEST_DATA)

    def second_branch_tests(self) -> dict:
        return self.tests(SECOND_BRANCH_TEST_DATA)
