"""Tests for functions of exercise 5."""

from exercises.ex05.utils import only_evens, sub, concat


__author__: str = "730401052"


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_no_evens() -> None: 
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None: 
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_sub_empty() -> None:
    xs: list[int] = []
    assert sub(xs, 0, 10) == []


def test_sub_normal() -> None: 
    xs: list[int] = [20, 30, 40, 50, 60, 70]
    assert sub(xs, 2, 5) == [40, 50, 60]


def test_sub_normal_again() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 4, 8) == [5, 6, 7, 8]


def test_sub_start_neg() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, -3, 8) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_end_too_big() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 4, 20) == [5, 6, 7, 8, 9, 10]


def test_sub_end_0() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 4, 0) == []


def test_sub_end_neg() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 4, -1) == []


def test_sub_start_too_big() -> None: 
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 11, 5) == []


def test_concat_empty() -> None: 
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_concat_empty_a() -> None: 
    a_list: list[int] = []
    b_list: list[int] = [1, 2, 3]
    assert concat(a_list, b_list) == [1, 2, 3]


def test_concat_empty_b() -> None: 
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = []
    assert concat(a_list, b_list) == [1, 2, 3]


def test_concat_unit() -> None: 
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = [4, 5, 6]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6]


def test_concat_unit_2() -> None: 
    a_list: list[int] = [2, 4, 6]
    b_list: list[int] = [6, 4, 2]
    assert concat(a_list, b_list) == [2, 4, 6, 6, 4, 2]