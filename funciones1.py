#Ejemplo factorial
#Debemos abstraer el algoritmo y colocarlo dentro de una funcion

def factorial_numero():
	"""Para saber que mi codigo esta dentro 
	de mi funcion debo verificar las tabulaciones"""
	numero = 5
	factorial =1
	while numero>0:
		factorial = factorial *numero
		numero-=1
	print(factorial)


#LLamar a la funcion
factorial_numero()


#Utilizacion de Parametros en las funciones

def factorial_numero(numero):
	factorial =1
	while numero>0:
		factorial = factorial *numero
		numero-=1
	print(factorial)


#LLamar a la funcion
factorial_numero(6)


#Retornar valores en una funcion

def factorial_numero(numero):
	factorial =1
	while numero>0:
		factorial = factorial *numero
		numero-=1
	return factorial


#LLamar a la funcion
resultado = factorial_numero(7)
print(resultado)