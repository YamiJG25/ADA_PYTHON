# Definir Listas

# Lista Vacia
lista_vacia = []
print("lista vacia: ", lista_vacia)
print(f"Lista vacia: {lista_vacia}") # otra forma (concatenacion)

# Lista de elementos iniciales / numeros
lista_elementos = [1, 2,3,4,5]
print("lista con elementos iniciales: ", lista_elementos)

# Lista de cadenas
lista_cadenas = ["Manzana", "banana", "Cereza"]
print("lista de cadenas: ", lista_cadenas)

# Lista Mixta
lista_mixta = [42, "texto", 3.14, [1, 2, 3]] # lista anidada (una lista dentro de otra)
print("lista mixta: ", lista_mixta)

# Lista con elementos repetidos
lista_repetidos = [0] * 5
print("listas con elementos repetidos: ", lista_repetidos)

# Lista a partir de otros iterables
cadena = "Yami"
lista_de_catacteres = list(cadena)
print("Lista a partir de otros iterables (cadena): ", lista_de_catacteres)