
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class TelebirrPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} Birr using Telebirr")

class BankPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} Birr using Bank Transfer")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} Birr using Card")

payments = [
    TelebirrPayment(),
    BankPayment(),
    CardPayment()
]

for payment in payments:
    payment.pay(500)
