from .validate import validate_valor, validate_tiny_int
from .error import TinyIntError

#Definimos la funcion que me retorne su el numero comple o no con la condicion buscada e TinyInt
def  tiny_int(valor):
	try:
		if validate_valor(valor) and validate_tiny_int(valor):
			return True
		else:
			raise TinyIntError()
	except TinyIntError as error:
		print(error)