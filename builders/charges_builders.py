from mundiapilib.models.create_charge_request import *
from mundiapilib.models.create_customer_request import *
from mundiapilib.models.create_payment_request import *
from mundiapilib.models.create_credit_card_payment_request import *
from mundiapilib.models.create_credit_card_request import *
from mundiapilib.models.update_charge_credit_card_request import *
from mundiapilib.models.update_charge_payment_method_request import *

def BuildCreditCardCharge(amount, capture = True):
	request = CreateChargeRequest()

	request.amount = amount
	request.customer = CreateCustomerRequest()
	request.customer.name = "Vitor de Andrade"

	request.payment = CreatePaymentRequest()
	request.payment.payment_method = "credit_card"
	request.payment.credit_card = CreateCreditCardPaymentRequest()
	request.payment.credit_card.capture = capture

	request.payment.credit_card.credit_card_info = CreateCreditCardRequest()
	request.payment.credit_card.credit_card_info.holder_name = "VITOR DE ANDRADE"
	request.payment.credit_card.credit_card_info.number = "4929675815719041"
	request.payment.credit_card.credit_card_info.exp_month = 12
	request.payment.credit_card.credit_card_info.exp_year = 21
	request.payment.credit_card.credit_card_info.cvv = "123"

	return request

def BuildBoletoCharge(amount):
	request = CreateChargeRequest()

	request.amount = amount
	request.customer = CreateCustomerRequest()
	request.customer.name = "Vitor de Andrade"

	request.payment = CreatePaymentRequest()
	request.payment.payment_method = "boleto"

	return request

def BuildUpdateChargeCreditCard():
	request = UpdateChargeCreditCardRequest()
	request.credit_card = CreateCreditCardRequest()
	request.credit_card.number = "5598193511496317"
	request.credit_card.cvv = "132"
	request.credit_card.exp_month = 1
	request.credit_card.exp_year = 23
	request.credit_card.holder_name = "VITOR DE ANDRADE"
	return request

def BuildUpdateChargePaymentMethod():
	request = UpdateChargePaymentMethodRequest()
	request.payment_method = "boleto"
	return request	
