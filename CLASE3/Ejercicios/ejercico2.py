# Suma de sublistas
# Crea un programa que tome una lista de números 
# y calcule la suma de una sublista especificada por el usuario.

# Define una lista de números predefinida.
# Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.
# Usa slicing para obtener la sublista.
# Suma los elementos de la sublista.
# Muestra la suma.

lista = [10, 20, 35, 42, 55, 60, 5]
print("Lista de numeros: ", lista)
inicio = int(input("Ingrese el indice de inicio de la sublista: "))
fin = int(input("Ingrese el indice del fin de la sublista: "))
sublista = lista[inicio:fin]
print(sublista)
suma = sum(sublista)
print("La suma de sublista es: ", suma)