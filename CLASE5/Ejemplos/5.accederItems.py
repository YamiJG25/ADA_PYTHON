# Crear un diccionario
persona = {
    "nombre" : "Alejandra",
    "edad" : 30,
    "Cuidad" : "Merida"
}

# Usamos el metodo items
pares_clave_valor = persona.items()

# Imprimimos
print("Pares clave valor: ", pares_clave_valor)

# Convertir valores en una lista
valores_lista = list(pares_clave_valor)
print("Valores como lista: ", valores_lista)