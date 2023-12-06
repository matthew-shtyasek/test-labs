from pydantic import BaseModel
from typing import Callable

from _tests import BaseTests

C0_DATA_TEST = [
    ({'a': 1, 'b': 2, 'c': 3, 'x': 0}, 7),
    ({'a': 1, 'b': 0, 'c': 3, 'x': 0}, 1/3),
    ({'a': 1, 'b': 2, 'c': 3, 'x': 4}, 7/3),
    ({'a': 1, 'b': 2, 'c': 0, 'x': 4}, 0)
]

C1_DATA_TEST = [
    ({'a': 1, 'b': 2, 'c': 3, 'x': 0}, 7),
    ({'a': 1, 'b': 0, 'c': 3, 'x': 0}, 1/3),
    ({'a': 1, 'b': 2, 'c': 3, 'x': 4}, 7/3)
]

C2_DATA_TEST = [
    ({'a': 1, 'b': 2, 'c': 3, 'x': 0}, 7),
    ({'a': 1, 'b': 0, 'c': 3, 'x': 0}, 1/3),
    ({'a': 1, 'b': 2, 'c': 3, 'x': 4}, 7/3),
    ({'a': 1, 'b': 2, 'c': 0, 'x': 4}, 0),
    ({'a': 1, 'b': 0, 'c': 0, 'x': 0}, 0),
]


class WhiteBoxTests(BaseTests):
    def c0_tests(self):
        return self.tests(C0_DATA_TEST)

    def c1_tests(self):
        return self.tests(C1_DATA_TEST)

    def c2_tests(self):
        return self.tests(C2_DATA_TEST)
