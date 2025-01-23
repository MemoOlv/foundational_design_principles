from src.polymorphism import CreditCard

def test_payment_methods():
    amount_to_pay = 100
    credit_card_payment = CreditCard(amount_to_pay)
    obtained = credit_card_payment.process_payment()
    assert obtained == "Credit card payment for 100: succesfull"

