from ..animales import Animal #Importamos llamando al modulo y a la clase
#.. significa sube un nivel y busca ahi
class Gato(Animal):
	def __init__(self,nombre):
		self.nombre=nombre