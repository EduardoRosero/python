#import Calculadora

#from Calculadora import suma, resta, multiplicacion
from Calculadora import (suma, 
						resta, 
						multiplicacion)

from Calculadora import division as div #Podemos renombrar las funciones

from Calculadora import * #Estamos importando todas las funciones de Calculadora pero no conocemos cuales son

resultado = div(10,20)
print(resultado)

resultado = suma(10,20)
print(resultado)