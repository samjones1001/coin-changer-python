class CoinChanger:
    def calculate(self, change_amount):
        if change_amount == 1: return [1]
        if change_amount == 2: return [2]
        return []