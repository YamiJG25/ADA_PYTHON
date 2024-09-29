# Creamos diccionario
estudiante = {
    "nombre" : "Laura",
    "edad" : 22,
    "curso" : "Ingenieria",
    "ciudad" : "Barcelona"
}

#Imprimir el diccionario
print("Diccionario original: ", estudiante)

# Eliminar el elemento con la clave "curso" usando Del
del estudiante["curso"]

# Imprimimos el diccionario despues de eliminar curso
print("Diccionario despues de eliminar curso: ", estudiante)