my_list = ["strings",21,21.5,True]
my_list.append(42) #Lo aumenta en la ultima posicion
my_list.insert(1, 'insert') #Parametro 1 es un entero indica la posicion, el segundo el dato
my_list.remove(21)
print(my_list)
print(my_list[1]) #Imprimir posicion 1


"""Trabajar como si fueran pilas"""

ultimo = my_list.pop() #Toma el ultimo valor de la lista
print(my_list)
print(ultimo)

"""Listas de un solo tipo"""

enteros=[21,25,98,10,15,3,74,14,20]
print(enteros)
enteros.sort() #Ordenar el arreglo
print(enteros)

enteros.sort(reverse = True) #Ordenar el arreglo
print(enteros)

"""Unir listas"""

enteros2=[100,200]

enteros.extend(enteros2)
print(enteros)