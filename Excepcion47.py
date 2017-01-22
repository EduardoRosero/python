#Crear una excepcion
class TinyIntError(Exception):
	pass #Definimos la excepcion como una funcion que hereda de Exception y le agregamos un pass para que la ejecucion no temine abruptamente
	

def tiny_int(val):
	return val >= 0 and val <= 255

try:
	numero = 1000
	if tiny_int(numero):
		print("El numero es correcto")
	else:
		#Se utiliza la palabra reservada raisa para Catchear la excepcion
		raise TinyIntError("Este es un mensaje para el error en los numeros que no son TinyInt") #Agregamos el mensaje para nuestra excepcion
except TinyIntError as error:  #Ingresamos nuestra excepcion y la renombramos como error
	print("No es posible terminar la opracion")
	print(error)