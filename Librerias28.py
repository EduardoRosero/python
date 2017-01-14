import random #Trabajar con aleatorios


valor = random.randint(0,10) #Numero aleatorio entre 0 y 10 incluidos
print (valor)

lista = [True, "String", 25, False, 24]
valor = random.choice( lista ) #Obtener un aleatorio de una lista
print (valor)

#Reordenar nuestra lista con random
print (lista)
random.shuffle(lista)
print (lista)



import datetime #Trabajar con hora y fecha del sistema
print(datetime.datetime.now())

import sys #Trabajar con opciones del sistema
import time
#Hacer barra de progreso

for i in range(100):
	time.sleep(0.5) #Delay de medio segundo
	sys.stdout.write("\r%d %%" % i) #Imprimir siempre en la misma posicion de la terminal
	sys.stdout.flush()