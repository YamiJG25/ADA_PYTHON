# Ejercicio de Sets y for
# Crea un programa que reciba una lista de números y realice las siguientes operaciones:
# Crear un set a partir de la lista para eliminar duplicados.
# Iterar sobre el set e imprimir cada número.
# Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.

lista1 = {9, 7, 25, 12, 20, 3}
lista2 = {9, 17, 35, 12, 22, 3}

union = lista1.union(lista2)
print(f"Lista despues de eliminar duplicados: {union}")

for numero in union:
    print(f"Se imprime cada numero despues de iterar: {numero}")
    
mayor_a = 17
nuevo_set = set()

for numero in union:
    if numero > mayor_a:
        nuevo_set.add(numero)
print(f"Numeros mayores a 17: {nuevo_set}")