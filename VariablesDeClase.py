class Circulo:
	"""Esta representando a un circulo en la vida real
	para lo cial se necesita una constante universal que es pi"""
	_pi = 3.1416 #Variable de clase, le pertenece a la clase y no a los objetos (instancias)
	def __init__(self, radio):
		self.radio=radio
		#self.pi = 3.1416 #Le va a pertenecer a cualquier instancia de la clase, pero como es una constante la vamos a ubicar en otra posicion para crear una variable de clase

	def area(self):
		return self.radio*self.radio*self._pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno._pi)
print(circulo_dos._pi)

print(Circulo._pi) #No se necesita crear un objeto para usar pi (le petenece a la clase)

print(circulo_uno.__dict__)#Nos muestra un diccionario de los atributos de la clase excluyendo los que son variables de clase

print(circulo_uno.area())