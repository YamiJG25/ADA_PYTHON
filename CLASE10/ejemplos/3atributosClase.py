# 3. Atributos de Clse

# Definimos la Clase coche
class Coche:
    ruedas = 4 # Atributo de clase: todas las instancias de coche tienen 4 ruedas.
    
    def __init__(self, marca, modelo):
        self.marca = marca # Atributo de instancia
        self.modelo = modelo # Atributo de instancia
        
# Imprimir el atributo de coche
print(Coche.ruedas)

# Crear instancia de la clase coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

# Acceder al atributo de clase de las instancias
print(coche1.ruedas)
print(coche2.ruedas)

# En la Clase Coche el atributo ruedas es un atributo 
# de clase que se aplica a todas las instancias de la clase, 
# estableciendo que cada coche tiene 4 ruedad.
# Este atributo se puede acceder tanto desde las clases como desde las instancias, 
# lo que permite compartir datos comunes entre todos los objetos de esa clase.