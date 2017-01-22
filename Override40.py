#Sobreescritura de metodos

class Animal:
	def terrestre(self):
		return True

class Mascota:
	def __init__(self, nombre):
		self.nombre=nombre

	def mostrar_nombre(self):
		print(self.nombre)




class Felino(Animal): #Clase padre de la que se van a heredar metodos y atributos
	@property
	def garras_retractiles(self):
		return True

	
	def cazar(self):
		print("El felino esta cazando")

class Gato(Felino, Mascota): #Entre parentesis colocamos el nombre de la clase que queremos heredar, con comas separamos el nombre de las demas clases a heredar
	def __init__(self, nombre):
		Mascota.__init__(self, nombre)
		self.nombre_gato=nombre

	def gato_cazador(self):
		self.cazar()

	def mostrar_nombre(self): #En esta parte hemos sobrescrito el metodo de la clase mascota
		Mascota.mostrar_nombre(self) #Para llamar el metodo de la clase padre, cuando son metodos de clase
		print("El nombre del gato es: {0}".format(self.nombre))


gato = Gato("Bigotes")
gato.nombre="Bigotes"
gato.mostrar_nombre()


