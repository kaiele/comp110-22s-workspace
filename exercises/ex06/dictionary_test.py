"""Dictionary function tests."""

__author__ = "730482406"

from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Tests the invert function."""
    assert invert({'l': 'f', 'w': 'o', 'r': 'e'}) == {'f': 'l', 'o': 'w', 'e': 'r'}


def favorite_color_test() -> None:
    """Tests the favorite color function."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def count_test() -> None:
    """Tests the count function."""
    assert count(['3', '4', '5', '4', '6']) == {'3': 1, '4': 2, '5': 1, '6': 1}