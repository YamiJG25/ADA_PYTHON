# Ejercicio de List Comprehension con range y for
# Crea un programa que:
# Genere una lista de números del 1 al 10 usando range.
# Cree una nueva lista que contenga el cuadrado de cada número solo si el número es impar.

lista_numeros = [numeros for numeros in range(1, 11)]

print("Lista de numeros del 1 al 10: ", lista_numeros)

print("\n")

cuadrados_impares = [numero ** 2 for numero in lista_numeros if numero % 2 != 0]

print("Nueva lista con cuadrados de impares:", cuadrados_impares)

print("\n")
