"""Tests for dictionary functions in dictionaries.py."""

__author__: str = "730401052"


from dictionary import invert, favorite_color, count


def test_empty_dict_invert() -> None:
    """Edge Test to see if a empty dictionary returns an empty dictionary."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_normal_invert() -> None: 
    """Use case to test if normal str, str dictionary is inverted."""
    a: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(a) == {"b": "a", "d": "c", "f": "e"}


def test_normal_invert_again() -> None:
    """Another use case to test if normal str, str dictionary is inverted."""
    a: dict[str, str] = {"z": "y", "w": "x", "t": "s"}
    assert invert(a) == {"y": "z", "x": "w", "s": "t"}


def test_favorite_color_empty() -> None:
    """Edge case to test if given an empty dictionary returns an empty dictionary."""
    a: dict[str, str] = {}
    assert favorite_color(a) == ""


def test_favorite_color_normal() -> None:
    """Use case to test if returns the most frequent color."""
    a: dict[str, str] = {"bob": "red", "Al": "red", "C": "black"}
    assert favorite_color(a) == "red"


def test_favorite_color_tie() -> None:
    """Use case to test if returns the most frequent color."""
    a: dict[str, str] = {"bob": "red", "Al": "red", "C": "black", "D": "black"}
    assert favorite_color(a) == "red"    


def test_count_empty() -> None: 
    """Edge test, if given an empty list return and empty dict."""
    a: list[str] = []
    assert count(a) == {}


def test_count_many_items() -> None: 
    """Edge test, if given an empty list return and empty dict."""
    a: list[str] = ["a", "a", "a", "b"]
    assert count(a) == {"a": 3, "b": 1}


def test_count_many_items_again() -> None: 
    """Edge test, if given an empty list return and empty dict."""
    a: list[str] = ["a", "b", "c", "d"]
    assert count(a) == {"a": 1, "b": 1, "c": 1, "d": 1}