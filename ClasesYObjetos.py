class Lapiz:#Plantilla
	color = "Amarillo" #Color por default de nuestra plantilla lapiz
	contiene_borrador =False #Por defecto nuesta plantilla lapiz no tiene borrador
	usa_grafito = True #Por defecto nuestra plantilla lapiz si usa grafito


#Crear un objeto, instanciar la clase

lapiz_generico = Lapiz()
print(lapiz_generico.color, lapiz_generico.contiene_borrador)