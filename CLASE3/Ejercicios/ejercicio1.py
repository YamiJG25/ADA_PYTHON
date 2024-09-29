# Contador de numeros especificos.

# Escribe un programa que cuente cuántas veces aparece un número específico en una lista.
# Define una lista de números predefinida o pídele al usuario que ingrese los números.
# Pide al usuario que ingrese un número a buscar.
# Usa el método count() para determinar cuántas veces aparece el número en la lista.
# Muestra el resultado.

mi_lista = [1, 2, 3, 4, 6, 6, 6, 9, 9, 7, 8, 9, 6, 6] 
print("Lista de numeros:", mi_lista)
buscar_numero = int(input("Ingrese numero a buscar: "))
conteo = mi_lista.count(buscar_numero)
print("El numero 9 aparece: ", conteo, "veces en la lista.")