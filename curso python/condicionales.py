fruta= 'manzana'

if fruta == 'pera' : 
	print("El valor es pera")
else:
	print("El valor no es pera")

	"""Reducir el condicional a una linea"""
	mensaje = "El valor es pera" if fruta=="pera" else "No son iguales"
	print(mensaje)


	"""Elseif"""
if fruta == 'pera' : 
	print("El valor es pera")
elif fruta == 'manzana' :
	print("El valor es manzana")
elif fruta == 'manzana' :
	pass #Palabra reservada para pasar por el condicional y no asignar instrucciones
else:
	print("El valor no es pera ni manzana")



"""Forma de validar si una variable tiene algun valor o no"""
valor = 1

if valor:
	print("La variable no esta vacia")

sin_valor = None #Palabra reservada que nos permite indicar que una variable no tiene valor

"""Condicionales convarias condiciones"""
valor2=21

if valor and valor2 >=20:
	print("Es verdad")
else:
	print("Es falso")