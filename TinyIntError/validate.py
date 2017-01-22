#En esta parte se hace la validacion
def validate_tiny_int(valor):
	return valor >= 0 and valor <= 255

#En esta parte hacemos la validacion para saber si es un numero
def validate_valor(valor):
	try:
		return isinstance(int(valor), int) #Antes de validar el numero intentamos transformarlo a ento
	except ValueError as error:
		return False