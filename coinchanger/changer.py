from typing import List


def calculate(change_amount: int, coins=None) -> List[int]:
    if coins is None: coins = []
    for coin in (200, 100, 50, 20, 10, 5, 2, 1):
        if coin <= change_amount:
            change_amount -= coin
            coins.append(coin)
            return calculate(change_amount, coins)

    return coins
