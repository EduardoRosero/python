#Leer datos de la terminal e imprimir datos de la terminal

nombre = "Eduardo"

puts "Hola #{nombre}" #Agrega un salto de linea al final de la linea
print "Hola #{nombre}" #No da salto de linea

puts "Ingrese el nombre"
nombre = gets
puts "Hola #{nombre}"

#Contar numero de letras del nombre

puts "Ingrese el nombre"
nombre = gets
nombre = nombre.chomp #Elimina el ultimo caracter de la cadena que es \n es decir va a quedar el texto original sin el salto de linea extra
puts "Hola, tu nombre tiene #{nombre.length} letras"

