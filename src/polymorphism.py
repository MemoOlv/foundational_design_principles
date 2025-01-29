class PaymentBase:
    def __init__(self, amount: int):
        self.amount: int = amount
    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self):
        msg = f"Credit card payment for {self.amount}: succesfull"
        return msg

class PayPal(PaymentBase):
    def process_payment(self):
        msg = f"Paypal payment for {self.amount}: succesfull"
        return msg


class Circle():
    def __init__(self, radius: int):
        self.__radius: int = radius