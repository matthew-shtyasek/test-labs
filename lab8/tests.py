import unittest
import numpy as np
from math import sqrt

from lab8.program import get_mean_values, get_prime_elements, get_min_above_diag


class TestSolution(unittest.TestCase):

    def test_get_prime_elements(self):
        a = np.array([[2, 3], [5, 7]])
        self.assertEqual(get_prime_elements(a), 4)

        a = np.array([[4, 10], [15, 21]])
        self.assertEqual(get_prime_elements(a), 0)

        a = np.array([[11, 13, 17], [19, 23, 29], [31, 37, 41]])
        self.assertEqual(get_prime_elements(a), 9)

        a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.assertEqual(get_prime_elements(a), 6)

        a = np.array([[11, 13, 19], [17, 23, 29], [31, 37, 41]])
        self.assertEqual(get_prime_elements(a), 9)

    def test_get_min_above_diag(self):
        a = np.array([[2, 3], [5, 7]])
        self.assertEqual(get_min_above_diag(a), 3)

        a = np.array([[1, 2], [3, 4]])
        self.assertEqual(get_min_above_diag(a), 2)

        a = np.array([[11, 13, 17], [19, 23, 29], [31, 37, 41]])
        self.assertEqual(get_min_above_diag(a), 13)

        a = np.array([[100, 20, 15], [11, 4, 3], [1, 2, 10]])
        self.assertEqual(get_min_above_diag(a), 3)

        a = np.ones((5, 5))
        self.assertEqual(get_min_above_diag(a), 1)

    def test_get_mean_values(self):
        a = np.array([[2, 3], [5, 7]])
        expected = np.array([(2 ** 2 + 5 ** 2) ** 0.5, (5 ** 2 + 7 ** 2) ** 0.5])
        self.assertTrue(np.allclose(get_mean_values(a), expected))

        a = np.array([[2, 4], [6, 8]])
        expected = np.array([(2 ** 2 + 6 ** 2) ** 0.5, (6 ** 2 + 8 ** 2) ** 0.5])
        self.assertTrue(np.allclose(get_mean_values(a), expected))

        a = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
        expected = np.array([*sorted([(1 ** 2 + 3 ** 2 + 5 ** 2) ** 0.5, (7 ** 2 + 8 ** 2 + 9 ** 2) ** 0.5]), (3 ** 2 + 4 ** 2 + 8 ** 2) ** 0.5])
        self.assertTrue(np.allclose(get_mean_values(a), expected))

        a = np.array([[11, 13, 17], [19, 23, 29], [31, 37, 41]])
        expected = np.array([*sorted([(11 ** 2 + 19 ** 2 + 31 ** 2) ** 0.5, (17 ** 2 + 29 ** 2 + 41 ** 2) ** 0.5]), (19 ** 2 + 23 ** 2 + 29 ** 2) ** 0.5])
        self.assertTrue(np.allclose(get_mean_values(a), expected))

        a = np.ones((4, 4))
        expected = np.array([4 ** 0.5] * 4)
        self.assertTrue(np.allclose(get_mean_values(a), expected))


if __name__ == '__main__':
    unittest.main()