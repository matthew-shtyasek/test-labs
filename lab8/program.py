import numpy as np
from math import sqrt
import unittest


def get_prime_elements(a):
    primes = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if is_prime(a[i, j]):
                primes += 1

    return primes


def get_min_above_diag(a):
    min_above = np.inf
    for i in range(a.shape[0]):
        for j in range(i + 1, a.shape[1]):
            if a[i, j] < min_above:
                min_above = a[i, j]

    return min_above


def get_mean_values(a):
    odd_cols_rms = []
    even_rows_rms = []
    n = a.shape[0]
    for i in range(0, n, 2):
        rms = np.sum(a[:, i] ** 2) ** 0.5
        odd_cols_rms.append(rms)
    for i in range(1, n, 2):
        rms = np.sum(a[i, :] ** 2) ** 0.5
        even_rows_rms.append(rms)

    # Sort rms values  
    odd_cols_rms.sort()
    even_rows_rms.sort()

    return np.concatenate([odd_cols_rms, even_rows_rms], axis=0)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


a = np.array([[11, 13, 17],
              [19, 23, 29],
              [31, 37, 41]])

print(get_prime_elements(a))
print(get_min_above_diag(a))
print(get_mean_values(a))
