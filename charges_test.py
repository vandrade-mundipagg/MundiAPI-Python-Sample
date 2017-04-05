from mundiapilib.mundi_api_client import *
from mundiapilib.models.create_charge_request import *
from mundiapilib.models.create_customer_request import *
from mundiapilib.models.create_payment_request import *
from mundiapilib.models.create_credit_card_payment_request import *
from mundiapilib.models.create_credit_card_request import *

# ...

# Configuration parameters and credentials
basic_auth_user_name = "sk_test_DoOpxqDTEFVKz3E4" # The username to use with basic authentication
basic_auth_password = "" # The password to use with basic authentication

client = MundiAPIClient(basic_auth_user_name, basic_auth_password)

charges_client = client.charges

# Create (credit_card)
request = CreateChargeRequest()

request.amount = 1000000
request.customer = CreateCustomerRequest()
request.customer.name = "Vitor de Andrade"

request.payment = CreatePaymentRequest()
request.payment.payment_method = "credit_card"
request.payment.credit_card = CreateCreditCardPaymentRequest()

request.payment.credit_card.credit_card_info = CreateCreditCardRequest()
request.payment.credit_card.credit_card_info.holder_name = "VITOR DE ANDRADE"
request.payment.credit_card.credit_card_info.number = "4929675815719041"
request.payment.credit_card.credit_card_info.exp_month = 12
request.payment.credit_card.credit_card_info.exp_year = 21
request.payment.credit_card.credit_card_info.cvv = "123"

result = charges_client.create_charge(request)

# Create (boleto)

# Get
charge_client.get_charge(result.id)

# Retry
charge_client.retry_charge(result.id)

# List
charge_client.get_charges()

# Cancel (total)

# Cancel (partial)

# Change credit_card
# Change payment_method

# Preauth

# Capture