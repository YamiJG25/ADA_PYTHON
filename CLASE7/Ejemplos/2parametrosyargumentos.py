# Definicion de funcion: parametros posicionales, con nombre y predeterminados
def presentar_presona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesion: {profesion}")
    print()
    
# Ejemplo de llamada a la funcion
# Usando argumentos posicionales

print("Ejemplo con argumentos posicionales: ")
presentar_presona("Ana", 30)

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre: ")
presentar_presona("Luis", 25, ciudad="Madrid", profesion="Ingeniero")

# Usando todos los argumentos con nombre
print("Ejemplo de todos los argumentos con nombre: ")
presentar_presona(nombre="Marta", edad=34, ciudad="Madrid", profesion="Ingeniero")

