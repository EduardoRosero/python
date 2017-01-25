x=10
y=5

s = x+y
puts "Suma: #{s}"

s = x-y
puts "Resta: #{s}"

s = x*y
puts "Multiplicacion: #{s}"

s = x/y
puts "Division: #{s}"

s = x%y
puts "Residuo: #{s}"

s = x**y
puts "Potencia: #{s}"


s = x+x*y.to_f
puts s

print ("Ingrese un numero: ")
numero = gets.chomp
numero = numero.to_i
residuo = numero%2

if(residuo==0)
	puts ("#{numero}  es par")
else
	puts ("#{numero}  es impar")
end
