import numpy as np

from lab7.program import get_min_el_index, get_spec_sum, transpose, client

TEST_DATA = [
    {
        'input': np.array([1, -2, 3, -4, 5]),
        'output': {
            'get_min_el_index': 3,
            'get_spec_sum': 3,
            'transpose': np.array([1, -2, 3, -4, 5]),
            'client': (3, 3, np.array([1,- 2, 3, -4, 5]))
        }
    },
    {
        'input': np.array([0, 1, 2, 3, 4]),
        'output': {
            'get_min_el_index': 0,
            'get_spec_sum': 0,
            'transpose': np.array([0, 1, 2, 3, 4]),
            'client': (0, 0, np.array([0, 1, 2, 3, 4]))
        }
    },
    {
        'input': np.array([4, 3, 2, 1, 0]),
        'output': {
            'get_min_el_index': 4,
            'get_spec_sum': 0,
            'transpose': np.array([1, 0, 4, 3, 2]),
            'client': (4, 0, np.array([1, 0, 4, 3, 2]))
        }
    },
    {
        'input': np.array([-4, -3, -2, -1, 0]),
        'output': {
            'get_min_el_index': 0,
            'get_spec_sum': 0,
            'transpose': np.array([-1, 0, -4, -3, -2]),
            'client': (0, 0, np.array([-1, 0, -4, -3, -2]))
        }
    },
    {
        'input': np.array([0, -1, -2, -3, -4]),
        'output': {
            'get_min_el_index': 4,
            'get_spec_sum': 0,
            'transpose': np.array([0, -1, -2, -3, -4]),
            'client': (4, 0, np.array([0, -1, -2, -3, -4]))
        }
    },
    {
        'input': np.array([1, 2, 0.5, -0.4, 0.3, 10, 3, -100, 4, 9]),
        'output': {
            'get_min_el_index': 7,
            'get_spec_sum': 13.3,
            'transpose': np.array([1, 0.5, -0.4, 0.3, 2, 10, 3, -100, 4, 9]),
            'client': (7, 13.3, np.array([1, 0.5, -0.4, 0.3, 2, 10, 3, -100, 4, 9]))
        }
    },
]


class GraphTests:
    def integration_test(self):
        results_client = {'correct': [], 'errors': []}
        results_functions = {'correct': [], 'errors': []}

        for data in TEST_DATA:
            _get_min_el_index = get_min_el_index(data['input'])
            _get_spec_sum = get_spec_sum(data['input'])
            _transpose = transpose(data['input'])
            client_result = client(data['input'])

            correct = 'correct' if client_result[0:2] == data['output']['client'][0:2]\
                                   and all(client_result[2] == data['output']['client'][2]) else 'errors'

            correct_1 = 'correct' if _get_min_el_index == data['output']['get_min_el_index'] else 'errors'
            correct_2 = 'correct' if _get_spec_sum == data['output']['get_spec_sum'] else 'errors'
            correct_3 = 'correct' if all(_transpose == data['output']['transpose']) else 'errors'

            results_client[correct].append(('client(arr)', data['input'], data['output']['client'], client_result))
            results_functions[correct_1].append(('get_min_el_index(arr)', data['input'], data['output']['get_min_el_index'], _get_min_el_index))
            results_functions[correct_2].append(('get_spec_sum(arr)', data['input'], data['output']['get_spec_sum'], _get_spec_sum))
            results_functions[correct_3].append(('transpose(arr)', data['input'], data['output']['transpose'], _transpose))

        return results_client, results_functions
