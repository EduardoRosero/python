from .gato import Gato
#Se antepone el punto porque el interprete va a ir a buscar lo que esta a la derecha del punto en la carpta en el mismo nivel del archivo __init__.py
from .leon import Leon
CONSTANTES = "Esto es una constante"
#Podemos definir la logica de nuestro init, agregando variables, constantes, metodos
def creador_gatos(nombre):
	return Gato(nombre)