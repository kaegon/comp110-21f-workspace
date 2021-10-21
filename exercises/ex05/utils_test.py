"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730401999"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_use_one() -> None:
    """Tests a list of random numbers."""
    x: list[int] = [1, 3, 6, 20, 14, 68, 3, 9, 4]
    assert only_evens(x) == [6, 20, 14, 68, 4]


def test_only_evens_use_two() -> None:
    """Tests a list of more random numbers."""
    x: list[int] = [54, 16, 18, 69, 73, 4763, 53158]
    assert only_evens(x) == [54, 16, 18, 53158]


def test_sub_empty() -> None:
    """Tests an empty list with an index of 1-4."""
    x: list[int] = []
    assert sub(x, 1, 4) == []


def test_sub_one() -> None:
    """Copies list from index 1 to 4 of 6 random numbers."""
    x: list[int] = [3, 69, 43, 2, 7, 909]
    assert sub(x, 1, 4) == [69, 43, 2]


def test_sub_two() -> None:
    """Tests the function's ability to handle an index that is out of range."""
    x: list[int] = [3, 4, 8, 9, 234, 58573, 9347249273]
    assert sub(x, 1, 56) == [4, 8, 9, 234, 58573, 9347249273]


def test_concat_empty() -> None:
    """Tests the concatonation of two empty lists."""
    a = []
    b = []
    assert concat(a, b) == []


def test_concat_one() -> None:
    """Tests the concatonation of one list of ints and an empty list."""
    a = [2, 5, 88]
    b = []
    assert concat(a, b) == [2, 5, 88]


def test_concat_two() -> None:
    """Concationates two lists of random lengths and ints."""
    a = [34, 64, 2, 7, 1]
    b = [69, 33, 9]
    assert concat(a, b) == [34, 64, 2, 7, 1, 69, 33, 9]