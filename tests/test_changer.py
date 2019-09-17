import pytest
from context import changer


@pytest.fixture(scope="function", autouse=True)
def coinChanger():
    return changer.CoinChanger()


def test_passing_zero_returns_an_empty_array(coinChanger):
    assert coinChanger.calculate(0) == []


def test_passing_one_returns_a_single_penny(coinChanger):
    assert coinChanger.calculate(1) == [1]


def test_passing_two_returns_a_single_2p_coin(coinChanger):
    assert coinChanger.calculate(2) == [2]


def test_passing_five_returns_a_single_5p_coin(coinChanger):
    assert coinChanger.calculate(5) == [5]