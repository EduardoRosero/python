#METODOS DE CADENAS

curso='Hola'
my_string='Esta es una cadena'


"""FORMATO"""
result = '{0} a todos {1}'.format(curso, my_string)
print(result)
result = result.lower()
print(result)
result = result.upper()
print(result)
result = result.title()
print(result)

"""BUSQUEDA"""

pos = result.find('Todos')
print('"Todos" esta en la posicion: ', pos)

"""Conteo"""

cont = result.count('a')
print('"a" se repite: ', pos ,  '  veces')

"""Substitucion"""

nuevo = my_string.replace('a','xx')
print(nuevo)

"""Regresa una lista"""
nuevo = my_string.split(' ') 
print(nuevo)