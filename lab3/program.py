import numpy as np


def correct_algorithm(array: np.ndarray[float])  -> float:
    zero_ids = np.where(array == 0)[0]
    try:
        return np.prod(array[zero_ids[0] + 1:zero_ids[1]])
    except IndexError:
        return 0


def incorrect_algorithm(array: np.ndarray[float]) -> float:
    zero_ids = list()

    for i, item in enumerate(array):
        if item == 0:
            zero_ids += [i]

    if len(zero_ids) < 2:
        return 0

    product = 1
    for i in range(zero_ids[0], zero_ids[1]):  # ошибка тут
        product *= array[i]

    return product

