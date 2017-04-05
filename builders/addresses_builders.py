from mundiapilib.models.create_address_request import *

def BuildCreateAddress():
	request = CreateAddressRequest()
	request.city = "City"
	request.complement = "Complement"
	request.Country = "BR"
	request.Neighborhood = "Neighborhood"
	request.number = "123"
	request.state = "RJ"
	request.Street = "Street"
	request.zip_code = "22221010"
	return request