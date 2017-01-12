#Documentacion de funciones

def generador(*args):
	""" Recibe n cantidad de parámetros y regresa el námero recibido como
parámetro ademàs de un valor True si el numero es mayor que 5 o 
False en caso contrario, ESTE TEXTO SE AÑADE PARA INDICAR LO QUE
HACE LA FUNCION ES DECIR LA DOCUMENTACIÓN.
SIEMPRE SE COLOCA EN LA PRIMERA LINEA DENTRO DE LA FUNCIÓN YA QUE PYTHON
RECONOCE LOS MENSAJES EN TRIPLES COMILLAS DOBLES COMO LA DOCUMENTACION"""	
	for valor in args:
		yield valor, True if valor>5 else False

nombre = generador.__name__
documentacion = generador.__doc__ #En python las funciones se consideran clases y .__doc__ es un atributo de dicha clase que se va a llenar con el comentario puesto en laprimera linea dentro de la funcion
print(nombre.upper(), ": ", documentacion) #Imprimimos el nombre de la funcion convertida a mayusculas y la descripcion indicada en la documentacion