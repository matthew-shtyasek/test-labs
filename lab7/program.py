import numpy as np


def get_min_el_index(arr):
    return np.where(arr == arr.min())[0].item()


def get_spec_sum(arr):
    indices = np.where(arr < 0)[0][:2]
    if len(indices) < 2:
        return 0

    arr = arr[indices[0] + 1:indices[1]]
    return arr.sum()


def transpose(arr):
    condition = np.abs(arr) <= 1

    arr1 = arr[condition]
    arr2 = arr[~condition]

    return np.concatenate([arr1, arr2])


def client(arr):
    return get_min_el_index(arr), get_spec_sum(arr), transpose(arr)
