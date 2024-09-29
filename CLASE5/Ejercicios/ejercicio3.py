# Ejercicio 3: Anidación Básica de Diccionarios
# Crea un diccionario que represente una persona con las siguientes claves:
# Nombre
# Edad
# Dirección (donde la dirección es otro diccionario con claves: Calle, Ciudad, Código postal)
# Imprime la ciudad de la dirección.

persona = {
    "nombre" : "Yamila",
    "edad" : 34,
    "direccion" : {
        "calle" : "primavera 24",
        "ciudad" : "Buenos Aires", 
        "codigo postal" : 1834
    }
}

print("Ciudad: ", persona["direccion"]["ciudad"])