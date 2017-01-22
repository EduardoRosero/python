from animales import Gato
from animales import Leon
from animales import creador_gatos
from animales import CONSTANTES
gato = creador_gatos("Nuevo gato por paquete")
print(gato.nombre)
print(CONSTANTES)
"""Un paquete es una carpeta que contiene un archivo
de nombre __init__.py y sus respectivos modulos"""