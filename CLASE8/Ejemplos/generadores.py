# Ejemplo basico de generador
#Generador que porduce numeros del 1 al 5
# Definicion del generador
def contador():
    # Itera sobre los numero del 1 al 5
    for i in range(1, 6): # Itera sobre los numeros del 1 al 5 (no contempla el 6)
        yield i #Porduce el valor de i y pausa la ejecucion

# Crear una instancia para el generador
gen = contador() # Gen es un objeto generador

# Iterar sobre los valores producidos por el mismo generador
for numero in gen:
    print(numero) # Imprime cada uno de los numeros producido por el generador
print()

# Ejemplo 2 - Fibonacci (con generadores)
def fibonacci():
    a,b = 0,1 # Inicializa los primeros dos numeros de la secuencia
    while True: # Esto es un cilo infinito para generar los numeros
        yield a # produce el valor de a y pausa la ejecucion
        a,b = b, a + b # Actualiza a y b para la siguiente iteracion
        
gen = fibonacci() # Gen es un objeto generador que produce numeros de fibonacci

# Obtener los primeros 10 numeros de fibonacci
for _ in range(10):
    print(next(gen)) # Obtiene el siguiente numero en la secuencia y lo imprime