# Ejercicio 5: Diccionario dentro de una Lista
# Crea una lista de diccionarios donde cada diccionario representa un producto en una tienda, con claves:
# Nombre
# Precio
# Cantidad en stock
# Imprime el nombre y el precio del segundo producto en la lista.

productos = [
    {
        "nombre1" : "yerba",
        "precio1" : 2500,
        "stock1" : 5
        },
    {
        "nombre2" : "cafe",
        "precio2" : 1500,
        "stock2" : 2
        },
    {
        "nombre3" : "atun",
        "precio3" : 3000,
        "stock3" : 6
        }
]

segundo_producto = productos[1]
print("El segundo producto es: ", segundo_producto["nombre2"], "y su precio es: ", segundo_producto["precio2"], "pesos")