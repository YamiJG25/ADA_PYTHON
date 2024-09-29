# Atributos de Instancia

# Definimos la Clase
class Gato:
    def __init__(self, color, nombre):
        self.color = color # atributo de instancia
        self.nombre = nombre # atributo de instancia

# Crear diferentes objetos (instancias) de la clase gato.
gato1 = Gato("negro", "Felix")
gato2 = Gato("gris", "Aries")

# Acceder a los atributos de instancia
print(gato1.color)
print(gato2.color)

# La clase gato incluye atributos de la instancia, color y nombre, 
# que se inicializa en el constructor.
# Cada objeto creado a partir de esta clase (como gato1 y gato2) tienen 
# sus pripios valores para estos atributos.
# La que permite que diferentes instancias representen gatos distintos 
# con caracteristicas unicas.