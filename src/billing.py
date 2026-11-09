import stripe

stripe.api_key = 'your_stripe_secret_key'

def create_charge(amount, currency, description):
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        description=description
    )

def get_charge(charge_id):
    return stripe.Charge.retrieve(charge_id)

# Beispielaufruf
# charge = create_charge(2000, 'usd', 'Charge for service')