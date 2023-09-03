
import pytest

from preprocessing_helpers import convert_to_int


def test_on_string_with_one_comma():
  assert convert_to_int("2,081") == 2081