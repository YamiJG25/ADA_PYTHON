# Ejercicio Integrador
# Desarrolla un programa que haga lo siguiente:
# Usar un bucle for con range para iterar sobre los números del 1 al 20.
# Usar continue para saltar los números divisibles por 3.
# Usar break para detener la iteración si se encuentra un número mayor que 15.
# Crear un set con los números restantes y verificar si algún número es par.
numeros_restantes = set()

for numero in range(1, 21):
    if numero % 3 == 0:
        continue
    if numero > 15:
        break
    print(numero)
    
    numeros_restantes.add(numero)

numero_par = any(numeros % 2 == 0 for numeros in numeros_restantes)
print("Números restantes:", numeros_restantes)
print("¿Hay números pares?", numero_par)




    
    
    



