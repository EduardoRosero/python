class Circulo:
	#_pi = 3.1416

	def __init__(self, radio):
		self.radio=radio

	"""
	Se crean metodos estaticos cuando son algo que le pertenece a la clase de manera absoluta
	"""
	@staticmethod #Lo decoramos con esta etiqueta para indicar que es statico, y este tipo de metodos le pertenecen a la clase y no al objeto instanciado
	def pi (): 
		return 3.1416

	def area(self): #Este es un metodo de instancia, es decir que un objeto puede mandar a llamarlos, son aquellos metodos que estan dentro de una clase y su primer parametro es la palabra reservada self
		#return self.radio * self.radio * Circulo.pi()
		return self.radio * self.radio * self.pi()

print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())