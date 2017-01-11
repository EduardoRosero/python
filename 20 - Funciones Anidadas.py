#Funciones que reciben como parametros otras funciones
def validacion(num_uno, num_dos): #POr lo general este tipo de funciones realizan tareas complejas
	return num_uno>0 and num_dos>0

def division(num_uno, num_dos):
	if validacion(num_uno, num_dos): #Hacemos la llamada a la funcion
		return num_uno / num_dos

resultado = division(10,0)
print(resultado)

#Funciones anidadas


def division(num_uno, num_dos):
	variable = "Nuevo"
	#def validacion(num_uno, num_dos): #Esta es la funcion anidada, y como es anidada se le pueden quitar los parametros
	def validacion():	#Se debe tener en cuenta la identacion (tabulacion)
		print(variable)
		return num_uno>0 and num_dos>0
	#if validacion(num_uno, num_dos): #Hacemos la llamada a la funcion anidada, y se le pueden quitar los argumentos
	if validacion():
		return num_uno / num_dos

resultado = division(10,2)
print(resultado)


#Funciones que crean funciones closure


def crear_funcion(num_uno, num_dos):
	def validacion():
		return num_uno>0 and num_dos>0
	return validacion

nueva_funcion = crear_funcion(10,2)

#Tenemos la nueva funcion almacenada en la variable nueva_funcion
#La llamamos como normalmente se hace
print(nueva_funcion()) #Dependiendo de los paramtros que enviemos nos dara d resultado True o False

#Funciones que reciben de parametro funciones


def crear_funcion(num_uno, num_dos):
	def validacion():
		print("Se ejecuta una validacion")
		return num_uno>0 and num_dos>0
	return validacion

def aplicar_funcion(func): #rECIBE COMO ARGUMENTO LA FUNCION
	resultado = func() #No recibe parametros porque ya se le pasaron en la linea nueva_funcion = crear_funcion(10,2)
	print(resultado)

nueva_funcion = crear_funcion(10,2)
aplicar_funcion(nueva_funcion)