# Ejercicio de Sets y Operaciones Básica
# Escribe un programa que:
# Cree dos sets de números.
# Realice operaciones de unión, intersección y diferencia entre estos sets.
# Imprima los resultados de cada operación.

set1_num = {10, 20, 30, 40,50}
set2_num = {5, 15, 20, 35, 45}

union_sets = set1_num | set2_num
print(f"Resultado de union: {union_sets}")

interseccion_sets = set1_num & set2_num
print(f"Resultado de interseccion: {interseccion_sets}")

dif_sets = set1_num - set2_num
print(f"Resultado de diferencia: {dif_sets}")