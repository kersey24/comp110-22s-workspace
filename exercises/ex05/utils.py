"""Functions for exercise 5."""

__author__: str = "730401052"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of integers returns even integers."""
    evens: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Given a list of integers return a list at start index and non inclusive end index."""
    list_new: list[int] = []
    if start < 0: 
        start = 0
        # while start < end: 
        #     list_new.append(xs[start])
        #     start += 1
        # return list_new
    if end > len(xs): 
        end = len(xs)
    if xs == []: 
        return []
    if start > len(xs): 
        return []
    if end <= 0: 
        return[]
    while start < end: 
        list_new.append(xs[start])
        start += 1
    return list_new


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Given two lists of integers return a list with the second list's elements added onto the firsts."""
    new_list: list[int] = []
    i: int = 0
    while i < len(a_list): 
        new_list.append(a_list[i])
        i += 1
    z: int = 0 
    while z < len(b_list):
        new_list.append(b_list[z])
        z += 1
    return new_list