class Lapiz:#Plantilla
	#Atributos
	color = "Amarillo" #Color por default de nuestra plantilla lapiz
	contiene_borrador =False #Por defecto nuesta plantilla lapiz no tiene borrador
	usa_grafito = True #Por defecto nuestra plantilla lapiz si usa grafito

	#Metodos, son funciones dentro de las clases
	def dibujar(self): #Se debe pasar como argumento la palabra self
		print("El lápiz está dibujando")
	def borrar(self):
		if self.puede_borrar(): #Llamada a un método dentro de otro método
			print("El lápiz está borrando")
		else:
			print("El lápiz no pueded borrar")
	def puede_borrar(self):
		return self.contiene_borrador #Llamar un atributo desde un método


#Crear un objeto, instanciar la clase

lapiz_generico = Lapiz()
print(lapiz_generico.color, lapiz_generico.contiene_borrador)
lapiz_generico.dibujar() #Llamada al metodo
lapiz_generico.contiene_borrador= True
lapiz_generico.borrar() 