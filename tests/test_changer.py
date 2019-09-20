import pytest
from context import changer


def test_passing_zero_returns_an_empty_array():
    assert changer.calculate(0) == []


def test_passing_one_returns_a_single_penny():
    assert changer.calculate(1) == [1]


def test_passing_two_returns_a_single_2p_coin():
    assert changer.calculate(2) == [2]


def test_passing_five_returns_a_single_5p_coin():
    assert changer.calculate(5) == [5]


def test_passing_10_returns_a_single_10p_coin():
    assert changer.calculate(10) == [10]


def test_passing_50_returns_a_single_50p_coin():
    assert changer.calculate(50) == [50]


def test_passing_100_returns_a_single_1_pound_coin():
    assert changer.calculate(100) == [100]


def test_passing_200_returns_a_single_2_pound_coin():
    assert changer.calculate(200) == [200]


def test_returns_two_coins_where_necessary():
    assert changer.calculate(3) == [2, 1]
    assert changer.calculate(11) == [10, 1]


def test_returns_three_coins_where_necessary():
    assert changer.calculate(16) == [10, 5, 1]
    assert changer.calculate(23) == [20, 2, 1]


def test_returns_multiple_coins_for_complex_cases():
    assert changer.calculate(227) == [200, 20, 5, 2]
    assert changer.calculate(77) == [50, 20, 5, 2]
    assert changer.calculate(373) == [200, 100, 50, 20, 2, 1]
