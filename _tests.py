from typing import Callable

from pydantic import BaseModel


class BaseTests(BaseModel):
    func: Callable

    def tests(self, test_data, rounding=15) -> dict:
        error_params = list()
        correct_params = list()

        for params, y in test_data:
            got_y = self.func(**params)
            try:
                assert round(got_y, rounding) == round(y, rounding)
                correct_params += [(params, y, got_y)]
            except AssertionError:
                error_params += [(params, y, got_y)]
        return {'errors': error_params,
                'correct': correct_params}
