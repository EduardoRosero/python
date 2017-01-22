#Crear una excepcion
class TinyIntError(Exception):
	#pass #Definimos la excepcion como una funcion que hereda de Exception y le agregamos un pass para que la ejecucion no temine abruptamente
	def __init__(self):
		self.message="El numero no cuenta con las caracteristicas de un numero TinyInt"

	def __str__(self):
		return self.message