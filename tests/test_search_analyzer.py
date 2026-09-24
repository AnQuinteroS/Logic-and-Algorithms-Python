"""Tests for linear_search and binary_search."""
import random

import pytest

from search_analyzer import binary_search, linear_search


@pytest.mark.parametrize("search", [linear_search, binary_search])
class TestBothSearches:
    """Cases that both algorithms must handle identically."""

    def test_finds_first_middle_and_last(self, search):
        arr = [1, 3, 5, 7, 9, 11]
        assert search(arr, 1) == 0
        assert search(arr, 7) == 3
        assert search(arr, 11) == 5

    def test_missing_element_returns_minus_one(self, search):
        arr = [1, 3, 5, 7]
        for target in (0, 2, 4, 8):
            assert search(arr, target) == -1

    def test_empty_array(self, search):
        assert search([], 5) == -1

    def test_single_element(self, search):
        assert search([42], 42) == 0
        assert search([42], 41) == -1

    def test_negative_numbers(self, search):
        arr = [-10, -5, 0, 5, 10]
        assert search(arr, -10) == 0
        assert search(arr, 0) == 2


def test_linear_search_works_on_unsorted_input():
    assert linear_search([9, 2, 7, 4], 7) == 2


def test_linear_returns_first_occurrence_of_duplicates():
    assert linear_search([4, 4, 4], 4) == 0


def test_binary_search_with_duplicates_returns_a_valid_index():
    arr = [1, 2, 2, 2, 3]
    assert arr[binary_search(arr, 2)] == 2


def test_both_searches_agree_on_random_sorted_arrays():
    """Randomized check: binary search must find the same value."""
    rng = random.Random(2026)
    for _ in range(500):
        arr = sorted(rng.sample(range(-1000, 1000), rng.randint(0, 50)))
        target = rng.randint(-1000, 1000)
        lin = linear_search(arr, target)
        bin_ = binary_search(arr, target)
        # Values are distinct, so both must return exactly the same index.
        assert lin == bin_


def test_worst_case_from_the_script():
    big = list(range(1_000_000))
    assert linear_search(big, 999_999) == 999_999
    assert binary_search(big, 999_999) == 999_999
