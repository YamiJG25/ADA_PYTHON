# Ejercicio 5: Manejo de Matrículas en una Tupla
# Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
# Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
# Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.

matriculas = (101, 102, 103, 104, 105)

numero102 = matriculas.count(102)
print("El numero 102 aparece: ", numero102, "veces en la tupla")

numero104 = matriculas.index(104)
print("El numero 104 se encuentra en la posicion: ", numero104, "de la tupla")