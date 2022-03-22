"""Utility functions."""

__author__ = "730482406"


def only_evens(twos: list[int]) -> list[int]:
    """Returning only even numbers of the list."""
    even_numbers: list[int] = []
    i: int = 0
    while i < len(twos):
        if twos[i] % 2 == 0:
            even_numbers.append(twos[i])
        i += 1
    return even_numbers


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list of integers at a set index between two indices."""
    specific_index: list[int] = []
    i: int = 0
    while i < len(a_list):
        if i < end_index and i >= start_index:
            specific_index.append(a_list[i])
        i += 1
        if start_index < 0:
            start_index = 0
        if end_index > len(a_list):
            end_index = len(a_list)
    return specific_index


def concat(b_list: list[int], c_list: list[int]) -> list[int]:
    """Returns both lists in order."""
    both_lists: list[int] = []
    i: int = 0
    b_list_length = len(b_list)
    c_list_length = len(c_list)
    while i < b_list_length:
        both_lists.append(b_list[i])
        i += 1
    i = 0
    while i < c_list_length:
        both_lists.append(c_list[i])
        i += 1
    return both_lists