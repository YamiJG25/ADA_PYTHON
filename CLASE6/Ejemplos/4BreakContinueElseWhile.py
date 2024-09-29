# Programar que pide numero hasta que se ingrese un nuemro negativo.

# Inicializamos la variable para acumular la suma de los numero positivos ingresados.

suma = 0

# Inicializamos un ciclo infinito usando while true
while True:
    #Solciitamos al usuario que introduzca un numero
    # La entrada se convierte en nuemro entero
    entrada = int(input("Introduce numero (negativo para terminar): "))
    
    # Verificamos si el numero ingresado es negativo
    if entrada < 0:
        # Si el numero es negativo, solicitamos del ciclo usando
        break
    
    # Sumamos el numero positivo ingresado a la variable suma
    suma += entrada
    
    # Verificar si el numero ingresado es par
    if entrada % 2 == 0: #para saber si el numero es par
        # Si el numero es par usamos continue para saltar la impresion 
        # y pasar a la siguiente interaccion del ciclo
        continue
    
    #Si el numero ingresado es par (es impar), se ejecuta esta linea:
    print(f"Numero impar ingresado: {entrada}")
    
# Mensaje final
print(f"El ciclo ha terminado porque se ingreso un numero negativo.")
print(f"La suma de los numeros ingresados es: {suma}")