#Metodos magicos

class Usuario:
	def __init__(self):
		self.__password="Esto es secreto"
	def mostrar_password(self):
		print(self.__password)


usuario = Usuario()
print(usuario.__dict__) #Visualizamos que no existen atributos
usuario.nombre="Eduardo" #Se crea un nuevo atributo publico dentro de la clase
usuario.__password="Ya no es secreto"
print(usuario.nombre)
print(usuario.__dict__) #Visualizamos los atributos creados
print(usuario.__password) #Este atributo es completamente nuevo y difrente del de la clase



#Metodos magicos, se caracterizan porque empiezan y terminan con doble guion bajo

class Usuario:
	def __new__(cls): #Este es el constructor de la clase
#primero se ejecuta el metodo new y despues el init"""
		print("Este metodo se ejecuta primero")
		return super().__new__(cls)

	def __init__(self):
		print("Este metodo se ejecuta segundo")

	def __str__(self):
		return "Esto se imprime cuando intento mostrar el objeto"

	def __getattr__(self, nombre_attributo_intentamos_acceder):
		print("Aqui mostramos que no se encontro el atributo del objeto")
		self.otros_metodos()

	def otros_metodos(self):
		print("Otros metodos")




usuario = Usuario()
print(usuario)
print(usuario.apellido)