import sys

#Nos permite imprimir los parametros que recibimos de consola
#Para colocar a nuestro script en un valor incial
"""if __name__ == '__main__':
	print(sys.argv)
"""
if __name__ == '__main__':
	if len(sys.argv)==1:
		print("Es necesario colocar al menos un argumento")
	else:
		if sys.argv[1] == "help":
			print("Para inquietudes y ayuda comunicate a 666")
		print(sys.argv)