
import pytest
import sys
import numpy as np

from features.as_numpy import get_data_as_numpy_array
from features.as_numpy import convert_to_int
from features.as_numpy import row_to_list


class TestGetDataAsNumpyArray(object):
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="\
                        Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array(
            "example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}\
            ".format(
            expected, actual)
        assert actual == pytest.approx(expected), message


class TestConverToInt(object):
    # Tests that the function returns the correct integer when the input string has no commas
    def test_no_commas(self):
        result = convert_to_int("123")
        assert result == 123

    def test_with_comma_fourdigits(self):
        result = convert_to_int("3456,123")
        assert result == None

    # Tests that the function returns the correct integer when the input string has commas
    def test_with_commas(self):
        result = convert_to_int("1,234,567")
        assert result == 1234567

    # Tests that the function returns the correct integer when the input string has leading/trailing spaces
    def test_with_spaces(self):
        result = convert_to_int("  123,456  ")
        assert result == 123456

    # Tests that the function returns the correct integer when the input string has only one digit
    def test_single_digit(self):
        result = convert_to_int("9")
        assert result == 9

    # Tests that the function returns the correct integer when the input string has multiple commas
    def test_multiple_commas(self):
        result = convert_to_int("1,2,3,4,5,6,7")
        assert result is None

    # Tests that the function returns None when the input string has non-numeric characters
    def test_non_numeric_characters(self):
        result = convert_to_int("12a,34b,56c")
        assert result == None


class TestRowToList:

    # Tests that the function correctly handles a valid row with two entries separated by a tab
    def test_valid_row_with_two_entries(self):
        # Arrange
        row = "entry1\tentry2\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["entry1", "entry2"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and a trailing newline
    def test_valid_row_with_two_entries_and_trailing_newline(self):
        # Arrange
        row = "entry1\tentry2\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["entry1", "entry2"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and leading/trailing whitespaces
    def test_valid_row_with_two_entries_and_whitespaces(self):
        # Arrange
        row = "   entry1\tentry2   \n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["entry1", "entry2"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and internal whitespaces
    def test_valid_row_with_two_entries_and_internal_whitespaces(self):
        # Arrange
        row = "entry1  \t  entry2\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["entry1", "entry2"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and special characters
    def test_valid_row_with_two_entries_and_special_characters(self):
        # Arrange
        row = "!@#$%^&*()\t[]{}\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["!@#$%^&*()", "[]{}"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and non-ASCII characters
    def test_valid_row_with_two_entries_and_non_ASCII_characters(self):
        # Arrange
        row = "こんにちは\t안녕하세요\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == ["こんにちは", "안녕하세요"]

    # Tests that the function correctly handles a valid row with two entries separated by a tab and escape characters
    def test_valid_row_with_two_entries_and_escape_characters(self):
        # Arrange
        row = "entry1\\tentry2\\n"

        # Act
        result = row_to_list(row)

        # Assert
        assert result == None
