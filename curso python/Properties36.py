class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password

	"""Vamos a usar propertis para manejar atributos privados, lo que seria
	los getters y setters de java
	"""
	@property
	def password(self):
		return self.__password

	@password.setter #Esta property nos permite cambiar el valor de el atributo privado password
	def password(self, valor):
		self.__password = self.__generar_password(valor)


eduardo = Usuario("eduardo", "root1234", "zerhiphop@live.com")
print(eduardo.password)#Hacemos la llamada al metodo del property y no al atributo

eduardo.password = "Cambiando pass"
print(eduardo.password)