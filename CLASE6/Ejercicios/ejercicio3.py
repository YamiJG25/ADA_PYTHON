# Ejercicio con range, enumerate, y break/continue
# Escribe un programa que:
# Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor.
# Utilice continue para saltar cadenas vacías.
# Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres.

cadenas = ["Juan", "Nuez", "Roma", "Napole", "Amsterdam", "Barcelona"]

for indice, valor in enumerate(cadenas):
    if valor == " ":
        continue
    print(f"El indice es el: {indice}, y el valor es: {valor}")
    
    if len(valor) > 5:
        print(f"Se encontró una cadena con más de 5 caracteres: '{valor}'")
        break

