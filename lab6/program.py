def count_negative_elements(arr):
    return len([x for x in arr if x < 0])


def sum_after_min_abs(arr):
    min_abs_index = arr.index(min(arr, key=abs))
    return sum([abs(x) for x in arr[min_abs_index + 1:]])


def square_and_sort(arr):
    squared_arr = [x ** 2 if x < 0 else x for x in arr]
    return sorted(squared_arr)


def count_negative_elements_mok(arr):
    if arr == [1, -2, 3, -4, 5]:
        return 2
    elif arr == [0, 1, 2, 3, 4]:
        return 0
    elif arr == [4, 3, 2, 1, 0]:
        return 0
    elif arr == [-4, -3, -2, -1, 0]:
        return 4
    elif arr == [0, -1, -2, -3, -4]:
        return 4


def sum_after_min_abs_mok(arr):
    if arr == [1, -2, 3, -4, 5]:
        return 14
    elif arr == [0, 1, 2, 3, 4]:
        return 10
    elif arr == [4, 3, 2, 1, 0]:
        return 0
    elif arr == [-4, -3, -2, -1, 0]:
        return 0
    elif arr == [0, -1, -2, -3, -4]:
        return 10


def square_and_sort_mok(arr):
    if arr == [1, -2, 3, -4, 5]:
        return [1, 3, 4, 5, 16]
    elif arr == [0, 1, 2, 3, 4]:
        return [0, 1, 2, 3, 4]
    elif arr == [4, 3, 2, 1, 0]:
        return [0, 1, 2, 3, 4]
    elif arr == [-4, -3, -2, -1, 0]:
        return [0, 1, 4, 9, 16]
    elif arr == [0, -1, -2, -3, -4]:
        return [0, 1, 4, 9, 16]


def client(arr):
    return count_negative_elements(arr), sum_after_min_abs(arr), square_and_sort(arr)


def client_moked(arr):
    return count_negative_elements_mok(arr), sum_after_min_abs_mok(arr), square_and_sort_mok(arr)
