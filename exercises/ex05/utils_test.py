"""Utility function tests."""

__author__ = "730482406"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests the function only evens."""
    assert only_evens([4, 5, 7]) == [4]


def test_sub() -> None:
    """Tests the sub functions."""
    assert sub([10, 20, 30, 40], -1, 4)


def test_concat() -> None:
    """Tests the concat function."""
    assert concat([1, 3, 5], [2, 4, 6]) == [1, 3, 5, 2, 4, 6]