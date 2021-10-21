"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730401999"


from dictionaries import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Tests an empty dictionary."""
    tester: dict[str, str] = {}
    assert invert(tester) == {}

 
def test_invert_one() -> None:
    """One test of the dictionary inversion."""
    xs: dict[str, str] = {"a": "one", "b": "two", "c": "three"}
    assert invert(xs) == {"one": "a", "two": "b", "three": "c"}


def test_invert_two() -> None:
    """A more practical inversion test."""
    xs: dict[str, str] = {
        "First Name": "Kaegon",
        "Last Name": "Matlock",
        "Age": "Nineteen"
    }
    assert invert(xs) == {
        "Kaegon": "First Name",
        "Matlock": "Last Name",
        "Nineteen": "Age"
    }


def test_invert_error() -> None:
    """Tests that the function raises the key error when necesary."""
    with pytest.raises(KeyError):
        xs: dict[str, str] = {
            "First Name": "Kaegon",
            "Last Name": "Kaegon"
        }
        invert(xs)


def test_favorite_color_empty() -> None:
    """Tests an empty dictiinary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == "No Values Entered"


def test_favorite_color_one() -> None:
    """Tests a dictiinary."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"
    

def test_favorite_color_two() -> None:
    """Another test for this awful function."""
    xs: dict[str, str] = {"kaegon": "orange", "kristie": "blue", "shane": "green", "chris": "orange", "soraya": "orange", "whoever": "purple"}
    assert favorite_color(xs) == "orange"


def test_count_empty() -> None: 
    """Tests an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_one() -> None: 
    """Tests an list of words related to unc."""
    xs: list[str] = ["chapel", "hill", "chapel", "hill", "tar", "heels", "chapel", "UNC"]
    assert count(xs) == {
        "chapel": 3,
        "hill": 2,
        "tar": 1,
        "heels": 1,
        "UNC": 1
    }


def test_count_two() -> None: 
    """Tests an list of words related to unc."""
    xs: list[str] = ["apple", "apple", "banana", "orange", "apple", "orange", "orange", "apple", "apple", "apple"]
    assert count(xs) == {
        "apple": 6,
        "orange": 3,
        "banana": 1,
    
    }