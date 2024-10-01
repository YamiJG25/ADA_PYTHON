import math 
# Este modulo math, se usa para realizar todo tipo de 
# operaciones matematicas abanzadas.

# Constantes
print(f"El valor de Pi es: {math.pi}")
print(f"El valor de e es: {math.e}")

# Calcular el seno de 90 grados
angulo_grados = 90
angulo_radianes = math.radians(angulo_grados)
print(f"Seno de {angulo_grados} grados es: {math.sin(angulo_radianes)}")

# Calcular logaritmos
numero = 100
print(f"Logaritmo natural de {numero} es: {math.log(numero)}")
print(f"Logaritmo en base 10 de {numero} es : {math.log10(numero)}")

# Redondeo
numero = 4.6
print(f"{numero} redondeado hacia abajo es: {math.floor(numero)}")
print(f"{numero} redondeado hacia arriba es: {math.ceil(numero)}")

# Raiz cuadrada
num = 16
print(f"La raiz cuadrada de {num} es: {math.sqrt(num)}")
