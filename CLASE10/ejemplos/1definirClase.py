# Definir Clase en python

# Definimos una clase llamada coche
class Coche:
    # metodo __init-- es el contructor que se llama al crear un nuevo objeto
    def __init__ (self, marca, modelo):
        # self es una referencia al objeto que estamos creando
        # inicializamos los atributos de la instancia
        self.marca = marca # atributo de instancia: guarda la marca del coche
        self.modelo = modelo # atributo de instancia: guarda el modelo del coche

# la clase coche es una plantilla para crear objetos de tipo auto
# contiene un metodo constructor __init__ que inicializa los atibutos
# especificos de cada coche que hagamos.
# como por ejemplo: marca, modelo usando la referencia self para 
# distinguir entre las profiedades del objeto y los parametros basados 
# al contructor.