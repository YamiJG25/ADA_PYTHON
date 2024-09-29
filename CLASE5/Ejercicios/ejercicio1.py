# Ejercicio 1: Crear y Acceder a un Diccionario Básico
# Crea un diccionario que contenga la siguiente información sobre un libro:
# Título
# Autor
# Año de publicación
# Género
# Accede e imprime cada uno de estos valores usando las claves correspondientes.

libro = {
    "titulo" : "El principito",
    "autor" : "Antoine de Saint-Exupéry",
    "año de publicacion" : 1943,
    "genero" : "Literatura infantil"
}

titulo = libro["titulo"]
autor = libro["autor"]
año_de_publicacion = libro.get("año de publicacion")
genero = libro.get("genero")

print("Titulo: ", titulo)
print("Autor: ", autor)
print("Año de publicacion: ", año_de_publicacion)
print("Genero: ", genero)