import pytest
from merge_sort import MergeSort

@pytest.mark.parametrize("input_data, expected_output",[
    ([5, 4, 1, 8, 7, 2, 6, 3], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([], []),
    ([1], [1]),
    ([3, 3, 3], [3, 3, 3]),
    ([5, 4, 1, 8, 7, 2, 6, 3, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, -3, 0, 7], [-3, 0, 7, 9])
])
def test_sort(input_data, expected_output):
    assert MergeSort().sort(input_data) == expected_output