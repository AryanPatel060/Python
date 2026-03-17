from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, amount): pass

class NormalDiscount(Discount):
    def calculate(self, amount): return amount

class VIPDiscount(Discount):
    def calculate(self, amount): return amount * 0.8

# Now, our calculator NEVER has to change. It is closed for modification!
class Checkout:
    def __init__(self,amount,discount_strategy):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def process(self):
        return self.discount_strategy.calculate(self.amount)

c1 = Checkout(1000,NormalDiscount())
c2 = Checkout(1000,VIPDiscount())

print(c1.process())  # 1000
print(c2.process())  # 800.0