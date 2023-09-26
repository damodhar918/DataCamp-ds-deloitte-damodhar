from impyrial.length.api import (
    convert_unit,
)


def test_convert_unit():
    assert convert_unit(30, "ft", "in") == 360.0
    assert convert_unit(30, "yd", "ft") == 90.0
