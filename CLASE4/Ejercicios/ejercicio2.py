# Ejercicio 2: Verificación de Elementos en una Tupla
# Crea una tupla llamada mi_tupla con los siguientes elementos: (3, 6, 9, 12, 15).
# Verifica si el número 6 está en la tupla y muestra un mensaje indicando si está presente o no.
# Verifica si el número 7 está en la tupla y muestra un mensaje indicando si está presente o no.

mi_tupla = (3, 6, 9, 12, 15)

verificar_numero = 6
if verificar_numero in mi_tupla:
    indice_del_valor = mi_tupla.index(verificar_numero)
    print("El numero: ", verificar_numero, "esta presente en la tupla.")
else:
    print("El numero: ", verificar_numero, "no esta presente en la tupla.")