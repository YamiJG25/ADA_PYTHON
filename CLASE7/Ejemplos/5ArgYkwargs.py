# Ejemplo 1 - Funcion que usa *args
def sumar_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print("Ejemplo 1 - Funcion que usa *args")
print(f"Suma de 1, 2, 3: {sumar_numeros(1, 2, 3)}")
print(f"Suma de 4, 5, 6, 7, 8: {sumar_numeros(4, 5, 6, 7, 8)}")
print()

# Ejemplo 2 - Funcion que usa **Kwargs
def mostrar_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

print("Ejemplo 2 - Funcion que usa **Kwargs")
mostrar_detalles(nombre= "Ana", edad=30, cuidad="Madrid")

# Ejemplo 3 - Convinados
def mostrar_info_completa(*args, **kwargs):
    print("Argumentos no nonombrados: ")
    for arg in args:
        print(args)
    print("\nArgumentos nombrados: ")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
print("Ejemplo 3 - Convinados")
mostrar_info_completa(1, 2, 3,nombre= "Ana", edad=30, cuidad="Madrid")