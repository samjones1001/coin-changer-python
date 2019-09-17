class CoinChanger:
    def __init__(self, denominations=(200, 100, 50, 20, 10, 5, 2, 1)):
        self.denominations = denominations

    def calculate(self, change_amount, coins=[]):
        for coin in self.denominations:
            if coin <= change_amount:
                change_amount -= coin
                coins.append(coin)
                return self.calculate(change_amount, coins)
        return coins
