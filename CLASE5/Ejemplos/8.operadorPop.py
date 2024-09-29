# Creamos diccionario
persona = {
    "nombre" : "Alejandra",
    "edad" : 30,
    "Cuidad" : "Merida"
}

# Usamos popo para eliminar la clave edad y obtener su valor
valor_eliminado = persona.pop("edad")

# Imprimimos el valor eliminado y el diccionario resultante
print("Valor eliminado: ", valor_eliminado)
print("Diccionario despues de eliminar edad: ", persona)

# Usar pop con una clave que no existe y un valor por defecto
valor_inexistente = persona.pop("pais", "no especificado")
print("Valor cuando la clave no existe: ", valor_inexistente)