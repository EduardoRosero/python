#Permite agregar mas funcionalidad en una funcion concreta

def saluda():
	print("Hola Mundo")

saluda()
#A, B y C son funciones
#Un decorador es una funcion que recibe como parametro otra funcion para dar salida una nueva funcion
#A recibe de parametro B y da como resultado C, A,B,C Funciones

def decorador(func): #Definimos A, recibimos como parametro B
	def nueva_funcion():
		#Agrego codigo antes de ejecutarla, ej abrir base de datos
		print("Vamos a ejecutar la funcion")
		func()
		#Agrego codigo despues de ejecutarla, ej cerrar base de datos
		print("Se ejecuto la funcion")
	return nueva_funcion #Creamos y devolvemos C

@decorador #Hacemos la llamada al reorador
def saluda():
	print("Hola Mundo")

saluda()


@decorador
def suma():
	print(10+20)

suma()

#Si la funcion recibe parametros, el programa va a fallar por como esta definido el decorador
#Para que el decorador sea mas flexible le dejamos recibir n cantidad de argumentos
def decorador1(func): #Definimos A, recibimos como parametro B
	def nueva_funcion(*args, **kwargs):
		#Agrego codigo antes de ejecutarla, ej abrir base de datos
		print("Vamos a ejecutar la funcion")
		func(*args, **kwargs)
		#Agrego codigo despues de ejecutarla, ej cerrar base de datos
		print("Se ejecuto la funcion")
	return nueva_funcion #Creamos y devolvemos C

@decorador1
def suma(num_uno, num_dos):
	print(num_uno + num_dos)

suma(20, 100)

#En caso de que la funcion retorne en vez de imprimir asignamos el resultado de la ejecucion a una variable
def decorador1(func): 
	def nueva_funcion(*args, **kwargs):
		
		print("Vamos a ejecutar la funcion")
		resultado = func(*args, **kwargs) #Asignamos el resultado a una variable
		
		print("Se ejecuto la funcion")
		return resultado
	return nueva_funcion #Creamos y devolvemos C

@decorador1
def suma(num_uno, num_dos):
	return num_uno + num_dos

resultado = suma(20, 100)
print(resultado)


#Lo decoradores tambien pueden recibir parametros
#Para eso se crea una funcion mas
def decorador2(is_valid): #Definimos esta nueva funcion y colocamos la anterior dentro de esta con su respectiva identacion
	def _decorador2(func): #Renombramos esta funcion que tenia el mismo de la superior que la contiene
		def nueva_funcion(*args, **kwargs):
			
			if is_valid:
				print("Vamos a ejecutar la funcion")
			resultado = func(*args, **kwargs) #Asignamos el resultado a una variable
			
			print("Se ejecuto la funcion")
			return resultado
		return nueva_funcion #Creamos y devolvemos C
	return _decorador2 #Retornamos el decorador interno (el renombrado)

@decorador2(is_valid = False) #Si l valor es True imprime el mensaje Vamos a ejecutar la funcion, si es False no lo imprime
def suma(num_uno, num_dos):
	return num_uno + num_dos

resultado = suma(20, 100)
print(resultado)
