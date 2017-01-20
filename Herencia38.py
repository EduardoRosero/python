#La herencia nos permite crear clases a partir de otras clases

class Gato:
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino esta cazando")

class Jaguar:
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino esta cazando")

gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)