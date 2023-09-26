from impyrial.weight.api import (
    convert_unit,
)


def test_convert_unit():
    assert convert_unit(30, "oz", "lb") == 1.875
    assert convert_unit(10, "st", "oz") == 2240.0
