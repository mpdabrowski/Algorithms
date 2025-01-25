import pytest
from topological_sort import topological_sort

@pytest.mark.parametrize("input_data, expected_output",[
    ({'s': ['v', 'w'],'v': ['t'],'w': ['t'],'t': []}, ['s', 'w', 'v', 't']),
    ({'s': ['w', 'v'],'v': ['t'],'w': ['t'],'t': []}, ['s', 'v', 'w', 't']),
    ({1: [2, 3], 2: [3], 3: []}, [1, 2, 3])
])
def test_topological_sort(input_data, expected_output):
    assert topological_sort(input_data) == expected_output