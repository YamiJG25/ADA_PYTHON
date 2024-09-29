# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
# Usa el método index para encontrar la posición de la fruta "banana".
# Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.

frutas = ("manzana", "banana", "cereza")
indice_de_banana = frutas.index("banana")
print("La posicion de la fruta banana es: ", indice_de_banana, "en la tupla")

verificar = "naranja"

if verificar in frutas:
    indice_de_naranja = frutas.index(verificar)
    print(f"La fruta {verificar} se encuenta en la posicion {indice_de_naranja} de la tupla.")
else:
    print(f"La fruta {verificar} no esta en la tupla.")