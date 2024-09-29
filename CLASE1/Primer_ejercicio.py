# 1. delaclacion de variables y constantes 
edad = 25  # numero
nombre = "Ana" # cadena de texto
esta_estudiando = True # Booleano

# Declaraciones de constantes
PI = 3.14 # NUMERO
PAIS = "Argentina" # cadena de texto

# 2. Leer valores por teclado
edad = int(input("Introduce tu edad: "))  # leer un numero entero
nombre = input("introduce tu nombre: ")   # Leer una cadena de texto
esta_estudiando = input("¿Estas estudiando? (si/no): ").lower() == "si" # leer y convertir a booleano

# 3. Tipos de datos
cantidad_de_libros = 10   #numero(int) 
titulo_libro = "El principito" # cadena de texto (string)
es_interesante = True # Booleano (bool)
temas = ["Aventura", "Fantasia", "Filosofia"]  # Lista (array)
autor = {
    "nombre": "Antoine de saint-exupery",
    "nacionalidad": "Francesa"
}

#convertir tipos de datos
edad_str = str(edad)   # convertir numero a cadena de texto
cantidad_de_libros_float = float(cantidad_de_libros)   #convertir entero a numero de punto flotante

# 4 imprimir resultados en la consola
print("Nombre:", nombre)
print("Edad:", edad)
print("¿Esta estudiando?", esta_estudiando)
print("Constante PI:", PI)
print("Constante Pais:", PAIS)
print("Cantidad de libros:", cantidad_de_libros)
print("Titulo del libro:", titulo_libro)
print("¿Es interesante?", es_interesante)
print("Temas del libro:", temas)
print("Autor del libro:", autor)
print("Edad (como cadena de texto):", edad_str)
print("Cantidad de libros (como float):", cantidad_de_libros_float)