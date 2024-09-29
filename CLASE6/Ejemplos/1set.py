# Setsion de asistentes de un evento
# Crear un programa que administre una lista de asistentes o eventos sin permitir 
#duplicados y que realice operaciones entre dos listas.

# Crear conjuntos de inviados
invitados_viernes = {"Ana", "Carlos", "Pedro", "Luis","Clara"}
invitados_sabado = {"Carlos", "Luis", "Sofia", "Maria", "Pedro"}

# Mostrar a los invitados unicos que asisten el Viernes
print(f"Invitados de Viernes: {invitados_viernes}")

# Mostrar a los invitados unicos que asisten el Sabado
print(f"Invitados de Sabado: {invitados_sabado}")

# Mostrar la union (Quien asistio al menos un dia)
todos_asistentes = invitados_sabado | invitados_viernes
print(f"Asistentes de ambos dias: {todos_asistentes}")

# Mostrar la interseccion (quien asistio ambos dias)
solo_viernes = invitados_viernes & invitados_sabado
print(f"Asistentes solo Viernes: {solo_viernes}")

# Mostrar la diferencia
solo_viernes = invitados_viernes - invitados_sabado
print(f"Asistencia solo el Viernes: {solo_viernes}")

# Agregar un nuevo invitado el Sabado
invitados_sabado.add("Miguel")
print(f"Invitados del Sabado despues de agregar un nuevo invitado: {invitados_sabado}")

# Eliminar un invitado que cancelo
invitados_sabado.remove("Maria")
print(f"Invitados del Sabado despues de eliminar un invitado: {invitados_sabado}")

# Comprobar si Ana asistio el Sabado
print(f"Ana asistio el Sabado?: {"Ana" in invitados_sabado}")
print(f"Ana asistio el Viernes?: {"Ana" in invitados_viernes}")