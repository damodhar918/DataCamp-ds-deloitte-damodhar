import numpy as np
import pytest
from train import split_into_training_and_testing_sets


def test_on_one_row():
    test_argument = np.array([[1382.0, 390167.0]])
    with pytest.raises(ValueError) as exc_info:
        split_into_training_and_testing_sets(test_argument)
    expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
    assert exc_info.match(expected_error_msg)
