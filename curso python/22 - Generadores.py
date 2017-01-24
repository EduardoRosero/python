#Los generadores sirven para poder crear objetos sin necesidad de almacenarlos en la memoria RAM

def return_valores():
	print("Hola mundo 1")
	return True #Termina la funcion y devuelve un valor
print(return_valores())


def generador(*args): #Recibe en argumentos
	for valor in args:
		yield valor * 10 #Ejemplo, no utilizamos return
						#yield toma el valor y lo devuelve sin terminar la funcion


for valor in generador(1,2,3,4,5,6,7,8,9):
	print(valor)



#yield puede devolver mas de dos valores siempre y cuando quien lo llama espere recibor dos
def generador(*args): #Recibe en argumentos
	for valor in args:
		yield valor * 10, True #Devolvemos dos valores
						#yield toma el valor y lo devuelve sin terminar la funcion


for valor, bol in generador(1,2,3,4,5,6,7,8,9): #Esperamos recivil dos valores valor y bol
	print(valor, bol)