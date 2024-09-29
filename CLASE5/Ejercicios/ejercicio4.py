# Ejercicio 4: Lista de Diccionarios
# Crea una lista de diccionarios, donde cada diccionario representa un estudiante con las siguientes claves:
# Nombre
# Edad
# Calificaciones (que es una lista de números)
# Imprime el nombre y las calificaciones del primer estudiante en la lista.

estudiantes = [
    {
        "nombre1" : "Matias",
        "Edad1" : 23,
        "calificaciones1" : [10, 8, 7, 6]
        },
    {
        "nombre2" : "Ezequiel",
        "Edad2" : 25,
        "calificaciones2" : [5, 2, 8, 7]
        },
    {
        "nombre3" : "Josefina",
        "Edad3" : 20,
        "calificaciones3" : [4, 6, 8, 2]
        }
]

primer_estudiante = estudiantes[0]
print("El nombre del primer estudiante es: ", primer_estudiante["nombre1"], "y sus calificacions son: ", primer_estudiante["calificaciones1"])
