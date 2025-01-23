from src.polymorphism import CreditCard

def test_payment_methods():
    credit_card_payment = CreditCard(100)
    credit_card_payment.process_payment()
