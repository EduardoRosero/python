#Son los errores que se presentan dentro del scripts al momento de ejecutarlos

print(2/10)
print("Se termino el Script")

#Ahora dividiendo 2 entre 0

try: #Es el contenido que se va a intentar ejecutar
	print(2/0)
except ZeroDivisionError as ex: #Se va a ejecutar cuando falle la ejecucion del try
	print(ex) #Mandamos a imprimir el error ocasionado
	print("No se puede dividir por cero")
	#De preferencia no poner una instruccion pass sino indicar el mensaje que indique que ocurre
print("Se termino el Script")


#Ejemplo 2

try:
	lista=[1,2]
	print(lista[9])
except IndexError as ex:
	print(ex)
	print("No es posible ontener la posicion 9 de la lista")


#Manejo de varios bloques except en un solo try

try: #Es el contenido que se va a intentar ejecutar
	print(2/0)
except ZeroDivisionError as ex: #Se va a ejecutar cuando falle la ejecucion del try
	print(ex) #Mandamos a imprimir el error ocasionado
	print("No se puede dividir por cero")
	#De preferencia no poner una instruccion pass sino indicar el mensaje que indique que ocurre
except IndexError as ex:
	print(ex)
	print("No es posible ontener la posicion 9 de la lista")


#Palabra reservada Exception
"""Permite capturar cualquier tipo de error sinimportar cual sea
asi permite ejecutar el bloque sin errores"""
try:
	lista=[1,2]
	print(lista[9])
except Exception as ex:
	print(ex) #De preferencia cuando se usa Exception se recomienda imprimir el tipo de error
	print("Algo ha salido mal")
finally: #Permite ejecutar un mensaje siempre, sea que se haya ejecutado la instruccion en el bloque try o no
	print("Se ha terminado es Script") 
