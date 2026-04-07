#Nitu Sharma 202501100700201-B
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self):
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{self.original_amount}")
        print(f"Final Amount Paid: ₹{self.final_amount}")
        print("-" * 30)


class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        self.final_amount = amount + gateway_fee + gst
        self.generate_receipt()


class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback
        self.generate_receipt()


class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        fee = 0.03 * amount + 20
        self.final_amount = amount + fee
        self.generate_receipt()


class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount
        if amount > self.balance:
            print(f"User: {self.user_name}")
            print("Transaction Failed: Insufficient Balance")
            print("-" * 30)
        else:
            self.balance -= amount
            self.final_amount = amount
            self.generate_receipt()
            print(f"Remaining Wallet Balance: ₹{self.balance}")
            print("-" * 30)


def process_payment(payment, amount):
    payment.pay(amount)


cc = CreditCardPayment("Nitu")
upi = UPIPayment("Nitu")
paypal = PayPalPayment("Nitu")
wallet = WalletPayment("Nitu", 1500)

process_payment(cc, 1000)
process_payment(upi, 1500)
process_payment(paypal, 2000)
process_payment(wallet, 500)
process_payment(wallet, 1200)