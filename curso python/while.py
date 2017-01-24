#CICLO WHILE


contador =0
"""while contador <10: #> >= < <=
	print(contador)
	contador+=1 #Aumentar en 1 el contador contador = contador +1
	if contador==5:
		print("Estamos en el numero 5")
		continue

	if contador ==6:
		break #Permite cortar el ciclo demanera abrupta
else:
	print("El while termino")"""

bandera = True
while bandera:
	print(contador)
	contador+=1 #Aumentar en 1 el contador contador = contador +1
	if contador==5:
		print("Estamos en el numero 5")
		continue

	if contador ==6:
		bandera = False #Permite cortar el ciclo demanera abrupta
else:
	print("El while termino")