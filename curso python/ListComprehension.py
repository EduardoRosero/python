#Futurre nos permite crear listas, diccionarios y tuplas de forma sencilla
#el primer "valor" es lo que se va a agregar a la lista
lista = [ valor for valor in range (0,101) ]
#Se necesita dos parametros el valor que se va a agregar y el ciclo que lo va a agregar
print(lista)

#Se puede usar condicionales

lista = [ valor for valor in range (0,101) if valor%2==0]
print(lista)

#Tambien se pueden crear tuplas, para volverlas tuplas se debe usar la palabra reservada tuple y ponerla dentro de parentesis

tupla = tuple(( valor for valor in range (0,101) if valor%2!=0 ))
print(tupla)

#Se pueden crear de igual manera diccionarios

diccionario = { indice:valor for indice, valor in enumerate(lista) }
print(diccionario)

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice<10}
print(diccionario)