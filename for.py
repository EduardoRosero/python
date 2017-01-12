#CICLO FOR

#Puede ser una lista o tupla
lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
	print(valor)

nuevo_rango = range(0,10) #Todos deben ser numeros
#Si solo coloco un parametro en el rango va a asumir que vadesde el cero hasta el valor -1
#Si le paso tres parametros vaa ser una lista iterable consaltos del valor del tercer parametro
for valor in nuevo_rango:
	print(valor)

indice =0
for valor in lista:
	print(valor, " Tiene el indice ", indice) #Utilizar el indice y el valor
	indice +=1

#Lo mismo que arriba pero sin una variable externa
for indice, valor in enumerate(lista):
	print(valor, " Tiene el indice ", indice) #Utilizar el indice y el valor
	indice +=1

#Utilizar como final el tamaño de la lista
for valor in range(0, len(lista)): #Len regresa el numero de objetos dentro de un objeto iterable
	print(valor)

#Hacer recorrer strings

for valor in "Curso de codigo facilito": #Los strings son iterables
	print(valor)


#Recorrer un diccionario

diccionario = {'a':10, 'b' :20, 'c' :30}
for llave, valor in diccionario.items(): #Items regresa la llave y el valor
	print("la llave ", llave, " tiene el valor de ", valor)