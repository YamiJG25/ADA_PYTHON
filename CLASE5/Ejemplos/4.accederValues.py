# Creamos un diccionario
persona = {
    "nombre" : "Analia",
    "edad" : 36,
    "Ciudad" : "Colon - Entre Rios"
}

# Usamos el metodo values
valores = persona.values()

# Imprimir
print("Valores del diccionario: ", valores)

# Convertir valores en una lista
valores_lista = list(valores)
print("Valores como lista: ", valores_lista)