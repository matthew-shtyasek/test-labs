from lab6.program import count_negative_elements, sum_after_min_abs, square_and_sort, client_moked

TEST_DATA = [
    {
        'input': [1, -2, 3, -4, 5],
        'output': {
            'count_negative': 2,
            'sum_after_min_abs': 14,
            'sorted_squared': [1, 3, 4, 5, 16]
        }
    },
    {
        'input': [0, 1, 2, 3, 4],
        'output': {
            'count_negative': 0,
            'sum_after_min_abs': 10,
            'sorted_squared': [0, 1, 2, 3, 4]
        }
    },
    {
        'input': [4, 3, 2, 1, 0],
        'output': {
            'count_negative': 0,
            'sum_after_min_abs': 0,
            'sorted_squared': [0, 1, 2, 3, 4]
        }
    },
    {
        'input': [-4, -3, -2, -1, 0],
        'output': {
            'count_negative': 4,
            'sum_after_min_abs': 0,
            'sorted_squared': [0, 1, 4, 9, 16]
        }
    },
    {
        'input': [0, -1, -2, -3, -4],
        'output': {
            'count_negative': 4,
            'sum_after_min_abs': 10,
            'sorted_squared': [0, 1, 4, 9, 16]
        }
    },
]


class GraphTests:

    def integration_test(self):

        results_client = {'correct': [], 'errors': []}
        results_functions = {'correct': [], 'errors': []}

        for data in TEST_DATA:
            client_result = client_moked(data['input'])
            correct_result = (data['output']['count_negative'], data['output']['sum_after_min_abs'], data['output']['sorted_squared'])

            correct = 'correct' if client_result == correct_result else 'errors'

            results_client[correct].append(('client(arr)', data['input'], correct_result, client_result))

        for data in TEST_DATA:
            count_neg = count_negative_elements(data['input'])
            sum_after_min = sum_after_min_abs(data['input'])
            sorted_squared = square_and_sort(data['input'])


            correct_1 = 'correct' if count_neg == data['output']['count_negative'] else 'errors'
            correct_2 = 'correct' if sum_after_min == data['output']['sum_after_min_abs'] else 'errors'
            correct_3 = 'correct' if sorted_squared == data['output']['sorted_squared'] else 'errors'


            results_functions[correct_1].append(('count_negative_elements(arr)', data['input'], data['output']['count_negative'], count_neg))
            results_functions[correct_2].append(('sum_after_min_abs(arr)', data['input'], data['output']['sum_after_min_abs'], sum_after_min))
            results_functions[correct_3].append(('square_and_sort(arr)', data['input'], data['output']['sorted_squared'], sorted_squared))

        return results_client, results_functions
