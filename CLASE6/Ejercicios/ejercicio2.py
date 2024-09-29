# Ejercicio de while y for
# Desarrolla un programa que haga lo siguiente: 
# Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0.
# Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.


numeros_a_ingresar = []
while True:
    entrada = input("Ingrese los numeros que desee (para terminar ingrese el `0`): ")
    numero = int(entrada)

    if numero == 0:
        break
    else:
        numeros_a_ingresar.append(numero)
print("Números ingresados:", numeros_a_ingresar)

suma = 0

for numero in numeros_a_ingresar:
    suma += numero

print("La suma de los números ingresados es:", suma)