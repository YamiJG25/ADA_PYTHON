# Definimos distintas variables para usar en las comparaciones
a = 10
b = 5
c = 15
d = 8

# Operador AND
# Ambas condiciones deben ser verdaderas para que el resultado sea TRUE
resultado_and =(a > b) and (c > d)
print(f"resultado de (a > v) and (c > d): {resultado_and}")
# (a > b) es True porque 10 > 5
# (c > d) es True porque 15 > 8

# Operador OR
# Al menos una de las condiciones debe ser verdadera para que el resultado sea True
resultado_or = (a < b) or (c > d)
print(f"resultado de (a < b) or (c > d): {resultado_or}")
# (a < b) es False porque 10 no es menor que 5
# (c > d) es True porque 15 es mayor que 5

# Operador NOT
# El operador not invierte el valor de la expresion
resultado_not = not (a < b)
print(f"resultado de not (a < b): {resultado_not}")
# (a < b) es False porque 10 no es menor que 5
# not False resulta en true

# Combinacion de los operadores logicos AND, OR Y NOT
resultado_combinado = (a > b) and (not (c < d)) or (b < c)
print(f"resultado combinado: {resultado_combinado}")
# (a > b) es True porque 10 > 5
# (c < d) es False porque 15 no es menor que 8, y not (false)
# (a > b) and (c < d) es True porque true and true resulta en true
# True o true resulta en true