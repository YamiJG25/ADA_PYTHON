# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario
# Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968.
# Elimina el género del diccionario.
# Imprime el diccionario después de cada operación.

libro = {
    "titulo" : "El principito",
    "autor" : "Antoine de Saint-Exupéry",
    "año de publicacion" : 1943,
    "genero" : "Literatura infantil"
}

libro["año de publicacion"] = 1968
print("Libro con nuevo año de publicacion: ", libro)

del libro["genero"]
print("Despues de elimirar genero: ", libro)