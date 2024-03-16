class CashRegister:
    def __init__(self):
        self.money = 0

    def top_up(self, x):
        if x < 0:
            raise ValueError("Amount cannot be negative")
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if x < 0:
            raise ValueError("Amount cannot be negative")
        if self.money < x:
            raise ValueError("Not enough money")
        self.money -= x

# Example usage:
cash_register = CashRegister()
cash_register.top_up(10000)
print(cash_register.count_1000())  #10
cash_register.take_away(5000)
print(cash_register.count_1000())  #5