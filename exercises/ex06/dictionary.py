"""Exercise 6, practice with dictionary functions."""

__author__: str = "730401052"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    result: dict[str, str] = {}
    for key in a:
        result[a[key]] = key
    error_check: list[str] = []
    for key in a:
        error_check.append(a[key])
    i: int = 0
    while i < len(error_check):
        count: int = 0 
        for word in error_check:
            if word == error_check[i]:
                count += 1 
        if count > 1: 
            raise KeyError("KeyError")
        i += 1 

    return result


def count(a: list[str]) -> dict[str, int]:
    """Provides the count for each item in a list of strings."""
    result: dict[str, int] = {}
    for item in a: 
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, provides the color which appears the most."""
    new_dict: dict[str, int] = {}
    color_list: list[str] = list(a.values())
    for item in color_list: 
        if item in new_dict:
            new_dict[item] += 1
        else: 
            new_dict[item] = 1
    color: int = 0 
    i: str = ''
    for key in new_dict:
        if new_dict[key] > color: 
            color = new_dict[key]
            i = key
    return i