#La herencia nos permite crear clases a partir de otras clases
class Animal:
	def terrestre(self):
		return True

class Felino(Animal): #Clase padre de la que se van a heredar metodos y atributos
	@property
	def garras_retractiles(self):
		return True

		"""Los metodos privador __cazar() no se pueden heredar en las clases hijos"""
	def cazar(self):
		print("El felino esta cazando")

class Gato(Felino): #Entre parentesis colocamos el nombre de la clase que queremos heredar
	def gato_cazador(self):
		self.cazar()

class Jaguar(Felino):
	pass

gato = Gato()
jaguar = Jaguar()

print(gato.terrestre())
print(jaguar.terrestre())
print(jaguar.garras_retractiles)

