# Ejemplo 1 - Callback operacion basica
def suma(a, b):
    return a+ b

def restar(a, b):
    return a- b

# Funcion que recibe otra funcion como collback
def operar(a, b, funcion_collback):
    resultado = funcion_collback(a, b)
    print(f"Resultado de la operacion : {resultado}")
    
# Uso de la funcion operar con diferentes collback
print("    Ejemplo de collback simple")
operar(5, 3, suma)
operar(5, 3, restar)

# Uso de una lambda como collback
operar(5, 3, lambda a, b: a * b)
operar(5, 3, lambda a, b: a / b)
