#Recibir argumentos
"""Si colocamos un * antes de la variable 
nos permite recibir n argumentos"""

def suma(*var): #Nos permite trabajar los argumentos como una tupla
	print(var)  #Si no le pasamos argumentos nos devuelve una tupla vacia es decir ()
	resultado = 0
	
	
	for valor in var:
		resultado = resultado+valor
	return resultado

resultado = suma(10, 100, 90, 50)
print(resultado)


#Definir una clave que nos permita identificar el argumento que recibimos
#Cuando se trabaja con n argumentos donde desconocemos n
def suma(**kwargsr): #Nos permite trabajar los argumentos como un diccionario
	valor = kwargsr.get("valor", "No existe")
	print(valor)


resultado = suma(valor="Eduardo", x=2, y=9, z=True)
print(resultado)