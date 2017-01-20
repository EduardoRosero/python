class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #Creamops un atributo privado
		self.email = email


#Algoritmo para encriptar el password, metodo de la clase (Verificar tabulacion)

	def  __generar_password(self, password):
		"""Para crear metodos privados se coloca doble 
	guion bajo antes del nombre del metodo"""
		return password.upper()

	def get_password(self):
		"""Creamos un metodo para poder acceder al
		atributo privado, (encapsulamiento)
		"""
		return self.__password

eduardo = Usuario("Eduardo", "root1234", "zerhiphop@live.com")
print(eduardo.username)
#eduardo.__password="Aqui cambio todo el password" #Utilizamos esta linea para indicar que se puede manipular la informacion de los atributos de la clase
#print(eduardo.password) 
print(eduardo.get_password())
print(eduardo.email)

"""Una ves creada la instancia no quiero que se pueda modificar los atributos, ejemplo el password
para eso creo metodos privados, para eso se agrega __ doble guion bajo
en el atributo que queremos hacerlo privado"""