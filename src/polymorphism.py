## Base class for payment methods

class PaymentBase:
    def __init__(self, amount: int):
        self.amount: int = amount
    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self):
        pass
