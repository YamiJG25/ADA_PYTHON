# Crear un diccionario
persona = {
    "nombre" : "Emilia",
    "edad" : 33,
    "Ciudad" : "CABA",
    "profesion" : "Vererinaria"
}

# Imprimir el diccionario original
print("Diccionario original: ", persona)

# Usamos popitem para eliminar y obtener el ultimo por clave-valor
ultimo_elemento = persona.popitem()

# Imprimimos el par clave-valor
print("Ultimo par clave-valor eliminado: ", ultimo_elemento)

# Imprimimos despues de usar popitem
print("Diccionario despues de usar popitem: ", persona)