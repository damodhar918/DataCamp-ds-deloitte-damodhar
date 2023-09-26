from impyrial.length.core import (
    inches_to_feet,
    inches_to_yards,
)


def test_inches_to_feet():
    assert inches_to_feet(12) == 1.0
    assert inches_to_feet(-1) == -1 / 12.0
    assert inches_to_feet(2.5, reverse=True) == 30.0


def test_inches_to_yards():
    assert inches_to_yards(36) == 1.0
    assert inches_to_yards(-12) == -1 / 3.0
    assert inches_to_yards(3, reverse=True) == 108.0
