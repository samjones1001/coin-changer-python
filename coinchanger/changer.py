class CoinChanger:
    def __init__(self, denominations=(200, 100, 50, 20, 10, 5, 2, 1)):
        self.denominations = denominations

    def calculate(self, change_amount):
        change = []
        for coin in self.denominations:
            count = int(change_amount/coin)
            for _ in range(count):
                change.append(coin)
                change_amount -= coin
        return change
