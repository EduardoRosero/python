puts (10> 5)
puts(5>10)

puts(10<5)
puts(5<10)

puts(5<5)
puts(5<=5)
puts(5>=5)

puts(10<=>10) #Si iguales devuelve 0
puts(20<=>10) #Si primero mayor devuelve 1
puts(10<=>20) #Si primero menor devuelve -1

puts("hola" == "hola")

puts(1 == 1.0)

puts(1.eql?(1.0))

puts("hola".eql?("hola"))

puts("hola".equal?("hola")) #Devuelve falso debido a que compara el id del objeto

puts("hola".object_id, "hola".object_id) #Los id que nos muestra son difrentes porque son objetos diferentes

hola="hola"

puts(hola.object_id, hola.object_id) #Como es el mismo objeto nos muestra el mismo id

puts(10!=10)

puts(10!=20)