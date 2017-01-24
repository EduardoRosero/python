#Strings como arreglos

my_string="Esta es mi cadena"

#E s t a   e s   m i  c a d e n a
#0 1 2 3 4 5 6 7 8 9.....

print(my_string[0])


#Mostrar desde el final
my_string="Esta es mi cadena"
print(my_string[-1])

#Mostrar una porcion de los caracterres
my_string="Esta es mi cadena"
print(my_string[5:10])

#Mostrar una porcion de los caracterres
my_string="Esta es mi cadena"
print(my_string[-5:-1])


#Mostrar una porcion de los caracterres en saltos progresivos
my_string="Esta es mi cadena"
print(my_string[-12:-1:2])#Saltos de 2 en dos ultimo parametro


#String leido de derecha a izquierda
my_string="Esta es mi cadena"
print(my_string[::-1])