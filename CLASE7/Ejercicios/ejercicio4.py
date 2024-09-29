# Ejercicio de while con Condiciones y Contadores
# Desarrolla un programa que:
# Use un bucle while para generar números de la serie de Fibonacci.
# Continúe generando números hasta que el número actual sea mayor o igual a 100.
# Imprima la serie de Fibonacci generada.

a, b = 0, 1

fibonacci = []

while a <= 100:
    fibonacci.append(a) 
    a, b = b, a + b
print("Fibonacci generadas: ", fibonacci)
    

    