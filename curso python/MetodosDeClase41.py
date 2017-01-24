class Animal:
	volador=True

class Cocodrilo(Animal):
	def __init__(self, nombre):
		self.nombre = nombre

	@classmethod #Para hacerlo metodo de clase agregamos esta etiqueta y cambiamos el self por cls
	def new(cls, nombre): #Este metodo es de instancia y se lo debe decorar para hacerlo de clase
		cls.volador=False #Accedemos al atributo de la clase padre
		return Cocodrilo(nombre) 

cocodrilo = Cocodrilo.new("coco") #No necesito realizar uns instancia para hacer new
print(cocodrilo.nombre)
print(cocodrilo.volador) #Cambiamos el valor del atributo desde la clase y no desde el objeto instanciado

"""La diferencia entre los metodos de instancia y los metodos de clase es que
los metodos de clase pueden acceder a los atributos o a los mtoodos de las clases 
que estamos heredando"""