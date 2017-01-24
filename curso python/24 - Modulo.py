#Cuando un proyecto crece se debe modularizar el codigo
#Es decir se debe separar el codigo en modulos
#Los modulos son archivos con extension .py que se los puede utilizar dentro de otros archivos
#Los archivos que se van a utilizar mutuamente deben estar en el mismo nivel de directorios

import Calculadora
#Esto nos creara un archivo .pyc compilado con nuestro modulo importado
#Son compilados ya que son mas rapidos en ejecutarse que los modulos reales
#Siempre se crea este archivo para que las siguientes ejecuciones se las haga a traves del archivo compilado y no el interpretado

resultado = Calculadora.suma(100, 20)
print("La suma es: " , resultado)
