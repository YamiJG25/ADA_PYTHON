# Programa para imprimir cuadrado de numeros y calcular la suma.

numeros = [1, 2 ,3, 4, 5]

# Iniciamos variable
suma_cuadrados = 0

# Interar sobre cada numero en la lista
for numero in numeros:
    #Calcular si el cuadrado del numero
    cuadrado = numero ** 2
    # Imprimir el cuadrado
    print(f"El cuadrado de {numero} es: {cuadrado}")
    #Agregar el cuadrado de la suma
    suma_cuadrados += cuadrado
#Imprimir
print(f"La suma de los cuadrados es: {suma_cuadrados}")