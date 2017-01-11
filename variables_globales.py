#Palindromo es cadena que leida de derecha a izquierda o viceversa es lo mismo
def palindromo(frase):
	frase = frase.replace(' ','')  #Eliminamos espacios en blanco, en una variable local
	print(frase)
	return frase == frase[::-1] #Devuelve la cadena de caracteres al reves

frase = 'dabale arroz a la zorra el abad' #Variable Global
resultado = palindromo(frase)
print(frase)
print(resultado)
print(frase)


#No enviar parametro sino hacer que la frase la lea de la variable global
def palindromo():
	nuevo_valor = frase.replace(' ','')  #Eliminamos espacios en blanco, en una variable local
	return nuevo_valor == nuevo_valor[::-1]

frase = 'dabale arroz a la zorra el abad' #Variable Global
resultado = palindromo()
print(resultado)


#Para cambiar el valor de una variable global se usa la palabra reservada global
def valor_global():
	global variable_global
	variable_global="Cambiar valor de la variabe global"


def mostrar_global():
	print(variable_global)

variable_global ="Esto es una variable global"
mostrar_global()
valor_global()
print(variable_global)


#Las funciones tambien pueden crear variables globales

def crear_global():
	global nueva_variable
	nueva_variable ="Esto es una variable global"

crear_global()
print(nueva_variable)#Hacemos la llamada a la variable global creada dentro de la funcion