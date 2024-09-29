# Crear un diccionario
persona = {
    "nombre" : "Veronica",
    "edad" : 25,
    "ciudad" : "Buenos Aires"
}

# Usar el metodo -Get() para acceder a los elementos
nombre = persona.get("nombre")
edad = persona.get("edad")
ciudad = persona.get("ciudad")

# Imprimir
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)

# Intentar acceder a una clave que no existe usando .get()
pais = persona.get("pais")
print("Pais: ", pais)

# Usar get con un valor predeterminado si la clave no existe
pais_con_valor_predeterminado = persona.get("Pais", "No especificado")
print("Pais (con valor predeterminado): ", pais_con_valor_predeterminado)