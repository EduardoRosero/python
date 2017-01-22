#La herencia multiple perimite heredar a nuestra clase de varias clases
class Animal:
	def terrestre(self):
		return True

class Mascota:
	nombre="" #Todas las mascotas necesitan un nombre
	def mostrar_nombre(self):
		print(self.nombre)

class Felino(Animal): #Clase padre de la que se van a heredar metodos y atributos
	@property
	def garras_retractiles(self):
		return True

		"""Los metodos privador __cazar() no se pueden heredar en las clases hijos"""
	def cazar(self):
		print("El felino esta cazando")

class Gato(Felino, Mascota): #Entre parentesis colocamos el nombre de la clase que queremos heredar, con comas separamos el nombre de las demas clases a heredar
	def gato_cazador(self):
		self.cazar()

class Jaguar(Felino):
	pass

gato = Gato()
gato.nombre="Bigotes"
print(gato.mostrar_nombre())


