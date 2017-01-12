"""Diccionarios
Son estructursa de datos como listas y tuplas
que permiten almacenar
 datos, eteros strings, tuplas etc
los diccionarios no se rigen por indices"""

diccionario = {'a':21,'b':"Hola",5:'String',(1,2):False}#Requieren una clave en este caso 'a'
print(diccionario)
"""Si se asigna las mismas claves para los datos del diccionario
se toma la ultima clave de la derecha con el mismo nombre

Los diccionarios pueden crecer o decrecer"""

diccionario['c']="Nuevo"#Se crea clave/valor
print(diccionario)


"""Modificar un valor"""

diccionario['a']=300000
print(diccionario)

"""Obtener un valor"""

valor=diccionario['a']
print(valor)

"""Si la clave no existe en el diccionario nos da error
y para evitar eso se usa un metodo del diccionario"""

valor=diccionario.get('z',"No se encuentra la clave")
print(valor)


"""Eliminar valores del diccionario"""

del diccionario[5]
print(diccionario)

"""Utilizar solo claves o solo valores"""

llaves = diccionario.keys()
print(llaves)

valores = diccionario.values()
print(valores)
"""Transformar llaves a lista"""
llaves = list( diccionario.keys())
print(llaves)

"""Transformar llaves a tupla"""
valores = tuple(diccionario.values())
print(valores)

diccionario2 = {'z':'kkk', 666:"bestia"}

"""Extender un diccionario con datos de otro"""
diccionario['z'] = diccionario2['z']
diccionario[666] = diccionario2[666]
print(diccionario)


"""Segundo metodo"""
diccionario.update(diccionario2)
print(diccionario)