# Programa para adivinar un numero secreto
# Definir el nuemro secreto
numero_secreto = 7

# Inicializar la variable para almacenar el numero del usuario
numero_adivinado = None

# Mensaje inicial
print("Adivina el nuemro secreto (entre el 1 y el 10): ")

# Bucle while que continua hasta que el usuario adivine el numero secreto
while numero_adivinado != numero_secreto:
    #Solicitar al usuario que ingrese un numero
    numero_adivinado = int(input("Introduce un numero: "))
    
    #Comprobar si el numero adivinado es correcto
    if numero_adivinado < numero_secreto:
        print("Demaciado bajo. Intenta de nuevo.")
    elif numero_adivinado > numero_secreto:
        print("Demaciado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades has adivinado el numero secreto!")
        
# Mensaje de finalizacion del juego
print("Gracias por jugar.")