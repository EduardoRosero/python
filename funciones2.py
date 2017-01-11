#
def suma(numero_uno, numero_dos, numero_tres):
	return numero_uno+numero_dos+numero_tres

resultado = suma(10,20,30)
print(resultado)


def division(numero_uno, numero_dos):
	return numero_dos/numero_uno

resultado = division(10,20)
print(resultado)

#Asignar los valores deliberadamente
resultado = division(numero_dos = 10, numero_uno = 20)
print(resultado)


#Dejamos asignado un valor por default para que lo tome en caso de no mandar ningun parametro
def multiplicacion(numero_uno, numero_dos=10):
	return numero_uno * numero_dos

resultado = multiplicacion(10,11)
print(resultado)

def multiples_valores():
	return "String", 1 , True, 25.6

resultado = multiples_valores()

text = resultado[0]
entero = resultado[1]
booleano  = resultado[2]
flotante = resultado[3]

print(text)
print(entero)
print(booleano)
print(flotante)


#Esto se puede optimizr asi
#Es decir se asignan los valores que devuelve la funcion a las variables en una sola linea


text, entero, booleano, flotante = multiples_valores()

print(text)
print(entero)
print(booleano)
print(flotante)

#Podemos asignar funciones a variables y mandarlas a ejecutar dentro de la variable

mi_variable = multiplicacion
resultado = mi_variable(6,1000)
print(resultado)

#Se puede mandar a ejecutar funciones dentro de otras funciones

def mostrar_resultado( funcion ):
	print(funcion(6,8))

mi_variable = multiplicacion
mostrar_resultado(mi_variable)

#Estamos enviando de parametro una funcion