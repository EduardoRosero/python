cadena = "Hola"

cadena2 = 'Mundo'

#Concatenacion

conc = cadena + cadena2
puts conc

#Interpolacion
inter ="Hola #{cadena2.upcase}"
puts inter

inter ="Hola #{cadena2.downcase}"
puts inter

inter ="Hola #{cadena2.capitalize}"
puts inter

puts "".methods #Ver los metodos de los strings