#Vamos a crear un lambda que permita realizar lo mismo que la funcion suma abajo indicada
#def suma(valor_uno, valor_dos):
#	return valor_uno+valor_dos


#Lambda permite crear funciones anonimas en una sola linea de codigo
#Se hace bajo denamda, crear lambda, dentro de lambda no se usan ciclos ni condicionales
#Se debe ser muy especifico
mi_funcion = lambda valor_uno, valor_dos : valor_uno+valor_dos
#No se utiliza return porque lambdas retornan algo

resultado = mi_funcion(10,20)
print(resultado)


#Vamos a dar un formato de pregunta a la sentencia
formato = lambda sentencia : '¿{0}?'.format(sentencia)
#Es importante que en algunas versiones de python cuando se usa el formato se debe indicar el numero del parametro al que se hace referencia en est cao es el 0

resultado = formato('Esto es ahora una pregunta')
print(resultado)

#Cuando un lambda no recibe ningun valor, podemos retornar algo

no_valor  = lambda : 10
resultado = no_valor()
print(resultado)


#Una lambda que no devuelve valores al menos debe ejecutar una accion por ejemplo un print y nos devolvera un valor de None

sin_retorno = lambda : print("No retornamos nada y se crea un None")

resultado = sin_retorno()
print(resultado)