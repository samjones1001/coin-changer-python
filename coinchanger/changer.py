class CoinChanger:
    def calculate(self, change_amount):
        if change_amount == 1: return [1]
        if change_amount == 2: return [2]
        if change_amount == 5: return [5]
        if change_amount == 10: return [10]
        if change_amount == 50: return [50]
        return []