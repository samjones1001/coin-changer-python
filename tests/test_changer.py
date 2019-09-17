from context import changer


def test_passing_nothing_returns_an_empty_array():
    coinchanger = changer.CoinChanger()
    assert coinchanger.calculate(0) == []