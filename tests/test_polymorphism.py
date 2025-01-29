from pytest import raises

from src.polymorphism import CreditCard, PayPal, Circle

def test_payment_methods():
    amount_to_pay = 100
    credit_card_payment = CreditCard(amount_to_pay)
    obtained = credit_card_payment.process_payment()
    assert obtained == "Credit card payment for 100: succesfull"

    paypal_payment = PayPal(amount_to_pay)
    obtained = paypal_payment.process_payment()
    assert obtained == "Paypal payment for 100: succesfull"

def test_circle_class():
    radius = 15
    obtained = Circle(radius)
    assert obtained.radius == radius

    new_radius = 17
    obtained.radius = new_radius
    assert obtained.radius == new_radius

    wrong_radius = -8
    with raises(ValueError, match="Radius cannot be negative!"):
        obtained.radius = wrong_radius
