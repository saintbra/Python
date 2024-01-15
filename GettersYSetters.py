class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

brandon = Persona("Patricio", 21)

nombre = brandon.get_nombre()
print(nombre)

brandon.set_nombre("Brandon")

nombre = brandon.get_nombre()
print(nombre)
