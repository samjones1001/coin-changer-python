import pytest
from context import changer


@pytest.fixture()
def coin_changer():
    return changer.CoinChanger()


def test_passing_zero_returns_an_empty_array(coin_changer):
    assert coin_changer.calculate(0) == []


def test_passing_one_returns_a_single_penny(coin_changer):
    assert coin_changer.calculate(1) == [1]


def test_passing_two_returns_a_single_2p_coin(coin_changer):
    assert coin_changer.calculate(2) == [2]


def test_passing_five_returns_a_single_5p_coin(coin_changer):
    assert coin_changer.calculate(5) == [5]


def test_passing_10_returns_a_single_10p_coin(coin_changer):
    assert coin_changer.calculate(10) == [10]


def test_passing_50_returns_a_single_50p_coin(coin_changer):
    assert coin_changer.calculate(50) == [50]


def test_passing_100_returns_a_single_1_pound_coin(coin_changer):
    assert coin_changer.calculate(100) == [100]


def test_passing_200_returns_a_single_2_pound_coin(coin_changer):
    assert coin_changer.calculate(200) == [200]


def test_returns_two_coins_where_necessary(coin_changer):
    assert coin_changer.calculate(3) == [2, 1]
    assert coin_changer.calculate(11) == [10, 1]


def test_returns_three_coins_where_necessary(coin_changer):
    assert coin_changer.calculate(16) == [10, 5, 1]
    assert coin_changer.calculate(23) == [20, 2, 1]