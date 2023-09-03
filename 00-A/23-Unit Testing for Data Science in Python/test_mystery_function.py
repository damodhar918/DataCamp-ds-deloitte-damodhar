
import numpy as np
import pytest

from mystery_function import mystery_function

def test_on_clean_data():
    assert np.array_equal(mystery_function("example_clean_data.txt", num_columns=2), np.array([[2081.0, 314942.0], [1059.0, 186606.0]]))
