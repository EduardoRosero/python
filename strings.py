#Manejo de Strings

mi_string="Mi Super Mensaje 'Comillas simples'\n\n"
print(mi_string)

mi_string = '''Este es un string
		que contiene saltos de linea
		pa que vea nomas\n\n'''
print(mi_string)


mi_string = "Este es un string\nque contiene saltos de linea\npa que vea nomas\n\n"
print(mi_string)



mi_string='Mi Super Mensaje "Comillas dobles"\n\n'
print(mi_string)


curso = "Python "
nombre = " Eduardo"
finalmsg = curso + nombre+"\n\n"
print(finalmsg )

finalmsg = "Nuevo curso de %s por %s" %(curso, nombre)
print(finalmsg ) 

finalmsg = "Nuevo curso de {} por {}".format(curso, nombre)
print(finalmsg ) 